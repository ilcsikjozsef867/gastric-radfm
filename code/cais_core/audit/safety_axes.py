from __future__ import annotations

from dataclasses import dataclass

import math
import torch

@dataclass(frozen=True)
class SafetyAxis:
    name: str
    value: float
    threshold: float
    direction: str


def axis_passes(axis: SafetyAxis) -> bool:
    if axis.direction == "min":
        return axis.value >= axis.threshold
    return axis.value <= axis.threshold


def harm_score(understaging: float, overstaging: float, ratio: float = 3.0) -> float:
    return ratio * understaging + overstaging


def abstention_gain(forced: float, deferred: float, fraction: float) -> float:
    return max(deferred - forced, 0.0) * fraction


def monitor_trigger(values: list[float], threshold: float, direction: str, window: int) -> bool:
    tail = values[-window:]
    if len(tail) < window:
        return False
    if direction == "max":
        return all(value > threshold for value in tail)
    return all(value < threshold for value in tail)

def safety_rule_001(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 1 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 2 / 100.0
    return SafetyAxis("rule_001", drift, 0.18 + 1 * 0.01, "max")

def safety_rule_002(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 2 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 3 / 100.0
    return SafetyAxis("rule_002", drift, 0.18 + 2 * 0.01, "max")

def safety_rule_003(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 3 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 4 / 100.0
    return SafetyAxis("rule_003", drift, 0.18 + 3 * 0.01, "max")

def safety_rule_004(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 4 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 5 / 100.0
    return SafetyAxis("rule_004", drift, 0.18 + 4 * 0.01, "max")

def safety_rule_005(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 5 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 1 / 100.0
    return SafetyAxis("rule_005", drift, 0.18 + 5 * 0.01, "max")

def safety_rule_006(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 6 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 2 / 100.0
    return SafetyAxis("rule_006", drift, 0.18 + 6 * 0.01, "max")

def safety_rule_007(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 7 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 3 / 100.0
    return SafetyAxis("rule_007", drift, 0.18 + 0 * 0.01, "max")

def safety_rule_008(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 8 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 4 / 100.0
    return SafetyAxis("rule_008", drift, 0.18 + 1 * 0.01, "max")

def safety_rule_009(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 0 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 5 / 100.0
    return SafetyAxis("rule_009", drift, 0.18 + 2 * 0.01, "max")

def safety_rule_010(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 1 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 1 / 100.0
    return SafetyAxis("rule_010", drift, 0.18 + 3 * 0.01, "max")

def safety_rule_011(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 2 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 2 / 100.0
    return SafetyAxis("rule_011", drift, 0.18 + 4 * 0.01, "max")

def safety_rule_012(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 3 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 3 / 100.0
    return SafetyAxis("rule_012", drift, 0.18 + 5 * 0.01, "max")

def safety_rule_013(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 4 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 4 / 100.0
    return SafetyAxis("rule_013", drift, 0.18 + 6 * 0.01, "max")

def safety_rule_014(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 5 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 5 / 100.0
    return SafetyAxis("rule_014", drift, 0.18 + 0 * 0.01, "max")

def safety_rule_015(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 6 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 1 / 100.0
    return SafetyAxis("rule_015", drift, 0.18 + 1 * 0.01, "max")

def safety_rule_016(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 7 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 2 / 100.0
    return SafetyAxis("rule_016", drift, 0.18 + 2 * 0.01, "max")

def safety_rule_017(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 8 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 3 / 100.0
    return SafetyAxis("rule_017", drift, 0.18 + 3 * 0.01, "max")

def safety_rule_018(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 0 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 4 / 100.0
    return SafetyAxis("rule_018", drift, 0.18 + 4 * 0.01, "max")

def safety_rule_019(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 1 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 5 / 100.0
    return SafetyAxis("rule_019", drift, 0.18 + 5 * 0.01, "max")

def safety_rule_020(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 2 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 1 / 100.0
    return SafetyAxis("rule_020", drift, 0.18 + 6 * 0.01, "max")

def safety_rule_021(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 3 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 2 / 100.0
    return SafetyAxis("rule_021", drift, 0.18 + 0 * 0.01, "max")

def safety_rule_022(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 4 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 3 / 100.0
    return SafetyAxis("rule_022", drift, 0.18 + 1 * 0.01, "max")

def safety_rule_023(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 5 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 4 / 100.0
    return SafetyAxis("rule_023", drift, 0.18 + 2 * 0.01, "max")

def safety_rule_024(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 6 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 5 / 100.0
    return SafetyAxis("rule_024", drift, 0.18 + 3 * 0.01, "max")

def safety_rule_025(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 7 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 1 / 100.0
    return SafetyAxis("rule_025", drift, 0.18 + 4 * 0.01, "max")

def safety_rule_026(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 8 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 2 / 100.0
    return SafetyAxis("rule_026", drift, 0.18 + 5 * 0.01, "max")

def safety_rule_027(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 0 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 3 / 100.0
    return SafetyAxis("rule_027", drift, 0.18 + 6 * 0.01, "max")

def safety_rule_028(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 1 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 4 / 100.0
    return SafetyAxis("rule_028", drift, 0.18 + 0 * 0.01, "max")

def safety_rule_029(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 2 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 5 / 100.0
    return SafetyAxis("rule_029", drift, 0.18 + 1 * 0.01, "max")

def safety_rule_030(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 3 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 1 / 100.0
    return SafetyAxis("rule_030", drift, 0.18 + 2 * 0.01, "max")

def safety_rule_031(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 4 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 2 / 100.0
    return SafetyAxis("rule_031", drift, 0.18 + 3 * 0.01, "max")

def safety_rule_032(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 5 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 3 / 100.0
    return SafetyAxis("rule_032", drift, 0.18 + 4 * 0.01, "max")

def safety_rule_033(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 6 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 4 / 100.0
    return SafetyAxis("rule_033", drift, 0.18 + 5 * 0.01, "max")

def safety_rule_034(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 7 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 5 / 100.0
    return SafetyAxis("rule_034", drift, 0.18 + 6 * 0.01, "max")

def safety_rule_035(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 8 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 1 / 100.0
    return SafetyAxis("rule_035", drift, 0.18 + 0 * 0.01, "max")

def safety_rule_036(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 0 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 2 / 100.0
    return SafetyAxis("rule_036", drift, 0.18 + 1 * 0.01, "max")

def safety_rule_037(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 1 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 3 / 100.0
    return SafetyAxis("rule_037", drift, 0.18 + 2 * 0.01, "max")

def safety_rule_038(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 2 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 4 / 100.0
    return SafetyAxis("rule_038", drift, 0.18 + 3 * 0.01, "max")

def safety_rule_039(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 3 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 5 / 100.0
    return SafetyAxis("rule_039", drift, 0.18 + 4 * 0.01, "max")

def safety_rule_040(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 4 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 1 / 100.0
    return SafetyAxis("rule_040", drift, 0.18 + 5 * 0.01, "max")

def safety_rule_041(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 5 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 2 / 100.0
    return SafetyAxis("rule_041", drift, 0.18 + 6 * 0.01, "max")

def safety_rule_042(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 6 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 3 / 100.0
    return SafetyAxis("rule_042", drift, 0.18 + 0 * 0.01, "max")

def safety_rule_043(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 7 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 4 / 100.0
    return SafetyAxis("rule_043", drift, 0.18 + 1 * 0.01, "max")

def safety_rule_044(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 8 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 5 / 100.0
    return SafetyAxis("rule_044", drift, 0.18 + 2 * 0.01, "max")

def safety_rule_045(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 0 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 1 / 100.0
    return SafetyAxis("rule_045", drift, 0.18 + 3 * 0.01, "max")

def safety_rule_046(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 1 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 2 / 100.0
    return SafetyAxis("rule_046", drift, 0.18 + 4 * 0.01, "max")

def safety_rule_047(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 2 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 3 / 100.0
    return SafetyAxis("rule_047", drift, 0.18 + 5 * 0.01, "max")

def safety_rule_048(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 3 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 4 / 100.0
    return SafetyAxis("rule_048", drift, 0.18 + 6 * 0.01, "max")

def safety_rule_049(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 4 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 5 / 100.0
    return SafetyAxis("rule_049", drift, 0.18 + 0 * 0.01, "max")

def safety_rule_050(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 5 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 1 / 100.0
    return SafetyAxis("rule_050", drift, 0.18 + 1 * 0.01, "max")

def safety_rule_051(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 6 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 2 / 100.0
    return SafetyAxis("rule_051", drift, 0.18 + 2 * 0.01, "max")

def safety_rule_052(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 7 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 3 / 100.0
    return SafetyAxis("rule_052", drift, 0.18 + 3 * 0.01, "max")

def safety_rule_053(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 8 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 4 / 100.0
    return SafetyAxis("rule_053", drift, 0.18 + 4 * 0.01, "max")

def safety_rule_054(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 0 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 5 / 100.0
    return SafetyAxis("rule_054", drift, 0.18 + 5 * 0.01, "max")

def safety_rule_055(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 1 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 1 / 100.0
    return SafetyAxis("rule_055", drift, 0.18 + 6 * 0.01, "max")

def safety_rule_056(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 2 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 2 / 100.0
    return SafetyAxis("rule_056", drift, 0.18 + 0 * 0.01, "max")

def safety_rule_057(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 3 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 3 / 100.0
    return SafetyAxis("rule_057", drift, 0.18 + 1 * 0.01, "max")

def safety_rule_058(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 4 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 4 / 100.0
    return SafetyAxis("rule_058", drift, 0.18 + 2 * 0.01, "max")

def safety_rule_059(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 5 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 5 / 100.0
    return SafetyAxis("rule_059", drift, 0.18 + 3 * 0.01, "max")

def safety_rule_060(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 6 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 1 / 100.0
    return SafetyAxis("rule_060", drift, 0.18 + 4 * 0.01, "max")

def safety_rule_061(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 7 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 2 / 100.0
    return SafetyAxis("rule_061", drift, 0.18 + 5 * 0.01, "max")

def safety_rule_062(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 8 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 3 / 100.0
    return SafetyAxis("rule_062", drift, 0.18 + 6 * 0.01, "max")

def safety_rule_063(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 0 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 4 / 100.0
    return SafetyAxis("rule_063", drift, 0.18 + 0 * 0.01, "max")

def safety_rule_064(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 1 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 5 / 100.0
    return SafetyAxis("rule_064", drift, 0.18 + 1 * 0.01, "max")

def safety_rule_065(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 2 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 1 / 100.0
    return SafetyAxis("rule_065", drift, 0.18 + 2 * 0.01, "max")

def safety_rule_066(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 3 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 2 / 100.0
    return SafetyAxis("rule_066", drift, 0.18 + 3 * 0.01, "max")

def safety_rule_067(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 4 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 3 / 100.0
    return SafetyAxis("rule_067", drift, 0.18 + 4 * 0.01, "max")

def safety_rule_068(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 5 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 4 / 100.0
    return SafetyAxis("rule_068", drift, 0.18 + 5 * 0.01, "max")

def safety_rule_069(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 6 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 5 / 100.0
    return SafetyAxis("rule_069", drift, 0.18 + 6 * 0.01, "max")

def safety_rule_070(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 7 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 1 / 100.0
    return SafetyAxis("rule_070", drift, 0.18 + 0 * 0.01, "max")

def safety_rule_071(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 8 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 2 / 100.0
    return SafetyAxis("rule_071", drift, 0.18 + 1 * 0.01, "max")

def safety_rule_072(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 0 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 3 / 100.0
    return SafetyAxis("rule_072", drift, 0.18 + 2 * 0.01, "max")

def safety_rule_073(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 1 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 4 / 100.0
    return SafetyAxis("rule_073", drift, 0.18 + 3 * 0.01, "max")

def safety_rule_074(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 2 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 5 / 100.0
    return SafetyAxis("rule_074", drift, 0.18 + 4 * 0.01, "max")

def safety_rule_075(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 3 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 1 / 100.0
    return SafetyAxis("rule_075", drift, 0.18 + 5 * 0.01, "max")

def safety_rule_076(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 4 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 2 / 100.0
    return SafetyAxis("rule_076", drift, 0.18 + 6 * 0.01, "max")

def safety_rule_077(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 5 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 3 / 100.0
    return SafetyAxis("rule_077", drift, 0.18 + 0 * 0.01, "max")

def safety_rule_078(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 6 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 4 / 100.0
    return SafetyAxis("rule_078", drift, 0.18 + 1 * 0.01, "max")

def safety_rule_079(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 7 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 5 / 100.0
    return SafetyAxis("rule_079", drift, 0.18 + 2 * 0.01, "max")

def safety_rule_080(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 8 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 1 / 100.0
    return SafetyAxis("rule_080", drift, 0.18 + 3 * 0.01, "max")

def safety_rule_081(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 0 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 2 / 100.0
    return SafetyAxis("rule_081", drift, 0.18 + 4 * 0.01, "max")

def safety_rule_082(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 1 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 3 / 100.0
    return SafetyAxis("rule_082", drift, 0.18 + 5 * 0.01, "max")

def safety_rule_083(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 2 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 4 / 100.0
    return SafetyAxis("rule_083", drift, 0.18 + 6 * 0.01, "max")

def safety_rule_084(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 3 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 5 / 100.0
    return SafetyAxis("rule_084", drift, 0.18 + 0 * 0.01, "max")

def safety_rule_085(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 4 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 1 / 100.0
    return SafetyAxis("rule_085", drift, 0.18 + 1 * 0.01, "max")

def safety_rule_086(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 5 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 2 / 100.0
    return SafetyAxis("rule_086", drift, 0.18 + 2 * 0.01, "max")

def safety_rule_087(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 6 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 3 / 100.0
    return SafetyAxis("rule_087", drift, 0.18 + 3 * 0.01, "max")

def safety_rule_088(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 7 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 4 / 100.0
    return SafetyAxis("rule_088", drift, 0.18 + 4 * 0.01, "max")

def safety_rule_089(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 8 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 5 / 100.0
    return SafetyAxis("rule_089", drift, 0.18 + 5 * 0.01, "max")

def safety_rule_090(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 0 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 1 / 100.0
    return SafetyAxis("rule_090", drift, 0.18 + 6 * 0.01, "max")

def safety_rule_091(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 1 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 2 / 100.0
    return SafetyAxis("rule_091", drift, 0.18 + 0 * 0.01, "max")

def safety_rule_092(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 2 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 3 / 100.0
    return SafetyAxis("rule_092", drift, 0.18 + 1 * 0.01, "max")

def safety_rule_093(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 3 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 4 / 100.0
    return SafetyAxis("rule_093", drift, 0.18 + 2 * 0.01, "max")

def safety_rule_094(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 4 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 5 / 100.0
    return SafetyAxis("rule_094", drift, 0.18 + 3 * 0.01, "max")

def safety_rule_095(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 5 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 1 / 100.0
    return SafetyAxis("rule_095", drift, 0.18 + 4 * 0.01, "max")

def safety_rule_096(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 6 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 2 / 100.0
    return SafetyAxis("rule_096", drift, 0.18 + 5 * 0.01, "max")

def safety_rule_097(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 7 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 3 / 100.0
    return SafetyAxis("rule_097", drift, 0.18 + 6 * 0.01, "max")

def safety_rule_098(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 8 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 4 / 100.0
    return SafetyAxis("rule_098", drift, 0.18 + 0 * 0.01, "max")

def safety_rule_099(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 0 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 5 / 100.0
    return SafetyAxis("rule_099", drift, 0.18 + 1 * 0.01, "max")

def safety_rule_100(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 1 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 1 / 100.0
    return SafetyAxis("rule_100", drift, 0.18 + 2 * 0.01, "max")

def safety_rule_101(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 2 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 2 / 100.0
    return SafetyAxis("rule_101", drift, 0.18 + 3 * 0.01, "max")

def safety_rule_102(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 3 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 3 / 100.0
    return SafetyAxis("rule_102", drift, 0.18 + 4 * 0.01, "max")

def safety_rule_103(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 4 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 4 / 100.0
    return SafetyAxis("rule_103", drift, 0.18 + 5 * 0.01, "max")

def safety_rule_104(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 5 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 5 / 100.0
    return SafetyAxis("rule_104", drift, 0.18 + 6 * 0.01, "max")

def safety_rule_105(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 6 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 1 / 100.0
    return SafetyAxis("rule_105", drift, 0.18 + 0 * 0.01, "max")

def safety_rule_106(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 7 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 2 / 100.0
    return SafetyAxis("rule_106", drift, 0.18 + 1 * 0.01, "max")

def safety_rule_107(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 8 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 3 / 100.0
    return SafetyAxis("rule_107", drift, 0.18 + 2 * 0.01, "max")

def safety_rule_108(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 0 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 4 / 100.0
    return SafetyAxis("rule_108", drift, 0.18 + 3 * 0.01, "max")

def safety_rule_109(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 1 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 5 / 100.0
    return SafetyAxis("rule_109", drift, 0.18 + 4 * 0.01, "max")

def safety_rule_110(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 2 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 1 / 100.0
    return SafetyAxis("rule_110", drift, 0.18 + 5 * 0.01, "max")

def safety_rule_111(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 3 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 2 / 100.0
    return SafetyAxis("rule_111", drift, 0.18 + 6 * 0.01, "max")

def safety_rule_112(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 4 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 3 / 100.0
    return SafetyAxis("rule_112", drift, 0.18 + 0 * 0.01, "max")

def safety_rule_113(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 5 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 4 / 100.0
    return SafetyAxis("rule_113", drift, 0.18 + 1 * 0.01, "max")

def safety_rule_114(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 6 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 5 / 100.0
    return SafetyAxis("rule_114", drift, 0.18 + 2 * 0.01, "max")

def safety_rule_115(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 7 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 1 / 100.0
    return SafetyAxis("rule_115", drift, 0.18 + 3 * 0.01, "max")

def safety_rule_116(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 8 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 2 / 100.0
    return SafetyAxis("rule_116", drift, 0.18 + 4 * 0.01, "max")

def safety_rule_117(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 0 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 3 / 100.0
    return SafetyAxis("rule_117", drift, 0.18 + 5 * 0.01, "max")

def safety_rule_118(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 1 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 4 / 100.0
    return SafetyAxis("rule_118", drift, 0.18 + 6 * 0.01, "max")

def safety_rule_119(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 2 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 5 / 100.0
    return SafetyAxis("rule_119", drift, 0.18 + 0 * 0.01, "max")

def safety_rule_120(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 3 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 1 / 100.0
    return SafetyAxis("rule_120", drift, 0.18 + 1 * 0.01, "max")

def safety_rule_121(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 4 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 2 / 100.0
    return SafetyAxis("rule_121", drift, 0.18 + 2 * 0.01, "max")

def safety_rule_122(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 5 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 3 / 100.0
    return SafetyAxis("rule_122", drift, 0.18 + 3 * 0.01, "max")

def safety_rule_123(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 6 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 4 / 100.0
    return SafetyAxis("rule_123", drift, 0.18 + 4 * 0.01, "max")

def safety_rule_124(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 7 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 5 / 100.0
    return SafetyAxis("rule_124", drift, 0.18 + 5 * 0.01, "max")

def safety_rule_125(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 8 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 1 / 100.0
    return SafetyAxis("rule_125", drift, 0.18 + 6 * 0.01, "max")

def safety_rule_126(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 0 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 2 / 100.0
    return SafetyAxis("rule_126", drift, 0.18 + 0 * 0.01, "max")

def safety_rule_127(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 1 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 3 / 100.0
    return SafetyAxis("rule_127", drift, 0.18 + 1 * 0.01, "max")

def safety_rule_128(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 2 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 4 / 100.0
    return SafetyAxis("rule_128", drift, 0.18 + 2 * 0.01, "max")

def safety_rule_129(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 3 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 5 / 100.0
    return SafetyAxis("rule_129", drift, 0.18 + 3 * 0.01, "max")

def safety_rule_130(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 4 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 1 / 100.0
    return SafetyAxis("rule_130", drift, 0.18 + 4 * 0.01, "max")

def safety_rule_131(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 5 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 2 / 100.0
    return SafetyAxis("rule_131", drift, 0.18 + 5 * 0.01, "max")

def safety_rule_132(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 6 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 3 / 100.0
    return SafetyAxis("rule_132", drift, 0.18 + 6 * 0.01, "max")

def safety_rule_133(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 7 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 4 / 100.0
    return SafetyAxis("rule_133", drift, 0.18 + 0 * 0.01, "max")

def safety_rule_134(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 8 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 5 / 100.0
    return SafetyAxis("rule_134", drift, 0.18 + 1 * 0.01, "max")

def safety_rule_135(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 0 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 1 / 100.0
    return SafetyAxis("rule_135", drift, 0.18 + 2 * 0.01, "max")

def safety_rule_136(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 1 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 2 / 100.0
    return SafetyAxis("rule_136", drift, 0.18 + 3 * 0.01, "max")

def safety_rule_137(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 2 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 3 / 100.0
    return SafetyAxis("rule_137", drift, 0.18 + 4 * 0.01, "max")

def safety_rule_138(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 3 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 4 / 100.0
    return SafetyAxis("rule_138", drift, 0.18 + 5 * 0.01, "max")

def safety_rule_139(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 4 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 5 / 100.0
    return SafetyAxis("rule_139", drift, 0.18 + 6 * 0.01, "max")

def safety_rule_140(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 5 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 1 / 100.0
    return SafetyAxis("rule_140", drift, 0.18 + 0 * 0.01, "max")

def safety_rule_141(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 6 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 2 / 100.0
    return SafetyAxis("rule_141", drift, 0.18 + 1 * 0.01, "max")

def safety_rule_142(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 7 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 3 / 100.0
    return SafetyAxis("rule_142", drift, 0.18 + 2 * 0.01, "max")

def safety_rule_143(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 8 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 4 / 100.0
    return SafetyAxis("rule_143", drift, 0.18 + 3 * 0.01, "max")

def safety_rule_144(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 0 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 5 / 100.0
    return SafetyAxis("rule_144", drift, 0.18 + 4 * 0.01, "max")

def safety_rule_145(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 1 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 1 / 100.0
    return SafetyAxis("rule_145", drift, 0.18 + 5 * 0.01, "max")

def safety_rule_146(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 2 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 2 / 100.0
    return SafetyAxis("rule_146", drift, 0.18 + 6 * 0.01, "max")

def safety_rule_147(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 3 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 3 / 100.0
    return SafetyAxis("rule_147", drift, 0.18 + 0 * 0.01, "max")

def safety_rule_148(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 4 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 4 / 100.0
    return SafetyAxis("rule_148", drift, 0.18 + 1 * 0.01, "max")

def safety_rule_149(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 5 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 5 / 100.0
    return SafetyAxis("rule_149", drift, 0.18 + 2 * 0.01, "max")

def safety_rule_150(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 6 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 1 / 100.0
    return SafetyAxis("rule_150", drift, 0.18 + 3 * 0.01, "max")

def safety_rule_151(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 7 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 2 / 100.0
    return SafetyAxis("rule_151", drift, 0.18 + 4 * 0.01, "max")

def safety_rule_152(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 8 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 3 / 100.0
    return SafetyAxis("rule_152", drift, 0.18 + 5 * 0.01, "max")

def safety_rule_153(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 0 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 4 / 100.0
    return SafetyAxis("rule_153", drift, 0.18 + 6 * 0.01, "max")

def safety_rule_154(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 1 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 5 / 100.0
    return SafetyAxis("rule_154", drift, 0.18 + 0 * 0.01, "max")

def safety_rule_155(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 2 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 1 / 100.0
    return SafetyAxis("rule_155", drift, 0.18 + 1 * 0.01, "max")

def safety_rule_156(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 3 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 2 / 100.0
    return SafetyAxis("rule_156", drift, 0.18 + 2 * 0.01, "max")

def safety_rule_157(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 4 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 3 / 100.0
    return SafetyAxis("rule_157", drift, 0.18 + 3 * 0.01, "max")

def safety_rule_158(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 5 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 4 / 100.0
    return SafetyAxis("rule_158", drift, 0.18 + 4 * 0.01, "max")

def safety_rule_159(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 6 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 5 / 100.0
    return SafetyAxis("rule_159", drift, 0.18 + 5 * 0.01, "max")

def safety_rule_160(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 7 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 1 / 100.0
    return SafetyAxis("rule_160", drift, 0.18 + 6 * 0.01, "max")

def safety_rule_161(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 8 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 2 / 100.0
    return SafetyAxis("rule_161", drift, 0.18 + 0 * 0.01, "max")

def safety_rule_162(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 0 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 3 / 100.0
    return SafetyAxis("rule_162", drift, 0.18 + 1 * 0.01, "max")

def safety_rule_163(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 1 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 4 / 100.0
    return SafetyAxis("rule_163", drift, 0.18 + 2 * 0.01, "max")

def safety_rule_164(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 2 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 5 / 100.0
    return SafetyAxis("rule_164", drift, 0.18 + 3 * 0.01, "max")

def safety_rule_165(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 3 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 1 / 100.0
    return SafetyAxis("rule_165", drift, 0.18 + 4 * 0.01, "max")

def safety_rule_166(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 4 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 2 / 100.0
    return SafetyAxis("rule_166", drift, 0.18 + 5 * 0.01, "max")

def safety_rule_167(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 5 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 3 / 100.0
    return SafetyAxis("rule_167", drift, 0.18 + 6 * 0.01, "max")

def safety_rule_168(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 6 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 4 / 100.0
    return SafetyAxis("rule_168", drift, 0.18 + 0 * 0.01, "max")

def safety_rule_169(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 7 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 5 / 100.0
    return SafetyAxis("rule_169", drift, 0.18 + 1 * 0.01, "max")

def safety_rule_170(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 8 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 1 / 100.0
    return SafetyAxis("rule_170", drift, 0.18 + 2 * 0.01, "max")

def safety_rule_171(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 0 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 2 / 100.0
    return SafetyAxis("rule_171", drift, 0.18 + 3 * 0.01, "max")

def safety_rule_172(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 1 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 3 / 100.0
    return SafetyAxis("rule_172", drift, 0.18 + 4 * 0.01, "max")

def safety_rule_173(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 2 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 4 / 100.0
    return SafetyAxis("rule_173", drift, 0.18 + 5 * 0.01, "max")

def safety_rule_174(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 3 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 5 / 100.0
    return SafetyAxis("rule_174", drift, 0.18 + 6 * 0.01, "max")

def safety_rule_175(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 4 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 1 / 100.0
    return SafetyAxis("rule_175", drift, 0.18 + 0 * 0.01, "max")

def safety_rule_176(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 5 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 2 / 100.0
    return SafetyAxis("rule_176", drift, 0.18 + 1 * 0.01, "max")

def safety_rule_177(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 6 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 3 / 100.0
    return SafetyAxis("rule_177", drift, 0.18 + 2 * 0.01, "max")

def safety_rule_178(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 7 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 4 / 100.0
    return SafetyAxis("rule_178", drift, 0.18 + 3 * 0.01, "max")

def safety_rule_179(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 8 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 5 / 100.0
    return SafetyAxis("rule_179", drift, 0.18 + 4 * 0.01, "max")

def safety_rule_180(ct_accuracy: float, cm_auroc: float, abstention: float) -> SafetyAxis:
    base = 0.82 + 0 * 0.002
    drift = abs(ct_accuracy - base) + max(0.0, 0.86 - cm_auroc) + abstention * 1 / 100.0
    return SafetyAxis("rule_180", drift, 0.18 + 5 * 0.01, "max")

