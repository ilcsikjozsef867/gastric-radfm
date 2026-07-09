from __future__ import annotations

from dataclasses import dataclass

import torch
from torch import nn
import torch.nn.functional as F


@dataclass(frozen=True)
class BottleneckSpec:
    latent_dim: int
    hidden_dim: int
    site_classes: int
    beta: float


class ConditionalBottleneck(nn.Module):
    def __init__(self, spec: BottleneckSpec) -> None:
        super().__init__()
        self.mu = nn.Sequential(nn.LayerNorm(spec.latent_dim), nn.Linear(spec.latent_dim, spec.hidden_dim), nn.SiLU(), nn.Linear(spec.hidden_dim, spec.hidden_dim))
        self.logvar = nn.Sequential(nn.LayerNorm(spec.latent_dim), nn.Linear(spec.latent_dim, spec.hidden_dim), nn.SiLU(), nn.Linear(spec.hidden_dim, spec.hidden_dim))
        self.site = nn.Linear(spec.hidden_dim, spec.site_classes)
        self.stage = nn.Linear(spec.hidden_dim, 5)
        self.beta = spec.beta

    def encode(self, z: torch.Tensor) -> tuple[torch.Tensor, torch.Tensor]:
        return self.mu(z), self.logvar(z).clamp(-8.0, 4.0)

    def sample(self, z: torch.Tensor) -> torch.Tensor:
        mu, logvar = self.encode(z)
        eps = torch.randn_like(mu)
        return mu + eps * torch.exp(0.5 * logvar)

    def forward(self, z: torch.Tensor) -> torch.Tensor:
        mu, _ = self.encode(z)
        return mu

    def objective(self, z: torch.Tensor, site: torch.Tensor, ct: torch.Tensor) -> tuple[torch.Tensor, dict[str, torch.Tensor]]:
        f = self.sample(z)
        site_logits = self.site(f)
        stage_logits = self.stage(f)
        site_loss = F.cross_entropy(site_logits, site)
        stage_loss = F.cross_entropy(stage_logits, ct)
        loss = site_loss - self.beta * stage_loss
        estimate = residual_site_information(site_logits, site)
        return loss, {"site_loss": site_loss.detach(), "stage_loss": stage_loss.detach(), "epsilon": estimate.detach()}


def residual_site_information(site_logits: torch.Tensor, site: torch.Tensor) -> torch.Tensor:
    probs = site_logits.softmax(dim=-1)
    marginal = torch.bincount(site, minlength=site_logits.shape[-1]).float().to(site_logits.device)
    marginal = marginal / marginal.sum().clamp_min(1.0)
    gathered = probs.gather(1, site.view(-1, 1)).squeeze(1).clamp_min(1e-8)
    base = marginal.gather(0, site).clamp_min(1e-8)
    return torch.log(gathered / base).mean().clamp_min(0.0)


def transfer_gap_bound(epsilon: float, label_shift: float, slack: float, lipschitz: float = 1.0) -> float:
    return float((2.0 * max(epsilon, 0.0)) ** 0.5 + lipschitz * label_shift + slack)
