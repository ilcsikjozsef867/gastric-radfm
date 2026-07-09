from __future__ import annotations

from dataclasses import dataclass

import torch
from torch import nn


@dataclass(frozen=True)
class EncoderSpec:
    input_channels: int
    latent_dim: int
    width: int


class PhaseStem(nn.Module):
    def __init__(self, spec: EncoderSpec) -> None:
        super().__init__()
        self.net = nn.Sequential(
            nn.Conv3d(spec.input_channels, spec.width, 3, padding=1),
            nn.GroupNorm(4, spec.width),
            nn.SiLU(),
            nn.Conv3d(spec.width, spec.width, 3, stride=2, padding=1),
            nn.GroupNorm(4, spec.width),
            nn.SiLU(),
            nn.AdaptiveAvgPool3d(1),
        )
        self.proj = nn.Linear(spec.width, spec.latent_dim)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        y = self.net(x).flatten(1)
        return self.proj(y)


class FrozenLatentProjector(nn.Module):
    def __init__(self, latent_dim: int, output_dim: int) -> None:
        super().__init__()
        self.proj = nn.Sequential(nn.LayerNorm(latent_dim), nn.Linear(latent_dim, output_dim), nn.SiLU())
        for param in self.parameters():
            param.requires_grad = False

    def forward(self, latent: torch.Tensor) -> torch.Tensor:
        return self.proj(latent)


def cache_latents(encoder: nn.Module, loader: object, device: torch.device) -> list[torch.Tensor]:
    encoder.eval()
    latents: list[torch.Tensor] = []
    with torch.no_grad():
        for batch in loader:
            x = batch["image"].to(device)
            latents.append(encoder(x).cpu())
    return latents
