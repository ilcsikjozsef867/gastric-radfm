from __future__ import annotations

import torch
from torch import nn
import torch.nn.functional as F


class TemperatureScaler(nn.Module):
    def __init__(self, initial: float = 1.0) -> None:
        super().__init__()
        self.log_temperature = nn.Parameter(torch.log(torch.tensor(initial)))

    def forward(self, logits: torch.Tensor) -> torch.Tensor:
        return logits / self.log_temperature.exp().clamp_min(1e-4)

    def fit_step(self, logits: torch.Tensor, labels: torch.Tensor, lr: float = 0.01) -> torch.Tensor:
        opt = torch.optim.LBFGS([self.log_temperature], lr=lr, max_iter=20)
        def closure() -> torch.Tensor:
            opt.zero_grad()
            loss = F.cross_entropy(self(logits), labels)
            loss.backward()
            return loss
        return opt.step(closure)


def expected_calibration_error(logits: torch.Tensor, labels: torch.Tensor, bins: int = 15) -> torch.Tensor:
    probs = logits.softmax(dim=-1)
    conf, pred = probs.max(dim=-1)
    correct = pred.eq(labels).float()
    total = torch.zeros((), device=logits.device)
    edges = torch.linspace(0, 1, bins + 1, device=logits.device)
    for left, right in zip(edges[:-1], edges[1:]):
        mask = (conf > left) & (conf <= right)
        if mask.any():
            total = total + mask.float().mean() * (conf[mask].mean() - correct[mask].mean()).abs()
    return total
