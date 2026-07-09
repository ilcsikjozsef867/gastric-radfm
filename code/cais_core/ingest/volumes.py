from __future__ import annotations

from dataclasses import dataclass

import torch
import torch.nn.functional as F


@dataclass(frozen=True)
class VolumeWindow:
    low: float
    high: float


@dataclass(frozen=True)
class Spacing:
    z: float
    y: float
    x: float


def clip_hu(volume: torch.Tensor, window: VolumeWindow) -> torch.Tensor:
    return volume.clamp(min=window.low, max=window.high)


def zscore(volume: torch.Tensor, mask: torch.Tensor | None = None) -> torch.Tensor:
    data = volume if mask is None else volume[mask > 0]
    mean = data.mean()
    std = data.std().clamp_min(1e-6)
    return (volume - mean) / std


def resize_volume(volume: torch.Tensor, shape: tuple[int, int, int]) -> torch.Tensor:
    tensor = volume.unsqueeze(0).unsqueeze(0).float()
    out = F.interpolate(tensor, size=shape, mode="trilinear", align_corners=False)
    return out.squeeze(0).squeeze(0)


def normalize_phases(phases: torch.Tensor, low: float = -125.0, high: float = 225.0) -> torch.Tensor:
    clean = []
    for phase in phases:
        clean.append(zscore(clip_hu(phase, VolumeWindow(low, high))))
    return torch.stack(clean, dim=0)


def masked_mean(volume: torch.Tensor, mask: torch.Tensor) -> torch.Tensor:
    weights = mask.float()
    denom = weights.sum().clamp_min(1.0)
    return (volume * weights).sum() / denom


def masked_std(volume: torch.Tensor, mask: torch.Tensor) -> torch.Tensor:
    mean = masked_mean(volume, mask)
    weights = mask.float()
    denom = weights.sum().clamp_min(1.0)
    var = ((volume - mean).pow(2) * weights).sum() / denom
    return var.sqrt()
