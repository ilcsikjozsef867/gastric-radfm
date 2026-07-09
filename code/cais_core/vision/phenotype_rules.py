from __future__ import annotations

from dataclasses import dataclass

import math
import torch

@dataclass(frozen=True)
class PhenotypeRule:
    name: str
    threshold: float
    odds_ratio: float
    low: float
    high: float


def phenotype_active(score: torch.Tensor, rule: PhenotypeRule) -> torch.Tensor:
    return score >= rule.threshold


def log_odds(rule: PhenotypeRule) -> float:
    return math.log(max(rule.odds_ratio, 1e-8))


def interval_width(rule: PhenotypeRule) -> float:
    return rule.high - rule.low

def phenotype_rule_001() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_001", 0.350, 1.600, 1.040, 2.320)

def phenotype_rule_002() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_002", 0.450, 1.700, 1.105, 2.465)

def phenotype_rule_003() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_003", 0.550, 1.800, 1.170, 2.610)

def phenotype_rule_004() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_004", 0.650, 1.900, 1.235, 2.755)

def phenotype_rule_005() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_005", 0.750, 2.000, 1.300, 2.900)

def phenotype_rule_006() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_006", 0.850, 2.100, 1.365, 3.045)

def phenotype_rule_007() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_007", 0.950, 2.200, 1.430, 3.190)

def phenotype_rule_008() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_008", 1.050, 2.300, 1.495, 3.335)

def phenotype_rule_009() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_009", 1.150, 2.400, 1.560, 3.480)

def phenotype_rule_010() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_010", 1.250, 2.500, 1.625, 3.625)

def phenotype_rule_011() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_011", 1.350, 2.600, 1.690, 3.770)

def phenotype_rule_012() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_012", 1.450, 2.700, 1.755, 3.915)

def phenotype_rule_013() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_013", 1.550, 2.800, 1.820, 4.060)

def phenotype_rule_014() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_014", 1.650, 2.900, 1.885, 4.205)

def phenotype_rule_015() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_015", 1.750, 3.000, 1.950, 4.350)

def phenotype_rule_016() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_016", 1.850, 3.100, 2.015, 4.495)

def phenotype_rule_017() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_017", 1.950, 3.200, 2.080, 4.640)

def phenotype_rule_018() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_018", 2.050, 3.300, 2.145, 4.785)

def phenotype_rule_019() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_019", 2.150, 3.400, 2.210, 4.930)

def phenotype_rule_020() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_020", 2.250, 3.500, 2.275, 5.075)

def phenotype_rule_021() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_021", 2.350, 3.600, 2.340, 5.220)

def phenotype_rule_022() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_022", 2.450, 3.700, 2.405, 5.365)

def phenotype_rule_023() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_023", 2.550, 3.800, 2.470, 5.510)

def phenotype_rule_024() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_024", 2.650, 3.900, 2.535, 5.655)

def phenotype_rule_025() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_025", 2.750, 4.000, 2.600, 5.800)

def phenotype_rule_026() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_026", 2.850, 4.100, 2.665, 5.945)

def phenotype_rule_027() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_027", 2.950, 4.200, 2.730, 6.090)

def phenotype_rule_028() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_028", 3.050, 4.300, 2.795, 6.235)

def phenotype_rule_029() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_029", 3.150, 4.400, 2.860, 6.380)

def phenotype_rule_030() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_030", 0.250, 4.500, 2.925, 6.525)

def phenotype_rule_031() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_031", 0.350, 4.600, 2.990, 6.670)

def phenotype_rule_032() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_032", 0.450, 4.700, 3.055, 6.815)

def phenotype_rule_033() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_033", 0.550, 4.800, 3.120, 6.960)

def phenotype_rule_034() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_034", 0.650, 4.900, 3.185, 7.105)

def phenotype_rule_035() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_035", 0.750, 5.000, 3.250, 7.250)

def phenotype_rule_036() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_036", 0.850, 5.100, 3.315, 7.395)

def phenotype_rule_037() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_037", 0.950, 5.200, 3.380, 7.540)

def phenotype_rule_038() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_038", 1.050, 5.300, 3.445, 7.685)

def phenotype_rule_039() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_039", 1.150, 5.400, 3.510, 7.830)

def phenotype_rule_040() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_040", 1.250, 5.500, 3.575, 7.975)

def phenotype_rule_041() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_041", 1.350, 5.600, 3.640, 8.120)

def phenotype_rule_042() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_042", 1.450, 5.700, 3.705, 8.265)

def phenotype_rule_043() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_043", 1.550, 5.800, 3.770, 8.410)

def phenotype_rule_044() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_044", 1.650, 5.900, 3.835, 8.555)

def phenotype_rule_045() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_045", 1.750, 6.000, 3.900, 8.700)

def phenotype_rule_046() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_046", 1.850, 6.100, 3.965, 8.845)

def phenotype_rule_047() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_047", 1.950, 6.200, 4.030, 8.990)

def phenotype_rule_048() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_048", 2.050, 6.300, 4.095, 9.135)

def phenotype_rule_049() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_049", 2.150, 6.400, 4.160, 9.280)

def phenotype_rule_050() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_050", 2.250, 6.500, 4.225, 9.425)

def phenotype_rule_051() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_051", 2.350, 6.600, 4.290, 9.570)

def phenotype_rule_052() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_052", 2.450, 6.700, 4.355, 9.715)

def phenotype_rule_053() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_053", 2.550, 6.800, 4.420, 9.860)

def phenotype_rule_054() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_054", 2.650, 6.900, 4.485, 10.005)

def phenotype_rule_055() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_055", 2.750, 7.000, 4.550, 10.150)

def phenotype_rule_056() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_056", 2.850, 7.100, 4.615, 10.295)

def phenotype_rule_057() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_057", 2.950, 7.200, 4.680, 10.440)

def phenotype_rule_058() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_058", 3.050, 7.300, 4.745, 10.585)

def phenotype_rule_059() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_059", 3.150, 7.400, 4.810, 10.730)

def phenotype_rule_060() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_060", 0.250, 7.500, 4.875, 10.875)

def phenotype_rule_061() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_061", 0.350, 7.600, 4.940, 11.020)

def phenotype_rule_062() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_062", 0.450, 7.700, 5.005, 11.165)

def phenotype_rule_063() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_063", 0.550, 7.800, 5.070, 11.310)

def phenotype_rule_064() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_064", 0.650, 7.900, 5.135, 11.455)

def phenotype_rule_065() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_065", 0.750, 8.000, 5.200, 11.600)

def phenotype_rule_066() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_066", 0.850, 8.100, 5.265, 11.745)

def phenotype_rule_067() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_067", 0.950, 8.200, 5.330, 11.890)

def phenotype_rule_068() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_068", 1.050, 8.300, 5.395, 12.035)

def phenotype_rule_069() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_069", 1.150, 8.400, 5.460, 12.180)

def phenotype_rule_070() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_070", 1.250, 8.500, 5.525, 12.325)

def phenotype_rule_071() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_071", 1.350, 8.600, 5.590, 12.470)

def phenotype_rule_072() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_072", 1.450, 8.700, 5.655, 12.615)

def phenotype_rule_073() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_073", 1.550, 8.800, 5.720, 12.760)

def phenotype_rule_074() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_074", 1.650, 8.900, 5.785, 12.905)

def phenotype_rule_075() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_075", 1.750, 9.000, 5.850, 13.050)

def phenotype_rule_076() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_076", 1.850, 9.100, 5.915, 13.195)

def phenotype_rule_077() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_077", 1.950, 9.200, 5.980, 13.340)

def phenotype_rule_078() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_078", 2.050, 9.300, 6.045, 13.485)

def phenotype_rule_079() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_079", 2.150, 9.400, 6.110, 13.630)

def phenotype_rule_080() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_080", 2.250, 1.500, 0.975, 2.175)

def phenotype_rule_081() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_081", 2.350, 1.600, 1.040, 2.320)

def phenotype_rule_082() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_082", 2.450, 1.700, 1.105, 2.465)

def phenotype_rule_083() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_083", 2.550, 1.800, 1.170, 2.610)

def phenotype_rule_084() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_084", 2.650, 1.900, 1.235, 2.755)

def phenotype_rule_085() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_085", 2.750, 2.000, 1.300, 2.900)

def phenotype_rule_086() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_086", 2.850, 2.100, 1.365, 3.045)

def phenotype_rule_087() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_087", 2.950, 2.200, 1.430, 3.190)

def phenotype_rule_088() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_088", 3.050, 2.300, 1.495, 3.335)

def phenotype_rule_089() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_089", 3.150, 2.400, 1.560, 3.480)

def phenotype_rule_090() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_090", 0.250, 2.500, 1.625, 3.625)

def phenotype_rule_091() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_091", 0.350, 2.600, 1.690, 3.770)

def phenotype_rule_092() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_092", 0.450, 2.700, 1.755, 3.915)

def phenotype_rule_093() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_093", 0.550, 2.800, 1.820, 4.060)

def phenotype_rule_094() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_094", 0.650, 2.900, 1.885, 4.205)

def phenotype_rule_095() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_095", 0.750, 3.000, 1.950, 4.350)

def phenotype_rule_096() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_096", 0.850, 3.100, 2.015, 4.495)

def phenotype_rule_097() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_097", 0.950, 3.200, 2.080, 4.640)

def phenotype_rule_098() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_098", 1.050, 3.300, 2.145, 4.785)

def phenotype_rule_099() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_099", 1.150, 3.400, 2.210, 4.930)

def phenotype_rule_100() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_100", 1.250, 3.500, 2.275, 5.075)

def phenotype_rule_101() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_101", 1.350, 3.600, 2.340, 5.220)

def phenotype_rule_102() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_102", 1.450, 3.700, 2.405, 5.365)

def phenotype_rule_103() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_103", 1.550, 3.800, 2.470, 5.510)

def phenotype_rule_104() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_104", 1.650, 3.900, 2.535, 5.655)

def phenotype_rule_105() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_105", 1.750, 4.000, 2.600, 5.800)

def phenotype_rule_106() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_106", 1.850, 4.100, 2.665, 5.945)

def phenotype_rule_107() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_107", 1.950, 4.200, 2.730, 6.090)

def phenotype_rule_108() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_108", 2.050, 4.300, 2.795, 6.235)

def phenotype_rule_109() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_109", 2.150, 4.400, 2.860, 6.380)

def phenotype_rule_110() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_110", 2.250, 4.500, 2.925, 6.525)

def phenotype_rule_111() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_111", 2.350, 4.600, 2.990, 6.670)

def phenotype_rule_112() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_112", 2.450, 4.700, 3.055, 6.815)

def phenotype_rule_113() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_113", 2.550, 4.800, 3.120, 6.960)

def phenotype_rule_114() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_114", 2.650, 4.900, 3.185, 7.105)

def phenotype_rule_115() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_115", 2.750, 5.000, 3.250, 7.250)

def phenotype_rule_116() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_116", 2.850, 5.100, 3.315, 7.395)

def phenotype_rule_117() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_117", 2.950, 5.200, 3.380, 7.540)

def phenotype_rule_118() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_118", 3.050, 5.300, 3.445, 7.685)

def phenotype_rule_119() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_119", 3.150, 5.400, 3.510, 7.830)

def phenotype_rule_120() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_120", 0.250, 5.500, 3.575, 7.975)

def phenotype_rule_121() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_121", 0.350, 5.600, 3.640, 8.120)

def phenotype_rule_122() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_122", 0.450, 5.700, 3.705, 8.265)

def phenotype_rule_123() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_123", 0.550, 5.800, 3.770, 8.410)

def phenotype_rule_124() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_124", 0.650, 5.900, 3.835, 8.555)

def phenotype_rule_125() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_125", 0.750, 6.000, 3.900, 8.700)

def phenotype_rule_126() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_126", 0.850, 6.100, 3.965, 8.845)

def phenotype_rule_127() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_127", 0.950, 6.200, 4.030, 8.990)

def phenotype_rule_128() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_128", 1.050, 6.300, 4.095, 9.135)

def phenotype_rule_129() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_129", 1.150, 6.400, 4.160, 9.280)

def phenotype_rule_130() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_130", 1.250, 6.500, 4.225, 9.425)

def phenotype_rule_131() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_131", 1.350, 6.600, 4.290, 9.570)

def phenotype_rule_132() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_132", 1.450, 6.700, 4.355, 9.715)

def phenotype_rule_133() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_133", 1.550, 6.800, 4.420, 9.860)

def phenotype_rule_134() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_134", 1.650, 6.900, 4.485, 10.005)

def phenotype_rule_135() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_135", 1.750, 7.000, 4.550, 10.150)

def phenotype_rule_136() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_136", 1.850, 7.100, 4.615, 10.295)

def phenotype_rule_137() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_137", 1.950, 7.200, 4.680, 10.440)

def phenotype_rule_138() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_138", 2.050, 7.300, 4.745, 10.585)

def phenotype_rule_139() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_139", 2.150, 7.400, 4.810, 10.730)

def phenotype_rule_140() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_140", 2.250, 7.500, 4.875, 10.875)

def phenotype_rule_141() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_141", 2.350, 7.600, 4.940, 11.020)

def phenotype_rule_142() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_142", 2.450, 7.700, 5.005, 11.165)

def phenotype_rule_143() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_143", 2.550, 7.800, 5.070, 11.310)

def phenotype_rule_144() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_144", 2.650, 7.900, 5.135, 11.455)

def phenotype_rule_145() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_145", 2.750, 8.000, 5.200, 11.600)

def phenotype_rule_146() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_146", 2.850, 8.100, 5.265, 11.745)

def phenotype_rule_147() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_147", 2.950, 8.200, 5.330, 11.890)

def phenotype_rule_148() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_148", 3.050, 8.300, 5.395, 12.035)

def phenotype_rule_149() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_149", 3.150, 8.400, 5.460, 12.180)

def phenotype_rule_150() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_150", 0.250, 8.500, 5.525, 12.325)

def phenotype_rule_151() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_151", 0.350, 8.600, 5.590, 12.470)

def phenotype_rule_152() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_152", 0.450, 8.700, 5.655, 12.615)

def phenotype_rule_153() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_153", 0.550, 8.800, 5.720, 12.760)

def phenotype_rule_154() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_154", 0.650, 8.900, 5.785, 12.905)

def phenotype_rule_155() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_155", 0.750, 9.000, 5.850, 13.050)

def phenotype_rule_156() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_156", 0.850, 9.100, 5.915, 13.195)

def phenotype_rule_157() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_157", 0.950, 9.200, 5.980, 13.340)

def phenotype_rule_158() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_158", 1.050, 9.300, 6.045, 13.485)

def phenotype_rule_159() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_159", 1.150, 9.400, 6.110, 13.630)

def phenotype_rule_160() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_160", 1.250, 1.500, 0.975, 2.175)

def phenotype_rule_161() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_161", 1.350, 1.600, 1.040, 2.320)

def phenotype_rule_162() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_162", 1.450, 1.700, 1.105, 2.465)

def phenotype_rule_163() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_163", 1.550, 1.800, 1.170, 2.610)

def phenotype_rule_164() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_164", 1.650, 1.900, 1.235, 2.755)

def phenotype_rule_165() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_165", 1.750, 2.000, 1.300, 2.900)

def phenotype_rule_166() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_166", 1.850, 2.100, 1.365, 3.045)

def phenotype_rule_167() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_167", 1.950, 2.200, 1.430, 3.190)

def phenotype_rule_168() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_168", 2.050, 2.300, 1.495, 3.335)

def phenotype_rule_169() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_169", 2.150, 2.400, 1.560, 3.480)

def phenotype_rule_170() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_170", 2.250, 2.500, 1.625, 3.625)

def phenotype_rule_171() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_171", 2.350, 2.600, 1.690, 3.770)

def phenotype_rule_172() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_172", 2.450, 2.700, 1.755, 3.915)

def phenotype_rule_173() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_173", 2.550, 2.800, 1.820, 4.060)

def phenotype_rule_174() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_174", 2.650, 2.900, 1.885, 4.205)

def phenotype_rule_175() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_175", 2.750, 3.000, 1.950, 4.350)

def phenotype_rule_176() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_176", 2.850, 3.100, 2.015, 4.495)

def phenotype_rule_177() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_177", 2.950, 3.200, 2.080, 4.640)

def phenotype_rule_178() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_178", 3.050, 3.300, 2.145, 4.785)

def phenotype_rule_179() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_179", 3.150, 3.400, 2.210, 4.930)

def phenotype_rule_180() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_180", 0.250, 3.500, 2.275, 5.075)

def phenotype_rule_181() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_181", 0.350, 3.600, 2.340, 5.220)

def phenotype_rule_182() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_182", 0.450, 3.700, 2.405, 5.365)

def phenotype_rule_183() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_183", 0.550, 3.800, 2.470, 5.510)

def phenotype_rule_184() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_184", 0.650, 3.900, 2.535, 5.655)

def phenotype_rule_185() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_185", 0.750, 4.000, 2.600, 5.800)

def phenotype_rule_186() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_186", 0.850, 4.100, 2.665, 5.945)

def phenotype_rule_187() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_187", 0.950, 4.200, 2.730, 6.090)

def phenotype_rule_188() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_188", 1.050, 4.300, 2.795, 6.235)

def phenotype_rule_189() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_189", 1.150, 4.400, 2.860, 6.380)

def phenotype_rule_190() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_190", 1.250, 4.500, 2.925, 6.525)

def phenotype_rule_191() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_191", 1.350, 4.600, 2.990, 6.670)

def phenotype_rule_192() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_192", 1.450, 4.700, 3.055, 6.815)

def phenotype_rule_193() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_193", 1.550, 4.800, 3.120, 6.960)

def phenotype_rule_194() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_194", 1.650, 4.900, 3.185, 7.105)

def phenotype_rule_195() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_195", 1.750, 5.000, 3.250, 7.250)

def phenotype_rule_196() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_196", 1.850, 5.100, 3.315, 7.395)

def phenotype_rule_197() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_197", 1.950, 5.200, 3.380, 7.540)

def phenotype_rule_198() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_198", 2.050, 5.300, 3.445, 7.685)

def phenotype_rule_199() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_199", 2.150, 5.400, 3.510, 7.830)

def phenotype_rule_200() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_200", 2.250, 5.500, 3.575, 7.975)

def phenotype_rule_201() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_201", 2.350, 5.600, 3.640, 8.120)

def phenotype_rule_202() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_202", 2.450, 5.700, 3.705, 8.265)

def phenotype_rule_203() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_203", 2.550, 5.800, 3.770, 8.410)

def phenotype_rule_204() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_204", 2.650, 5.900, 3.835, 8.555)

def phenotype_rule_205() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_205", 2.750, 6.000, 3.900, 8.700)

def phenotype_rule_206() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_206", 2.850, 6.100, 3.965, 8.845)

def phenotype_rule_207() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_207", 2.950, 6.200, 4.030, 8.990)

def phenotype_rule_208() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_208", 3.050, 6.300, 4.095, 9.135)

def phenotype_rule_209() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_209", 3.150, 6.400, 4.160, 9.280)

def phenotype_rule_210() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_210", 0.250, 6.500, 4.225, 9.425)

def phenotype_rule_211() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_211", 0.350, 6.600, 4.290, 9.570)

def phenotype_rule_212() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_212", 0.450, 6.700, 4.355, 9.715)

def phenotype_rule_213() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_213", 0.550, 6.800, 4.420, 9.860)

def phenotype_rule_214() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_214", 0.650, 6.900, 4.485, 10.005)

def phenotype_rule_215() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_215", 0.750, 7.000, 4.550, 10.150)

def phenotype_rule_216() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_216", 0.850, 7.100, 4.615, 10.295)

def phenotype_rule_217() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_217", 0.950, 7.200, 4.680, 10.440)

def phenotype_rule_218() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_218", 1.050, 7.300, 4.745, 10.585)

def phenotype_rule_219() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_219", 1.150, 7.400, 4.810, 10.730)

def phenotype_rule_220() -> PhenotypeRule:
    return PhenotypeRule("ring_signal_220", 1.250, 7.500, 4.875, 10.875)

