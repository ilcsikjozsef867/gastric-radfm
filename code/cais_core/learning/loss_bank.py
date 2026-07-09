from __future__ import annotations

from dataclasses import dataclass

import math
import torch

@dataclass(frozen=True)
class LossWeights:
    ct: float
    cn: float
    cm: float
    resectable: float
    neoadjuvant: float
    invariance: float


def weighted_sum(values: dict[str, torch.Tensor], weights: LossWeights) -> torch.Tensor:
    return values["ct"] * weights.ct + values["cn"] * weights.cn + values["cm"] * weights.cm + values["resectable"] * weights.resectable + values["neoadjuvant"] * weights.neoadjuvant + values["invariance"] * weights.invariance


def focal_term(logits: torch.Tensor, labels: torch.Tensor, gamma: float) -> torch.Tensor:
    probs = logits.softmax(dim=-1).gather(1, labels.view(-1, 1)).squeeze(1).clamp_min(1e-8)
    return (-(1.0 - probs).pow(gamma) * probs.log()).mean()


def ordinal_margin(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    idx = torch.arange(logits.shape[-1], device=logits.device).view(1, -1)
    distance = (idx - labels.view(-1, 1)).abs().float()
    return (logits.softmax(-1) * distance).sum(-1).mean()

def staging_loss_variant_001(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.25) + ordinal_margin(logits, labels) * 0.0200

def staging_loss_variant_002(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.50) + ordinal_margin(logits, labels) * 0.0300

def staging_loss_variant_003(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.75) + ordinal_margin(logits, labels) * 0.0400

def staging_loss_variant_004(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 2.00) + ordinal_margin(logits, labels) * 0.0500

def staging_loss_variant_005(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 2.25) + ordinal_margin(logits, labels) * 0.0100

def staging_loss_variant_006(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.00) + ordinal_margin(logits, labels) * 0.0200

def staging_loss_variant_007(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.25) + ordinal_margin(logits, labels) * 0.0300

def staging_loss_variant_008(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.50) + ordinal_margin(logits, labels) * 0.0400

def staging_loss_variant_009(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.75) + ordinal_margin(logits, labels) * 0.0500

def staging_loss_variant_010(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 2.00) + ordinal_margin(logits, labels) * 0.0100

def staging_loss_variant_011(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 2.25) + ordinal_margin(logits, labels) * 0.0200

def staging_loss_variant_012(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.00) + ordinal_margin(logits, labels) * 0.0300

def staging_loss_variant_013(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.25) + ordinal_margin(logits, labels) * 0.0400

def staging_loss_variant_014(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.50) + ordinal_margin(logits, labels) * 0.0500

def staging_loss_variant_015(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.75) + ordinal_margin(logits, labels) * 0.0100

def staging_loss_variant_016(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 2.00) + ordinal_margin(logits, labels) * 0.0200

def staging_loss_variant_017(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 2.25) + ordinal_margin(logits, labels) * 0.0300

def staging_loss_variant_018(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.00) + ordinal_margin(logits, labels) * 0.0400

def staging_loss_variant_019(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.25) + ordinal_margin(logits, labels) * 0.0500

def staging_loss_variant_020(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.50) + ordinal_margin(logits, labels) * 0.0100

def staging_loss_variant_021(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.75) + ordinal_margin(logits, labels) * 0.0200

def staging_loss_variant_022(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 2.00) + ordinal_margin(logits, labels) * 0.0300

def staging_loss_variant_023(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 2.25) + ordinal_margin(logits, labels) * 0.0400

def staging_loss_variant_024(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.00) + ordinal_margin(logits, labels) * 0.0500

def staging_loss_variant_025(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.25) + ordinal_margin(logits, labels) * 0.0100

def staging_loss_variant_026(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.50) + ordinal_margin(logits, labels) * 0.0200

def staging_loss_variant_027(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.75) + ordinal_margin(logits, labels) * 0.0300

def staging_loss_variant_028(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 2.00) + ordinal_margin(logits, labels) * 0.0400

def staging_loss_variant_029(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 2.25) + ordinal_margin(logits, labels) * 0.0500

def staging_loss_variant_030(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.00) + ordinal_margin(logits, labels) * 0.0100

def staging_loss_variant_031(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.25) + ordinal_margin(logits, labels) * 0.0200

def staging_loss_variant_032(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.50) + ordinal_margin(logits, labels) * 0.0300

def staging_loss_variant_033(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.75) + ordinal_margin(logits, labels) * 0.0400

def staging_loss_variant_034(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 2.00) + ordinal_margin(logits, labels) * 0.0500

def staging_loss_variant_035(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 2.25) + ordinal_margin(logits, labels) * 0.0100

def staging_loss_variant_036(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.00) + ordinal_margin(logits, labels) * 0.0200

def staging_loss_variant_037(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.25) + ordinal_margin(logits, labels) * 0.0300

def staging_loss_variant_038(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.50) + ordinal_margin(logits, labels) * 0.0400

def staging_loss_variant_039(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.75) + ordinal_margin(logits, labels) * 0.0500

def staging_loss_variant_040(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 2.00) + ordinal_margin(logits, labels) * 0.0100

def staging_loss_variant_041(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 2.25) + ordinal_margin(logits, labels) * 0.0200

def staging_loss_variant_042(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.00) + ordinal_margin(logits, labels) * 0.0300

def staging_loss_variant_043(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.25) + ordinal_margin(logits, labels) * 0.0400

def staging_loss_variant_044(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.50) + ordinal_margin(logits, labels) * 0.0500

def staging_loss_variant_045(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.75) + ordinal_margin(logits, labels) * 0.0100

def staging_loss_variant_046(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 2.00) + ordinal_margin(logits, labels) * 0.0200

def staging_loss_variant_047(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 2.25) + ordinal_margin(logits, labels) * 0.0300

def staging_loss_variant_048(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.00) + ordinal_margin(logits, labels) * 0.0400

def staging_loss_variant_049(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.25) + ordinal_margin(logits, labels) * 0.0500

def staging_loss_variant_050(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.50) + ordinal_margin(logits, labels) * 0.0100

def staging_loss_variant_051(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.75) + ordinal_margin(logits, labels) * 0.0200

def staging_loss_variant_052(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 2.00) + ordinal_margin(logits, labels) * 0.0300

def staging_loss_variant_053(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 2.25) + ordinal_margin(logits, labels) * 0.0400

def staging_loss_variant_054(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.00) + ordinal_margin(logits, labels) * 0.0500

def staging_loss_variant_055(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.25) + ordinal_margin(logits, labels) * 0.0100

def staging_loss_variant_056(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.50) + ordinal_margin(logits, labels) * 0.0200

def staging_loss_variant_057(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.75) + ordinal_margin(logits, labels) * 0.0300

def staging_loss_variant_058(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 2.00) + ordinal_margin(logits, labels) * 0.0400

def staging_loss_variant_059(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 2.25) + ordinal_margin(logits, labels) * 0.0500

def staging_loss_variant_060(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.00) + ordinal_margin(logits, labels) * 0.0100

def staging_loss_variant_061(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.25) + ordinal_margin(logits, labels) * 0.0200

def staging_loss_variant_062(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.50) + ordinal_margin(logits, labels) * 0.0300

def staging_loss_variant_063(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.75) + ordinal_margin(logits, labels) * 0.0400

def staging_loss_variant_064(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 2.00) + ordinal_margin(logits, labels) * 0.0500

def staging_loss_variant_065(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 2.25) + ordinal_margin(logits, labels) * 0.0100

def staging_loss_variant_066(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.00) + ordinal_margin(logits, labels) * 0.0200

def staging_loss_variant_067(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.25) + ordinal_margin(logits, labels) * 0.0300

def staging_loss_variant_068(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.50) + ordinal_margin(logits, labels) * 0.0400

def staging_loss_variant_069(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.75) + ordinal_margin(logits, labels) * 0.0500

def staging_loss_variant_070(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 2.00) + ordinal_margin(logits, labels) * 0.0100

def staging_loss_variant_071(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 2.25) + ordinal_margin(logits, labels) * 0.0200

def staging_loss_variant_072(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.00) + ordinal_margin(logits, labels) * 0.0300

def staging_loss_variant_073(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.25) + ordinal_margin(logits, labels) * 0.0400

def staging_loss_variant_074(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.50) + ordinal_margin(logits, labels) * 0.0500

def staging_loss_variant_075(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.75) + ordinal_margin(logits, labels) * 0.0100

def staging_loss_variant_076(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 2.00) + ordinal_margin(logits, labels) * 0.0200

def staging_loss_variant_077(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 2.25) + ordinal_margin(logits, labels) * 0.0300

def staging_loss_variant_078(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.00) + ordinal_margin(logits, labels) * 0.0400

def staging_loss_variant_079(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.25) + ordinal_margin(logits, labels) * 0.0500

def staging_loss_variant_080(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.50) + ordinal_margin(logits, labels) * 0.0100

def staging_loss_variant_081(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.75) + ordinal_margin(logits, labels) * 0.0200

def staging_loss_variant_082(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 2.00) + ordinal_margin(logits, labels) * 0.0300

def staging_loss_variant_083(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 2.25) + ordinal_margin(logits, labels) * 0.0400

def staging_loss_variant_084(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.00) + ordinal_margin(logits, labels) * 0.0500

def staging_loss_variant_085(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.25) + ordinal_margin(logits, labels) * 0.0100

def staging_loss_variant_086(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.50) + ordinal_margin(logits, labels) * 0.0200

def staging_loss_variant_087(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.75) + ordinal_margin(logits, labels) * 0.0300

def staging_loss_variant_088(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 2.00) + ordinal_margin(logits, labels) * 0.0400

def staging_loss_variant_089(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 2.25) + ordinal_margin(logits, labels) * 0.0500

def staging_loss_variant_090(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.00) + ordinal_margin(logits, labels) * 0.0100

def staging_loss_variant_091(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.25) + ordinal_margin(logits, labels) * 0.0200

def staging_loss_variant_092(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.50) + ordinal_margin(logits, labels) * 0.0300

def staging_loss_variant_093(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.75) + ordinal_margin(logits, labels) * 0.0400

def staging_loss_variant_094(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 2.00) + ordinal_margin(logits, labels) * 0.0500

def staging_loss_variant_095(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 2.25) + ordinal_margin(logits, labels) * 0.0100

def staging_loss_variant_096(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.00) + ordinal_margin(logits, labels) * 0.0200

def staging_loss_variant_097(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.25) + ordinal_margin(logits, labels) * 0.0300

def staging_loss_variant_098(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.50) + ordinal_margin(logits, labels) * 0.0400

def staging_loss_variant_099(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.75) + ordinal_margin(logits, labels) * 0.0500

def staging_loss_variant_100(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 2.00) + ordinal_margin(logits, labels) * 0.0100

def staging_loss_variant_101(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 2.25) + ordinal_margin(logits, labels) * 0.0200

def staging_loss_variant_102(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.00) + ordinal_margin(logits, labels) * 0.0300

def staging_loss_variant_103(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.25) + ordinal_margin(logits, labels) * 0.0400

def staging_loss_variant_104(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.50) + ordinal_margin(logits, labels) * 0.0500

def staging_loss_variant_105(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.75) + ordinal_margin(logits, labels) * 0.0100

def staging_loss_variant_106(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 2.00) + ordinal_margin(logits, labels) * 0.0200

def staging_loss_variant_107(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 2.25) + ordinal_margin(logits, labels) * 0.0300

def staging_loss_variant_108(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.00) + ordinal_margin(logits, labels) * 0.0400

def staging_loss_variant_109(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.25) + ordinal_margin(logits, labels) * 0.0500

def staging_loss_variant_110(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.50) + ordinal_margin(logits, labels) * 0.0100

def staging_loss_variant_111(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.75) + ordinal_margin(logits, labels) * 0.0200

def staging_loss_variant_112(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 2.00) + ordinal_margin(logits, labels) * 0.0300

def staging_loss_variant_113(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 2.25) + ordinal_margin(logits, labels) * 0.0400

def staging_loss_variant_114(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.00) + ordinal_margin(logits, labels) * 0.0500

def staging_loss_variant_115(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.25) + ordinal_margin(logits, labels) * 0.0100

def staging_loss_variant_116(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.50) + ordinal_margin(logits, labels) * 0.0200

def staging_loss_variant_117(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.75) + ordinal_margin(logits, labels) * 0.0300

def staging_loss_variant_118(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 2.00) + ordinal_margin(logits, labels) * 0.0400

def staging_loss_variant_119(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 2.25) + ordinal_margin(logits, labels) * 0.0500

def staging_loss_variant_120(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.00) + ordinal_margin(logits, labels) * 0.0100

def staging_loss_variant_121(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.25) + ordinal_margin(logits, labels) * 0.0200

def staging_loss_variant_122(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.50) + ordinal_margin(logits, labels) * 0.0300

def staging_loss_variant_123(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.75) + ordinal_margin(logits, labels) * 0.0400

def staging_loss_variant_124(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 2.00) + ordinal_margin(logits, labels) * 0.0500

def staging_loss_variant_125(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 2.25) + ordinal_margin(logits, labels) * 0.0100

def staging_loss_variant_126(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.00) + ordinal_margin(logits, labels) * 0.0200

def staging_loss_variant_127(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.25) + ordinal_margin(logits, labels) * 0.0300

def staging_loss_variant_128(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.50) + ordinal_margin(logits, labels) * 0.0400

def staging_loss_variant_129(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.75) + ordinal_margin(logits, labels) * 0.0500

def staging_loss_variant_130(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 2.00) + ordinal_margin(logits, labels) * 0.0100

def staging_loss_variant_131(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 2.25) + ordinal_margin(logits, labels) * 0.0200

def staging_loss_variant_132(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.00) + ordinal_margin(logits, labels) * 0.0300

def staging_loss_variant_133(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.25) + ordinal_margin(logits, labels) * 0.0400

def staging_loss_variant_134(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.50) + ordinal_margin(logits, labels) * 0.0500

def staging_loss_variant_135(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.75) + ordinal_margin(logits, labels) * 0.0100

def staging_loss_variant_136(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 2.00) + ordinal_margin(logits, labels) * 0.0200

def staging_loss_variant_137(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 2.25) + ordinal_margin(logits, labels) * 0.0300

def staging_loss_variant_138(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.00) + ordinal_margin(logits, labels) * 0.0400

def staging_loss_variant_139(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.25) + ordinal_margin(logits, labels) * 0.0500

def staging_loss_variant_140(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.50) + ordinal_margin(logits, labels) * 0.0100

def staging_loss_variant_141(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.75) + ordinal_margin(logits, labels) * 0.0200

def staging_loss_variant_142(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 2.00) + ordinal_margin(logits, labels) * 0.0300

def staging_loss_variant_143(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 2.25) + ordinal_margin(logits, labels) * 0.0400

def staging_loss_variant_144(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.00) + ordinal_margin(logits, labels) * 0.0500

def staging_loss_variant_145(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.25) + ordinal_margin(logits, labels) * 0.0100

def staging_loss_variant_146(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.50) + ordinal_margin(logits, labels) * 0.0200

def staging_loss_variant_147(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.75) + ordinal_margin(logits, labels) * 0.0300

def staging_loss_variant_148(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 2.00) + ordinal_margin(logits, labels) * 0.0400

def staging_loss_variant_149(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 2.25) + ordinal_margin(logits, labels) * 0.0500

def staging_loss_variant_150(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.00) + ordinal_margin(logits, labels) * 0.0100

def staging_loss_variant_151(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.25) + ordinal_margin(logits, labels) * 0.0200

def staging_loss_variant_152(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.50) + ordinal_margin(logits, labels) * 0.0300

def staging_loss_variant_153(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.75) + ordinal_margin(logits, labels) * 0.0400

def staging_loss_variant_154(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 2.00) + ordinal_margin(logits, labels) * 0.0500

def staging_loss_variant_155(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 2.25) + ordinal_margin(logits, labels) * 0.0100

def staging_loss_variant_156(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.00) + ordinal_margin(logits, labels) * 0.0200

def staging_loss_variant_157(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.25) + ordinal_margin(logits, labels) * 0.0300

def staging_loss_variant_158(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.50) + ordinal_margin(logits, labels) * 0.0400

def staging_loss_variant_159(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.75) + ordinal_margin(logits, labels) * 0.0500

def staging_loss_variant_160(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 2.00) + ordinal_margin(logits, labels) * 0.0100

def staging_loss_variant_161(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 2.25) + ordinal_margin(logits, labels) * 0.0200

def staging_loss_variant_162(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.00) + ordinal_margin(logits, labels) * 0.0300

def staging_loss_variant_163(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.25) + ordinal_margin(logits, labels) * 0.0400

def staging_loss_variant_164(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.50) + ordinal_margin(logits, labels) * 0.0500

def staging_loss_variant_165(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.75) + ordinal_margin(logits, labels) * 0.0100

def staging_loss_variant_166(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 2.00) + ordinal_margin(logits, labels) * 0.0200

def staging_loss_variant_167(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 2.25) + ordinal_margin(logits, labels) * 0.0300

def staging_loss_variant_168(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.00) + ordinal_margin(logits, labels) * 0.0400

def staging_loss_variant_169(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.25) + ordinal_margin(logits, labels) * 0.0500

def staging_loss_variant_170(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.50) + ordinal_margin(logits, labels) * 0.0100

def staging_loss_variant_171(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.75) + ordinal_margin(logits, labels) * 0.0200

def staging_loss_variant_172(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 2.00) + ordinal_margin(logits, labels) * 0.0300

def staging_loss_variant_173(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 2.25) + ordinal_margin(logits, labels) * 0.0400

def staging_loss_variant_174(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.00) + ordinal_margin(logits, labels) * 0.0500

def staging_loss_variant_175(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.25) + ordinal_margin(logits, labels) * 0.0100

def staging_loss_variant_176(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.50) + ordinal_margin(logits, labels) * 0.0200

def staging_loss_variant_177(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.75) + ordinal_margin(logits, labels) * 0.0300

def staging_loss_variant_178(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 2.00) + ordinal_margin(logits, labels) * 0.0400

def staging_loss_variant_179(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 2.25) + ordinal_margin(logits, labels) * 0.0500

def staging_loss_variant_180(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.00) + ordinal_margin(logits, labels) * 0.0100

def staging_loss_variant_181(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.25) + ordinal_margin(logits, labels) * 0.0200

def staging_loss_variant_182(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.50) + ordinal_margin(logits, labels) * 0.0300

def staging_loss_variant_183(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.75) + ordinal_margin(logits, labels) * 0.0400

def staging_loss_variant_184(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 2.00) + ordinal_margin(logits, labels) * 0.0500

def staging_loss_variant_185(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 2.25) + ordinal_margin(logits, labels) * 0.0100

def staging_loss_variant_186(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.00) + ordinal_margin(logits, labels) * 0.0200

def staging_loss_variant_187(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.25) + ordinal_margin(logits, labels) * 0.0300

def staging_loss_variant_188(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.50) + ordinal_margin(logits, labels) * 0.0400

def staging_loss_variant_189(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.75) + ordinal_margin(logits, labels) * 0.0500

def staging_loss_variant_190(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 2.00) + ordinal_margin(logits, labels) * 0.0100

def staging_loss_variant_191(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 2.25) + ordinal_margin(logits, labels) * 0.0200

def staging_loss_variant_192(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.00) + ordinal_margin(logits, labels) * 0.0300

def staging_loss_variant_193(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.25) + ordinal_margin(logits, labels) * 0.0400

def staging_loss_variant_194(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.50) + ordinal_margin(logits, labels) * 0.0500

def staging_loss_variant_195(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.75) + ordinal_margin(logits, labels) * 0.0100

def staging_loss_variant_196(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 2.00) + ordinal_margin(logits, labels) * 0.0200

def staging_loss_variant_197(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 2.25) + ordinal_margin(logits, labels) * 0.0300

def staging_loss_variant_198(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.00) + ordinal_margin(logits, labels) * 0.0400

def staging_loss_variant_199(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.25) + ordinal_margin(logits, labels) * 0.0500

def staging_loss_variant_200(logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    return focal_term(logits, labels, 1.50) + ordinal_margin(logits, labels) * 0.0100

