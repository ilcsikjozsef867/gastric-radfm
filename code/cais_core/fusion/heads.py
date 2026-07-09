from __future__ import annotations

from dataclasses import dataclass

import torch
from torch import nn
import torch.nn.functional as F


@dataclass(frozen=True)
class FusionSpec:
    image_dim: int
    radiomic_dim: int
    clinical_dim: int
    hidden_dim: int


class BoundaryGate(nn.Module):
    def __init__(self, hidden_dim: int) -> None:
        super().__init__()
        self.scale = nn.Sequential(nn.Linear(1, hidden_dim), nn.Sigmoid())

    def forward(self, entropy: torch.Tensor, clinical: torch.Tensor) -> torch.Tensor:
        gate = self.scale(entropy.view(-1, 1))
        return gate * clinical


class DecisionFusion(nn.Module):
    def __init__(self, spec: FusionSpec) -> None:
        super().__init__()
        self.image = nn.Linear(spec.image_dim, spec.hidden_dim)
        self.radiomic = nn.Linear(spec.radiomic_dim, spec.hidden_dim)
        self.clinical = nn.Linear(spec.clinical_dim, spec.hidden_dim)
        self.gate = BoundaryGate(spec.hidden_dim)
        self.out = nn.Sequential(nn.LayerNorm(spec.hidden_dim * 3), nn.Linear(spec.hidden_dim * 3, spec.hidden_dim), nn.SiLU())

    def forward(self, image: torch.Tensor, radiomic: torch.Tensor, clinical: torch.Tensor, entropy: torch.Tensor) -> torch.Tensor:
        image_h = self.image(image)
        radio_h = self.radiomic(radiomic)
        clinical_h = self.gate(entropy, self.clinical(clinical))
        return self.out(torch.cat([image_h, radio_h, clinical_h], dim=-1))


class MultiTaskHead(nn.Module):
    def __init__(self, hidden_dim: int) -> None:
        super().__init__()
        self.ct = nn.Linear(hidden_dim, 5)
        self.cn = nn.Linear(hidden_dim, 3)
        self.cm = nn.Linear(hidden_dim, 2)
        self.resectable = nn.Linear(hidden_dim, 2)
        self.neoadjuvant = nn.Linear(hidden_dim, 2)

    def forward(self, hidden: torch.Tensor) -> dict[str, torch.Tensor]:
        return {
            "ct": self.ct(hidden),
            "cn": self.cn(hidden),
            "cm": self.cm(hidden),
            "resectable": self.resectable(hidden),
            "neoadjuvant": self.neoadjuvant(hidden),
        }


def posterior_entropy(logits: torch.Tensor) -> torch.Tensor:
    probs = logits.softmax(dim=-1).clamp_min(1e-8)
    entropy = -(probs * probs.log()).sum(dim=-1)
    return entropy / torch.log(torch.tensor(float(logits.shape[-1]), device=logits.device))


def multitask_loss(logits: dict[str, torch.Tensor], batch: dict[str, torch.Tensor]) -> torch.Tensor:
    return sum(F.cross_entropy(logits[key], batch[key].long()) for key in logits.keys())
