from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class RunConfig:
    seed: int
    epochs: int
    batch_size: int
    learning_rate: float
    weight_decay: float
    warmup_epochs: int
    gradient_clip: float
    precision: str
    spacing_mm: tuple[float, float, float]
    hu_window: tuple[float, float]
    ring_width_mm: float
    radiomic_features: int
    latent_dim: int
    hidden_dim: int
    site_classes: int
    beta: float
    target_epsilon: float
    gate_threshold: float
    conformal_alpha: float
    abstention_threshold: float
    seeds: list[int]
    output_dir: str


def load_config(path: str | Path) -> RunConfig:
    data = json.loads(Path(path).read_text())
    return RunConfig(
        seed=int(data["seed"]),
        epochs=int(data["epochs"]),
        batch_size=int(data["batch_size"]),
        learning_rate=float(data["learning_rate"]),
        weight_decay=float(data["weight_decay"]),
        warmup_epochs=int(data["warmup_epochs"]),
        gradient_clip=float(data["gradient_clip"]),
        precision=str(data["precision"]),
        spacing_mm=tuple(float(x) for x in data["spacing_mm"]),
        hu_window=tuple(float(x) for x in data["hu_window"]),
        ring_width_mm=float(data["ring_width_mm"]),
        radiomic_features=int(data["radiomic_features"]),
        latent_dim=int(data["latent_dim"]),
        hidden_dim=int(data["hidden_dim"]),
        site_classes=int(data["site_classes"]),
        beta=float(data["beta"]),
        target_epsilon=float(data["target_epsilon"]),
        gate_threshold=float(data["gate_threshold"]),
        conformal_alpha=float(data["conformal_alpha"]),
        abstention_threshold=float(data["abstention_threshold"]),
        seeds=[int(x) for x in data["seeds"]],
        output_dir=str(data["output_dir"]),
    )
