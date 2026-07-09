from __future__ import annotations

import torch

from cais_core.calibration.conformal import calibrate, infer_sets
from cais_core.fusion.model import CAISNet, CAISSpec
from cais_core.ingest.synthetic import SyntheticBatchSpec, SyntheticStagingDataset
from cais_core.learning.config import load_config
from cais_core.learning.trainer import train_local
from cais_core.vision.invariance import transfer_gap_bound
from cais_core.vision.radiomics import RingSpec, perigastric_ring, radiomic_signature


def test_model_forward_shapes() -> None:
    model = CAISNet(CAISSpec(32, 107, 10, 64, 4, 0.1))
    logits = model(torch.randn(3, 32), torch.randn(3, 107), torch.randn(3, 10))
    assert logits["ct"].shape == (3, 5)
    assert logits["cn"].shape == (3, 3)
    assert logits["cm"].shape == (3, 2)


def test_conformal_sets() -> None:
    logits = {"ct": torch.randn(8, 5), "cm": torch.randn(8, 2)}
    labels = {"ct": torch.randint(0, 5, (8,)), "cm": torch.randint(0, 2, (8,))}
    book = calibrate(logits, labels, 0.1)
    sets, abstain = infer_sets({key: value[:1] for key, value in logits.items()}, book, 0.9)
    assert len(sets) == 2
    assert isinstance(abstain, bool)


def test_radiomic_signature_size() -> None:
    phases = torch.randn(3, 8, 8, 8)
    stomach = torch.zeros(8, 8, 8).bool()
    tumor = torch.zeros(8, 8, 8).bool()
    stomach[2:6, 2:6, 2:6] = True
    tumor[3:5, 3:5, 3:5] = True
    ring = perigastric_ring(stomach, tumor, RingSpec(5.0, (1.0, 1.0, 1.0)))
    sig = radiomic_signature(phases, tumor, ring)
    assert sig.shape == (107,)


def test_synthetic_dataset() -> None:
    ds = SyntheticStagingDataset(SyntheticBatchSpec(10, 32, 10, 107, 4, 7))
    assert len(ds) == 10
    assert ds[0]["latent"].shape == (32,)


def test_transfer_bound() -> None:
    assert transfer_gap_bound(0.041, 0.0, 0.0) > 0.28


def test_local_training_runs() -> None:
    config = load_config("settings/local_check.json")
    result = train_local(config, torch.device("cpu"))
    assert len(result.losses) > 0
    assert result.losses[-1] <= result.losses[0] + 2.0
