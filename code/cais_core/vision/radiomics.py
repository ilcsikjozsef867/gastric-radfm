from __future__ import annotations

from dataclasses import dataclass

import torch
import torch.nn.functional as F

from cais_core.ingest.volumes import masked_mean, masked_std


@dataclass(frozen=True)
class RingSpec:
    width_mm: float
    spacing_mm: tuple[float, float, float]
    target_features: int = 107


def binary_dilate(mask: torch.Tensor, steps: int) -> torch.Tensor:
    x = mask.float().unsqueeze(0).unsqueeze(0)
    for _ in range(max(steps, 0)):
        x = F.max_pool3d(x, kernel_size=3, stride=1, padding=1)
    return x.squeeze(0).squeeze(0) > 0.5


def perigastric_ring(stomach_mask: torch.Tensor, tumor_mask: torch.Tensor, spec: RingSpec) -> torch.Tensor:
    voxels = max(1, int(round(spec.width_mm / min(spec.spacing_mm))))
    outer = binary_dilate(stomach_mask > 0, voxels)
    inner = stomach_mask > 0
    tumor = binary_dilate(tumor_mask > 0, 1)
    return outer & ~inner & ~tumor


def histogram_features(values: torch.Tensor, bins: int) -> torch.Tensor:
    if values.numel() == 0:
        return torch.zeros(bins)
    lo = values.min()
    hi = values.max()
    if torch.isclose(lo, hi):
        out = torch.zeros(bins)
        out[0] = 1.0
        return out
    hist = torch.histc(values.float(), bins=bins, min=float(lo), max=float(hi))
    return hist / hist.sum().clamp_min(1.0)


def phase_features(volume: torch.Tensor, mask: torch.Tensor) -> torch.Tensor:
    values = volume[mask > 0]
    if values.numel() == 0:
        return torch.zeros(24)
    quantiles = torch.quantile(values.float(), torch.tensor([0.05, 0.1, 0.25, 0.5, 0.75, 0.9, 0.95]))
    centered = values.float() - values.float().mean()
    skew = centered.pow(3).mean() / centered.pow(2).mean().sqrt().clamp_min(1e-6).pow(3)
    stats = torch.stack([
        masked_mean(volume, mask),
        masked_std(volume, mask),
        values.min(),
        values.max(),
        skew if values.numel() > 2 else torch.tensor(0.0),
    ])
    hist = histogram_features(values, 12)
    energy = torch.stack([(values.float().pow(2).mean()), values.float().abs().mean()])
    return torch.cat([stats.float(), quantiles.float(), hist.float(), energy.float()], dim=0)


def pairwise_phase_deltas(features: list[torch.Tensor]) -> torch.Tensor:
    deltas = []
    for left, right in [(0, 1), (1, 2), (0, 2)]:
        deltas.append(features[right] - features[left])
    return torch.cat(deltas, dim=0)


def radiomic_signature(phases: torch.Tensor, tumor_mask: torch.Tensor, ring_mask: torch.Tensor, target: int = 107) -> torch.Tensor:
    tumor_parts = [phase_features(phase, tumor_mask) for phase in phases]
    ring_parts = [phase_features(phase, ring_mask) for phase in phases]
    merged = torch.cat(tumor_parts + ring_parts + [pairwise_phase_deltas(ring_parts)], dim=0)
    if merged.numel() >= target:
        return merged[:target]
    pad = torch.zeros(target - merged.numel(), dtype=merged.dtype)
    return torch.cat([merged, pad], dim=0)


class RadiomicNormalizer:
    def __init__(self) -> None:
        self.mean: torch.Tensor | None = None
        self.std: torch.Tensor | None = None

    def fit(self, features: torch.Tensor) -> None:
        self.mean = features.mean(dim=0)
        self.std = features.std(dim=0).clamp_min(1e-6)

    def transform(self, features: torch.Tensor) -> torch.Tensor:
        if self.mean is None or self.std is None:
            raise RuntimeError("normalizer is not fitted")
        return (features - self.mean.to(features.device)) / self.std.to(features.device)

    def fit_transform(self, features: torch.Tensor) -> torch.Tensor:
        self.fit(features)
        return self.transform(features)
