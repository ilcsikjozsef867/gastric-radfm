from __future__ import annotations

from dataclasses import dataclass

import torch


@dataclass(frozen=True)
class BinaryStats:
    sensitivity: float
    specificity: float
    precision: float
    f1: float


def accuracy(logits: torch.Tensor, labels: torch.Tensor) -> float:
    return float(logits.argmax(dim=-1).eq(labels).float().mean().detach().cpu())


def confusion_matrix(pred: torch.Tensor, labels: torch.Tensor, classes: int) -> torch.Tensor:
    out = torch.zeros(classes, classes, dtype=torch.long)
    for p, y in zip(pred.flatten().cpu(), labels.flatten().cpu()):
        out[int(y), int(p)] += 1
    return out


def binary_stats(logits: torch.Tensor, labels: torch.Tensor) -> BinaryStats:
    pred = logits.argmax(dim=-1)
    tp = ((pred == 1) & (labels == 1)).sum().float()
    tn = ((pred == 0) & (labels == 0)).sum().float()
    fp = ((pred == 1) & (labels == 0)).sum().float()
    fn = ((pred == 0) & (labels == 1)).sum().float()
    sensitivity = tp / (tp + fn).clamp_min(1)
    specificity = tn / (tn + fp).clamp_min(1)
    precision = tp / (tp + fp).clamp_min(1)
    f1 = 2 * precision * sensitivity / (precision + sensitivity).clamp_min(1e-8)
    return BinaryStats(float(sensitivity), float(specificity), float(precision), float(f1))


def auroc(scores: torch.Tensor, labels: torch.Tensor) -> float:
    order = torch.argsort(scores)
    ranks = torch.empty_like(order, dtype=torch.float32)
    ranks[order] = torch.arange(1, scores.numel() + 1, device=scores.device).float()
    pos = labels == 1
    n_pos = pos.sum().float()
    n_neg = (~pos).sum().float()
    if n_pos == 0 or n_neg == 0:
        return 0.5
    value = (ranks[pos].sum() - n_pos * (n_pos + 1) / 2) / (n_pos * n_neg)
    return float(value.detach().cpu())


def summarize_tasks(logits: dict[str, torch.Tensor], batch: dict[str, torch.Tensor]) -> dict[str, float]:
    out: dict[str, float] = {}
    for key in ["ct", "cn", "cm", "resectable", "neoadjuvant"]:
        out[f"{key}_accuracy"] = accuracy(logits[key], batch[key].long())
    out["cm_auroc"] = auroc(logits["cm"].softmax(-1)[:, 1], batch["cm"].long())
    out["resectable_auroc"] = auroc(logits["resectable"].softmax(-1)[:, 1], batch["resectable"].long())
    return out
