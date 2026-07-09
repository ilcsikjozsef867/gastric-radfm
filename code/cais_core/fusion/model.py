from __future__ import annotations

from dataclasses import dataclass

import torch
from torch import nn

from cais_core.fusion.heads import DecisionFusion, FusionSpec, MultiTaskHead, posterior_entropy
from cais_core.vision.invariance import BottleneckSpec, ConditionalBottleneck


@dataclass(frozen=True)
class CAISSpec:
    latent_dim: int
    radiomic_dim: int
    clinical_dim: int
    hidden_dim: int
    site_classes: int
    beta: float


class CAISNet(nn.Module):
    def __init__(self, spec: CAISSpec) -> None:
        super().__init__()
        self.adapter = ConditionalBottleneck(BottleneckSpec(spec.latent_dim, spec.hidden_dim, spec.site_classes, spec.beta))
        self.imaging_probe = nn.Linear(spec.hidden_dim, 5)
        self.fusion = DecisionFusion(FusionSpec(spec.hidden_dim, spec.radiomic_dim, spec.clinical_dim, spec.hidden_dim))
        self.head = MultiTaskHead(spec.hidden_dim)

    def forward(self, latent: torch.Tensor, radiomic: torch.Tensor, clinical: torch.Tensor) -> dict[str, torch.Tensor]:
        image = self.adapter(latent)
        entropy = posterior_entropy(self.imaging_probe(image))
        hidden = self.fusion(image, radiomic, clinical, entropy)
        return self.head(hidden)

    def hidden(self, latent: torch.Tensor, radiomic: torch.Tensor, clinical: torch.Tensor) -> torch.Tensor:
        image = self.adapter(latent)
        entropy = posterior_entropy(self.imaging_probe(image))
        return self.fusion(image, radiomic, clinical, entropy)
