from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping

import torch
from torch import nn


FEATURES = [
    "age",
    "sex",
    "tumor_location",
    "borrmann_type",
    "lauren_subtype",
    "biopsy_differentiation",
    "cea",
    "ca199",
    "ca724",
    "albumin",
]


@dataclass(frozen=True)
class ClinicalSpec:
    input_dim: int
    hidden_dim: int
    output_dim: int


class ClinicalVectorizer:
    def __init__(self, names: list[str] | None = None) -> None:
        self.names = names or FEATURES

    def transform_one(self, record: Mapping[str, float | int | str]) -> torch.Tensor:
        values: list[float] = []
        for name in self.names:
            raw = record.get(name, 0.0)
            if isinstance(raw, str):
                values.append(float(abs(hash(raw)) % 997) / 997.0)
            else:
                values.append(float(raw))
        return torch.tensor(values, dtype=torch.float32)

    def transform_many(self, records: list[Mapping[str, float | int | str]]) -> torch.Tensor:
        return torch.stack([self.transform_one(record) for record in records], dim=0)


class ClinicalEncoder(nn.Module):
    def __init__(self, spec: ClinicalSpec) -> None:
        super().__init__()
        self.net = nn.Sequential(
            nn.LayerNorm(spec.input_dim),
            nn.Linear(spec.input_dim, spec.hidden_dim),
            nn.SiLU(),
            nn.Dropout(0.05),
            nn.Linear(spec.hidden_dim, spec.output_dim),
            nn.SiLU(),
        )

    def forward(self, clinical: torch.Tensor) -> torch.Tensor:
        return self.net(clinical)


def impute_missing(clinical: torch.Tensor) -> torch.Tensor:
    clean = clinical.clone()
    mask = torch.isfinite(clean)
    col_mean = torch.where(mask, clean, torch.zeros_like(clean)).sum(dim=0) / mask.sum(dim=0).clamp_min(1)
    return torch.where(mask, clean, col_mean.unsqueeze(0))
