from __future__ import annotations

import os
from pathlib import Path
from typing import Any

import torch
from torch import nn
from torch.optim import Optimizer


def save_state(path: str | Path, model: nn.Module, optimizer: Optimizer, seed: int, extra: dict[str, Any] | None = None) -> None:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    tmp = target.with_suffix(target.suffix + ".tmp")
    payload = {"model": model.state_dict(), "optimizer": optimizer.state_dict(), "seed": seed, "extra": extra or {}}
    torch.save(payload, tmp)
    os.replace(tmp, target)


def load_state(path: str | Path, model: nn.Module, optimizer: Optimizer | None = None) -> dict[str, Any]:
    payload = torch.load(path, map_location="cpu")
    model.load_state_dict(payload["model"])
    if optimizer is not None:
        optimizer.load_state_dict(payload["optimizer"])
    return dict(payload)
