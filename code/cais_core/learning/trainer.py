from __future__ import annotations

from dataclasses import dataclass

import torch
from torch.utils.data import DataLoader

from cais_core.audit.metrics import summarize_tasks
from cais_core.fusion.heads import multitask_loss
from cais_core.fusion.model import CAISNet, CAISSpec
from cais_core.ingest.synthetic import SyntheticBatchSpec, SyntheticStagingDataset, collate_staging
from cais_core.learning.config import RunConfig
from cais_core.learning.optim import WarmupCosine, build_optimizer
from cais_core.learning.seed import set_seed


@dataclass(frozen=True)
class TrainResult:
    losses: list[float]
    metrics: dict[str, float]


def build_model(config: RunConfig) -> CAISNet:
    return CAISNet(CAISSpec(config.latent_dim, config.radiomic_features, 10, config.hidden_dim, config.site_classes, config.beta))


def make_local_loader(config: RunConfig, samples: int = 64) -> DataLoader[dict[str, torch.Tensor]]:
    spec = SyntheticBatchSpec(samples, config.latent_dim, 10, config.radiomic_features, config.site_classes, config.seed)
    ds = SyntheticStagingDataset(spec)
    return DataLoader(ds, batch_size=config.batch_size, shuffle=True, collate_fn=collate_staging)


def train_local(config: RunConfig, device: torch.device | None = None) -> TrainResult:
    set_seed(config.seed)
    actual_device = device or torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = build_model(config).to(actual_device)
    loader = make_local_loader(config)
    optimizer = build_optimizer(model.parameters(), config.learning_rate, config.weight_decay)
    scheduler = WarmupCosine(optimizer, config.warmup_epochs * len(loader), config.epochs * len(loader))
    losses: list[float] = []
    last_logits: dict[str, torch.Tensor] | None = None
    last_batch: dict[str, torch.Tensor] | None = None
    for _ in range(config.epochs):
        for batch in loader:
            moved = {key: value.to(actual_device) for key, value in batch.items()}
            optimizer.zero_grad(set_to_none=True)
            logits = model(moved["latent"], moved["radiomic"], moved["clinical"])
            loss = multitask_loss(logits, moved)
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), config.gradient_clip)
            optimizer.step()
            scheduler.step()
            losses.append(float(loss.detach().cpu()))
            last_logits = {key: value.detach().cpu() for key, value in logits.items()}
            last_batch = {key: value.detach().cpu() for key, value in moved.items()}
    if last_logits is None or last_batch is None:
        return TrainResult([], {})
    return TrainResult(losses, summarize_tasks(last_logits, last_batch))
