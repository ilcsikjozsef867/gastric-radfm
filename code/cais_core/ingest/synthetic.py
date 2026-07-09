from __future__ import annotations

from dataclasses import dataclass

import torch
from torch.utils.data import Dataset


@dataclass(frozen=True)
class SyntheticBatchSpec:
    samples: int
    latent_dim: int
    clinical_dim: int
    radiomic_dim: int
    site_classes: int
    seed: int


class SyntheticStagingDataset(Dataset[dict[str, torch.Tensor]]):
    def __init__(self, spec: SyntheticBatchSpec) -> None:
        gen = torch.Generator().manual_seed(spec.seed)
        latent = torch.randn(spec.samples, spec.latent_dim, generator=gen)
        clinical = torch.randn(spec.samples, spec.clinical_dim, generator=gen)
        radiomic = torch.randn(spec.samples, spec.radiomic_dim, generator=gen)
        site = torch.randint(0, spec.site_classes, (spec.samples,), generator=gen)
        marker = latent[:, 0] + 0.4 * clinical[:, 0] + 0.2 * radiomic[:, 0]
        ct = torch.bucketize(marker, torch.tensor([-1.0, -0.25, 0.35, 1.05]))
        cn = torch.bucketize(latent[:, 1] + radiomic[:, 1], torch.tensor([-0.2, 0.75]))
        cm = (latent[:, 2] + clinical[:, 1] > 0).long()
        res = (latent[:, 3] - radiomic[:, 2] > -0.1).long()
        neo = ((ct >= 2) | (cn >= 1) | (cm > 0)).long()
        self.items = {
            "latent": latent,
            "clinical": clinical,
            "radiomic": radiomic,
            "site": site,
            "ct": ct,
            "cn": cn,
            "cm": cm,
            "resectable": res,
            "neoadjuvant": neo,
        }

    def __len__(self) -> int:
        return int(self.items["latent"].shape[0])

    def __getitem__(self, index: int) -> dict[str, torch.Tensor]:
        return {key: value[index] for key, value in self.items.items()}


def collate_staging(batch: list[dict[str, torch.Tensor]]) -> dict[str, torch.Tensor]:
    keys = batch[0].keys()
    return {key: torch.stack([item[key] for item in batch], dim=0) for key in keys}
