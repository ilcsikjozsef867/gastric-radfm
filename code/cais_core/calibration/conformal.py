from __future__ import annotations

from dataclasses import dataclass

import torch


@dataclass(frozen=True)
class ConformalSet:
    task: str
    labels: list[int]
    confidence: float


@dataclass(frozen=True)
class QuantileBook:
    values: dict[str, float]
    alpha: float


def nonconformity(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    probs = logits.softmax(dim=-1)
    return 1.0 - probs.gather(1, labels.view(-1, 1)).squeeze(1)


def weighted_quantile(scores: torch.Tensor, weights: torch.Tensor, q: float) -> torch.Tensor:
    order = torch.argsort(scores)
    scores_sorted = scores[order]
    weights_sorted = weights[order].clamp_min(0)
    cdf = weights_sorted.cumsum(0) / weights_sorted.sum().clamp_min(1e-8)
    idx = torch.searchsorted(cdf, torch.tensor(q, device=scores.device)).clamp(max=scores.numel() - 1)
    return scores_sorted[idx]


def calibrate(logits: dict[str, torch.Tensor], labels: dict[str, torch.Tensor], alpha: float, weights: torch.Tensor | None = None) -> QuantileBook:
    values: dict[str, float] = {}
    for key, value in logits.items():
        scores = nonconformity(value, labels[key])
        w = torch.ones_like(scores) if weights is None else weights.to(scores.device)
        values[key] = float(weighted_quantile(scores, w, 1.0 - alpha).detach().cpu())
    return QuantileBook(values=values, alpha=alpha)


def prediction_set(logits: torch.Tensor, threshold: float) -> tuple[list[int], float]:
    probs = logits.softmax(dim=-1).flatten()
    scores = 1.0 - probs
    labels = torch.nonzero(scores <= threshold, as_tuple=False).flatten().tolist()
    if not labels:
        labels = [int(torch.argmax(probs).item())]
    confidence = float(probs.max().detach().cpu())
    return [int(x) for x in labels], confidence


def infer_sets(logits: dict[str, torch.Tensor], book: QuantileBook, abstention_threshold: float) -> tuple[list[ConformalSet], bool]:
    sets: list[ConformalSet] = []
    abstain = False
    for key, value in logits.items():
        labels, confidence = prediction_set(value, book.values[key])
        sets.append(ConformalSet(key, labels, confidence))
        if len(labels) > 1 and confidence < abstention_threshold:
            abstain = True
    return sets, abstain
