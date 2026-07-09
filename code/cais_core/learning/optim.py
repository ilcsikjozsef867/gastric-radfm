from __future__ import annotations

import math

import torch
from torch.optim import Optimizer


def build_optimizer(params: object, lr: float, weight_decay: float) -> Optimizer:
    return torch.optim.AdamW(params, lr=lr, weight_decay=weight_decay)


class WarmupCosine:
    def __init__(self, optimizer: Optimizer, warmup: int, total: int, min_factor: float = 0.05) -> None:
        self.optimizer = optimizer
        self.warmup = max(warmup, 1)
        self.total = max(total, self.warmup + 1)
        self.min_factor = min_factor
        self.step_count = 0
        self.base = [group["lr"] for group in optimizer.param_groups]

    def step(self) -> None:
        self.step_count += 1
        if self.step_count <= self.warmup:
            factor = self.step_count / self.warmup
        else:
            progress = (self.step_count - self.warmup) / (self.total - self.warmup)
            factor = self.min_factor + (1 - self.min_factor) * 0.5 * (1 + math.cos(math.pi * progress))
        for lr, group in zip(self.base, self.optimizer.param_groups):
            group["lr"] = lr * factor
