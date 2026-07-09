from __future__ import annotations

from dataclasses import dataclass

import torch


@dataclass(frozen=True)
class Interval:
    low: float
    mid: float
    high: float


def bootstrap_mean(values: torch.Tensor, rounds: int = 1000, alpha: float = 0.05, seed: int = 7) -> Interval:
    gen = torch.Generator().manual_seed(seed)
    vals = values.float().flatten()
    estimates = []
    for _ in range(rounds):
        idx = torch.randint(0, vals.numel(), (vals.numel(),), generator=gen)
        estimates.append(vals[idx].mean())
    stack = torch.stack(estimates)
    low = torch.quantile(stack, alpha / 2)
    high = torch.quantile(stack, 1 - alpha / 2)
    return Interval(float(low), float(vals.mean()), float(high))


def benjamini_hochberg(pvalues: torch.Tensor, q: float = 0.05) -> torch.Tensor:
    order = torch.argsort(pvalues)
    ranked = pvalues[order]
    m = pvalues.numel()
    thresholds = q * torch.arange(1, m + 1, device=pvalues.device).float() / float(m)
    passed = ranked <= thresholds
    keep = torch.zeros_like(pvalues, dtype=torch.bool)
    if passed.any():
        k = int(torch.nonzero(passed, as_tuple=False).max().item())
        keep[order[: k + 1]] = True
    return keep


def mcnemar_discordance(a_correct: torch.Tensor, b_correct: torch.Tensor) -> torch.Tensor:
    b01 = ((a_correct == 0) & (b_correct == 1)).sum().float()
    b10 = ((a_correct == 1) & (b_correct == 0)).sum().float()
    return (b01 - b10).abs().sub(1).clamp_min(0).pow(2) / (b01 + b10).clamp_min(1)
