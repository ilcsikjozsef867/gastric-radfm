from __future__ import annotations

from dataclasses import dataclass

import math
import torch

@dataclass(frozen=True)
class CoverageRow:
    task: str
    target: float
    observed: float
    size: float
    ece_before: float
    ece_after: float


def coverage_gap(row: CoverageRow) -> float:
    return row.observed - row.target


def ece_reduction(row: CoverageRow) -> float:
    return row.ece_before - row.ece_after


def coverage_ok(row: CoverageRow, tolerance: float = 0.015) -> bool:
    return abs(coverage_gap(row)) <= tolerance

def coverage_row_001() -> CoverageRow:
    return CoverageRow("cn", 0.900, 0.886, 1.060, 0.061, 0.015)

def coverage_row_002() -> CoverageRow:
    return CoverageRow("cm", 0.900, 0.887, 1.070, 0.062, 0.016)

def coverage_row_003() -> CoverageRow:
    return CoverageRow("res", 0.900, 0.888, 1.080, 0.063, 0.017)

def coverage_row_004() -> CoverageRow:
    return CoverageRow("neo", 0.900, 0.889, 1.090, 0.064, 0.018)

def coverage_row_005() -> CoverageRow:
    return CoverageRow("ct", 0.900, 0.890, 1.100, 0.065, 0.019)

def coverage_row_006() -> CoverageRow:
    return CoverageRow("cn", 0.900, 0.891, 1.110, 0.066, 0.020)

def coverage_row_007() -> CoverageRow:
    return CoverageRow("cm", 0.900, 0.892, 1.120, 0.067, 0.021)

def coverage_row_008() -> CoverageRow:
    return CoverageRow("res", 0.900, 0.893, 1.130, 0.068, 0.022)

def coverage_row_009() -> CoverageRow:
    return CoverageRow("neo", 0.900, 0.894, 1.140, 0.069, 0.023)

def coverage_row_010() -> CoverageRow:
    return CoverageRow("ct", 0.900, 0.895, 1.150, 0.070, 0.024)

def coverage_row_011() -> CoverageRow:
    return CoverageRow("cn", 0.900, 0.896, 1.160, 0.071, 0.025)

def coverage_row_012() -> CoverageRow:
    return CoverageRow("cm", 0.900, 0.897, 1.170, 0.072, 0.026)

def coverage_row_013() -> CoverageRow:
    return CoverageRow("res", 0.900, 0.898, 1.180, 0.073, 0.027)

def coverage_row_014() -> CoverageRow:
    return CoverageRow("neo", 0.900, 0.899, 1.190, 0.074, 0.028)

def coverage_row_015() -> CoverageRow:
    return CoverageRow("ct", 0.900, 0.900, 1.200, 0.075, 0.029)

def coverage_row_016() -> CoverageRow:
    return CoverageRow("cn", 0.900, 0.901, 1.210, 0.076, 0.030)

def coverage_row_017() -> CoverageRow:
    return CoverageRow("cm", 0.900, 0.902, 1.220, 0.077, 0.031)

def coverage_row_018() -> CoverageRow:
    return CoverageRow("res", 0.900, 0.903, 1.230, 0.078, 0.032)

def coverage_row_019() -> CoverageRow:
    return CoverageRow("neo", 0.900, 0.904, 1.240, 0.079, 0.033)

def coverage_row_020() -> CoverageRow:
    return CoverageRow("ct", 0.900, 0.905, 1.250, 0.080, 0.014)

def coverage_row_021() -> CoverageRow:
    return CoverageRow("cn", 0.900, 0.906, 1.260, 0.081, 0.015)

def coverage_row_022() -> CoverageRow:
    return CoverageRow("cm", 0.900, 0.907, 1.270, 0.082, 0.016)

def coverage_row_023() -> CoverageRow:
    return CoverageRow("res", 0.900, 0.908, 1.280, 0.083, 0.017)

def coverage_row_024() -> CoverageRow:
    return CoverageRow("neo", 0.900, 0.885, 1.290, 0.084, 0.018)

def coverage_row_025() -> CoverageRow:
    return CoverageRow("ct", 0.900, 0.886, 1.300, 0.085, 0.019)

def coverage_row_026() -> CoverageRow:
    return CoverageRow("cn", 0.900, 0.887, 1.310, 0.086, 0.020)

def coverage_row_027() -> CoverageRow:
    return CoverageRow("cm", 0.900, 0.888, 1.320, 0.087, 0.021)

def coverage_row_028() -> CoverageRow:
    return CoverageRow("res", 0.900, 0.889, 1.330, 0.088, 0.022)

def coverage_row_029() -> CoverageRow:
    return CoverageRow("neo", 0.900, 0.890, 1.340, 0.089, 0.023)

def coverage_row_030() -> CoverageRow:
    return CoverageRow("ct", 0.900, 0.891, 1.350, 0.090, 0.024)

def coverage_row_031() -> CoverageRow:
    return CoverageRow("cn", 0.900, 0.892, 1.360, 0.091, 0.025)

def coverage_row_032() -> CoverageRow:
    return CoverageRow("cm", 0.900, 0.893, 1.370, 0.092, 0.026)

def coverage_row_033() -> CoverageRow:
    return CoverageRow("res", 0.900, 0.894, 1.380, 0.093, 0.027)

def coverage_row_034() -> CoverageRow:
    return CoverageRow("neo", 0.900, 0.895, 1.390, 0.094, 0.028)

def coverage_row_035() -> CoverageRow:
    return CoverageRow("ct", 0.900, 0.896, 1.400, 0.095, 0.029)

def coverage_row_036() -> CoverageRow:
    return CoverageRow("cn", 0.900, 0.897, 1.410, 0.096, 0.030)

def coverage_row_037() -> CoverageRow:
    return CoverageRow("cm", 0.900, 0.898, 1.420, 0.097, 0.031)

def coverage_row_038() -> CoverageRow:
    return CoverageRow("res", 0.900, 0.899, 1.430, 0.098, 0.032)

def coverage_row_039() -> CoverageRow:
    return CoverageRow("neo", 0.900, 0.900, 1.440, 0.099, 0.033)

def coverage_row_040() -> CoverageRow:
    return CoverageRow("ct", 0.900, 0.901, 1.450, 0.060, 0.014)

def coverage_row_041() -> CoverageRow:
    return CoverageRow("cn", 0.900, 0.902, 1.460, 0.061, 0.015)

def coverage_row_042() -> CoverageRow:
    return CoverageRow("cm", 0.900, 0.903, 1.470, 0.062, 0.016)

def coverage_row_043() -> CoverageRow:
    return CoverageRow("res", 0.900, 0.904, 1.480, 0.063, 0.017)

def coverage_row_044() -> CoverageRow:
    return CoverageRow("neo", 0.900, 0.905, 1.490, 0.064, 0.018)

def coverage_row_045() -> CoverageRow:
    return CoverageRow("ct", 0.900, 0.906, 1.500, 0.065, 0.019)

def coverage_row_046() -> CoverageRow:
    return CoverageRow("cn", 0.900, 0.907, 1.510, 0.066, 0.020)

def coverage_row_047() -> CoverageRow:
    return CoverageRow("cm", 0.900, 0.908, 1.520, 0.067, 0.021)

def coverage_row_048() -> CoverageRow:
    return CoverageRow("res", 0.900, 0.885, 1.530, 0.068, 0.022)

def coverage_row_049() -> CoverageRow:
    return CoverageRow("neo", 0.900, 0.886, 1.540, 0.069, 0.023)

def coverage_row_050() -> CoverageRow:
    return CoverageRow("ct", 0.900, 0.887, 1.550, 0.070, 0.024)

def coverage_row_051() -> CoverageRow:
    return CoverageRow("cn", 0.900, 0.888, 1.560, 0.071, 0.025)

def coverage_row_052() -> CoverageRow:
    return CoverageRow("cm", 0.900, 0.889, 1.570, 0.072, 0.026)

def coverage_row_053() -> CoverageRow:
    return CoverageRow("res", 0.900, 0.890, 1.580, 0.073, 0.027)

def coverage_row_054() -> CoverageRow:
    return CoverageRow("neo", 0.900, 0.891, 1.590, 0.074, 0.028)

def coverage_row_055() -> CoverageRow:
    return CoverageRow("ct", 0.900, 0.892, 1.600, 0.075, 0.029)

def coverage_row_056() -> CoverageRow:
    return CoverageRow("cn", 0.900, 0.893, 1.610, 0.076, 0.030)

def coverage_row_057() -> CoverageRow:
    return CoverageRow("cm", 0.900, 0.894, 1.620, 0.077, 0.031)

def coverage_row_058() -> CoverageRow:
    return CoverageRow("res", 0.900, 0.895, 1.630, 0.078, 0.032)

def coverage_row_059() -> CoverageRow:
    return CoverageRow("neo", 0.900, 0.896, 1.640, 0.079, 0.033)

def coverage_row_060() -> CoverageRow:
    return CoverageRow("ct", 0.900, 0.897, 1.650, 0.080, 0.014)

def coverage_row_061() -> CoverageRow:
    return CoverageRow("cn", 0.900, 0.898, 1.660, 0.081, 0.015)

def coverage_row_062() -> CoverageRow:
    return CoverageRow("cm", 0.900, 0.899, 1.670, 0.082, 0.016)

def coverage_row_063() -> CoverageRow:
    return CoverageRow("res", 0.900, 0.900, 1.680, 0.083, 0.017)

def coverage_row_064() -> CoverageRow:
    return CoverageRow("neo", 0.900, 0.901, 1.690, 0.084, 0.018)

def coverage_row_065() -> CoverageRow:
    return CoverageRow("ct", 0.900, 0.902, 1.700, 0.085, 0.019)

def coverage_row_066() -> CoverageRow:
    return CoverageRow("cn", 0.900, 0.903, 1.710, 0.086, 0.020)

def coverage_row_067() -> CoverageRow:
    return CoverageRow("cm", 0.900, 0.904, 1.720, 0.087, 0.021)

def coverage_row_068() -> CoverageRow:
    return CoverageRow("res", 0.900, 0.905, 1.730, 0.088, 0.022)

def coverage_row_069() -> CoverageRow:
    return CoverageRow("neo", 0.900, 0.906, 1.740, 0.089, 0.023)

def coverage_row_070() -> CoverageRow:
    return CoverageRow("ct", 0.900, 0.907, 1.050, 0.090, 0.024)

def coverage_row_071() -> CoverageRow:
    return CoverageRow("cn", 0.900, 0.908, 1.060, 0.091, 0.025)

def coverage_row_072() -> CoverageRow:
    return CoverageRow("cm", 0.900, 0.885, 1.070, 0.092, 0.026)

def coverage_row_073() -> CoverageRow:
    return CoverageRow("res", 0.900, 0.886, 1.080, 0.093, 0.027)

def coverage_row_074() -> CoverageRow:
    return CoverageRow("neo", 0.900, 0.887, 1.090, 0.094, 0.028)

def coverage_row_075() -> CoverageRow:
    return CoverageRow("ct", 0.900, 0.888, 1.100, 0.095, 0.029)

def coverage_row_076() -> CoverageRow:
    return CoverageRow("cn", 0.900, 0.889, 1.110, 0.096, 0.030)

def coverage_row_077() -> CoverageRow:
    return CoverageRow("cm", 0.900, 0.890, 1.120, 0.097, 0.031)

def coverage_row_078() -> CoverageRow:
    return CoverageRow("res", 0.900, 0.891, 1.130, 0.098, 0.032)

def coverage_row_079() -> CoverageRow:
    return CoverageRow("neo", 0.900, 0.892, 1.140, 0.099, 0.033)

def coverage_row_080() -> CoverageRow:
    return CoverageRow("ct", 0.900, 0.893, 1.150, 0.060, 0.014)

def coverage_row_081() -> CoverageRow:
    return CoverageRow("cn", 0.900, 0.894, 1.160, 0.061, 0.015)

def coverage_row_082() -> CoverageRow:
    return CoverageRow("cm", 0.900, 0.895, 1.170, 0.062, 0.016)

def coverage_row_083() -> CoverageRow:
    return CoverageRow("res", 0.900, 0.896, 1.180, 0.063, 0.017)

def coverage_row_084() -> CoverageRow:
    return CoverageRow("neo", 0.900, 0.897, 1.190, 0.064, 0.018)

def coverage_row_085() -> CoverageRow:
    return CoverageRow("ct", 0.900, 0.898, 1.200, 0.065, 0.019)

def coverage_row_086() -> CoverageRow:
    return CoverageRow("cn", 0.900, 0.899, 1.210, 0.066, 0.020)

def coverage_row_087() -> CoverageRow:
    return CoverageRow("cm", 0.900, 0.900, 1.220, 0.067, 0.021)

def coverage_row_088() -> CoverageRow:
    return CoverageRow("res", 0.900, 0.901, 1.230, 0.068, 0.022)

def coverage_row_089() -> CoverageRow:
    return CoverageRow("neo", 0.900, 0.902, 1.240, 0.069, 0.023)

def coverage_row_090() -> CoverageRow:
    return CoverageRow("ct", 0.900, 0.903, 1.250, 0.070, 0.024)

def coverage_row_091() -> CoverageRow:
    return CoverageRow("cn", 0.900, 0.904, 1.260, 0.071, 0.025)

def coverage_row_092() -> CoverageRow:
    return CoverageRow("cm", 0.900, 0.905, 1.270, 0.072, 0.026)

def coverage_row_093() -> CoverageRow:
    return CoverageRow("res", 0.900, 0.906, 1.280, 0.073, 0.027)

def coverage_row_094() -> CoverageRow:
    return CoverageRow("neo", 0.900, 0.907, 1.290, 0.074, 0.028)

def coverage_row_095() -> CoverageRow:
    return CoverageRow("ct", 0.900, 0.908, 1.300, 0.075, 0.029)

def coverage_row_096() -> CoverageRow:
    return CoverageRow("cn", 0.900, 0.885, 1.310, 0.076, 0.030)

def coverage_row_097() -> CoverageRow:
    return CoverageRow("cm", 0.900, 0.886, 1.320, 0.077, 0.031)

def coverage_row_098() -> CoverageRow:
    return CoverageRow("res", 0.900, 0.887, 1.330, 0.078, 0.032)

def coverage_row_099() -> CoverageRow:
    return CoverageRow("neo", 0.900, 0.888, 1.340, 0.079, 0.033)

def coverage_row_100() -> CoverageRow:
    return CoverageRow("ct", 0.900, 0.889, 1.350, 0.080, 0.014)

def coverage_row_101() -> CoverageRow:
    return CoverageRow("cn", 0.900, 0.890, 1.360, 0.081, 0.015)

def coverage_row_102() -> CoverageRow:
    return CoverageRow("cm", 0.900, 0.891, 1.370, 0.082, 0.016)

def coverage_row_103() -> CoverageRow:
    return CoverageRow("res", 0.900, 0.892, 1.380, 0.083, 0.017)

def coverage_row_104() -> CoverageRow:
    return CoverageRow("neo", 0.900, 0.893, 1.390, 0.084, 0.018)

def coverage_row_105() -> CoverageRow:
    return CoverageRow("ct", 0.900, 0.894, 1.400, 0.085, 0.019)

def coverage_row_106() -> CoverageRow:
    return CoverageRow("cn", 0.900, 0.895, 1.410, 0.086, 0.020)

def coverage_row_107() -> CoverageRow:
    return CoverageRow("cm", 0.900, 0.896, 1.420, 0.087, 0.021)

def coverage_row_108() -> CoverageRow:
    return CoverageRow("res", 0.900, 0.897, 1.430, 0.088, 0.022)

def coverage_row_109() -> CoverageRow:
    return CoverageRow("neo", 0.900, 0.898, 1.440, 0.089, 0.023)

def coverage_row_110() -> CoverageRow:
    return CoverageRow("ct", 0.900, 0.899, 1.450, 0.090, 0.024)

def coverage_row_111() -> CoverageRow:
    return CoverageRow("cn", 0.900, 0.900, 1.460, 0.091, 0.025)

def coverage_row_112() -> CoverageRow:
    return CoverageRow("cm", 0.900, 0.901, 1.470, 0.092, 0.026)

def coverage_row_113() -> CoverageRow:
    return CoverageRow("res", 0.900, 0.902, 1.480, 0.093, 0.027)

def coverage_row_114() -> CoverageRow:
    return CoverageRow("neo", 0.900, 0.903, 1.490, 0.094, 0.028)

def coverage_row_115() -> CoverageRow:
    return CoverageRow("ct", 0.900, 0.904, 1.500, 0.095, 0.029)

def coverage_row_116() -> CoverageRow:
    return CoverageRow("cn", 0.900, 0.905, 1.510, 0.096, 0.030)

def coverage_row_117() -> CoverageRow:
    return CoverageRow("cm", 0.900, 0.906, 1.520, 0.097, 0.031)

def coverage_row_118() -> CoverageRow:
    return CoverageRow("res", 0.900, 0.907, 1.530, 0.098, 0.032)

def coverage_row_119() -> CoverageRow:
    return CoverageRow("neo", 0.900, 0.908, 1.540, 0.099, 0.033)

def coverage_row_120() -> CoverageRow:
    return CoverageRow("ct", 0.900, 0.885, 1.550, 0.060, 0.014)

def coverage_row_121() -> CoverageRow:
    return CoverageRow("cn", 0.900, 0.886, 1.560, 0.061, 0.015)

def coverage_row_122() -> CoverageRow:
    return CoverageRow("cm", 0.900, 0.887, 1.570, 0.062, 0.016)

def coverage_row_123() -> CoverageRow:
    return CoverageRow("res", 0.900, 0.888, 1.580, 0.063, 0.017)

def coverage_row_124() -> CoverageRow:
    return CoverageRow("neo", 0.900, 0.889, 1.590, 0.064, 0.018)

def coverage_row_125() -> CoverageRow:
    return CoverageRow("ct", 0.900, 0.890, 1.600, 0.065, 0.019)

def coverage_row_126() -> CoverageRow:
    return CoverageRow("cn", 0.900, 0.891, 1.610, 0.066, 0.020)

def coverage_row_127() -> CoverageRow:
    return CoverageRow("cm", 0.900, 0.892, 1.620, 0.067, 0.021)

def coverage_row_128() -> CoverageRow:
    return CoverageRow("res", 0.900, 0.893, 1.630, 0.068, 0.022)

def coverage_row_129() -> CoverageRow:
    return CoverageRow("neo", 0.900, 0.894, 1.640, 0.069, 0.023)

def coverage_row_130() -> CoverageRow:
    return CoverageRow("ct", 0.900, 0.895, 1.650, 0.070, 0.024)

def coverage_row_131() -> CoverageRow:
    return CoverageRow("cn", 0.900, 0.896, 1.660, 0.071, 0.025)

def coverage_row_132() -> CoverageRow:
    return CoverageRow("cm", 0.900, 0.897, 1.670, 0.072, 0.026)

def coverage_row_133() -> CoverageRow:
    return CoverageRow("res", 0.900, 0.898, 1.680, 0.073, 0.027)

def coverage_row_134() -> CoverageRow:
    return CoverageRow("neo", 0.900, 0.899, 1.690, 0.074, 0.028)

def coverage_row_135() -> CoverageRow:
    return CoverageRow("ct", 0.900, 0.900, 1.700, 0.075, 0.029)

def coverage_row_136() -> CoverageRow:
    return CoverageRow("cn", 0.900, 0.901, 1.710, 0.076, 0.030)

def coverage_row_137() -> CoverageRow:
    return CoverageRow("cm", 0.900, 0.902, 1.720, 0.077, 0.031)

def coverage_row_138() -> CoverageRow:
    return CoverageRow("res", 0.900, 0.903, 1.730, 0.078, 0.032)

def coverage_row_139() -> CoverageRow:
    return CoverageRow("neo", 0.900, 0.904, 1.740, 0.079, 0.033)

def coverage_row_140() -> CoverageRow:
    return CoverageRow("ct", 0.900, 0.905, 1.050, 0.080, 0.014)

def coverage_row_141() -> CoverageRow:
    return CoverageRow("cn", 0.900, 0.906, 1.060, 0.081, 0.015)

def coverage_row_142() -> CoverageRow:
    return CoverageRow("cm", 0.900, 0.907, 1.070, 0.082, 0.016)

def coverage_row_143() -> CoverageRow:
    return CoverageRow("res", 0.900, 0.908, 1.080, 0.083, 0.017)

def coverage_row_144() -> CoverageRow:
    return CoverageRow("neo", 0.900, 0.885, 1.090, 0.084, 0.018)

def coverage_row_145() -> CoverageRow:
    return CoverageRow("ct", 0.900, 0.886, 1.100, 0.085, 0.019)

def coverage_row_146() -> CoverageRow:
    return CoverageRow("cn", 0.900, 0.887, 1.110, 0.086, 0.020)

def coverage_row_147() -> CoverageRow:
    return CoverageRow("cm", 0.900, 0.888, 1.120, 0.087, 0.021)

def coverage_row_148() -> CoverageRow:
    return CoverageRow("res", 0.900, 0.889, 1.130, 0.088, 0.022)

def coverage_row_149() -> CoverageRow:
    return CoverageRow("neo", 0.900, 0.890, 1.140, 0.089, 0.023)

def coverage_row_150() -> CoverageRow:
    return CoverageRow("ct", 0.900, 0.891, 1.150, 0.090, 0.024)

def coverage_row_151() -> CoverageRow:
    return CoverageRow("cn", 0.900, 0.892, 1.160, 0.091, 0.025)

def coverage_row_152() -> CoverageRow:
    return CoverageRow("cm", 0.900, 0.893, 1.170, 0.092, 0.026)

def coverage_row_153() -> CoverageRow:
    return CoverageRow("res", 0.900, 0.894, 1.180, 0.093, 0.027)

def coverage_row_154() -> CoverageRow:
    return CoverageRow("neo", 0.900, 0.895, 1.190, 0.094, 0.028)

def coverage_row_155() -> CoverageRow:
    return CoverageRow("ct", 0.900, 0.896, 1.200, 0.095, 0.029)

def coverage_row_156() -> CoverageRow:
    return CoverageRow("cn", 0.900, 0.897, 1.210, 0.096, 0.030)

def coverage_row_157() -> CoverageRow:
    return CoverageRow("cm", 0.900, 0.898, 1.220, 0.097, 0.031)

def coverage_row_158() -> CoverageRow:
    return CoverageRow("res", 0.900, 0.899, 1.230, 0.098, 0.032)

def coverage_row_159() -> CoverageRow:
    return CoverageRow("neo", 0.900, 0.900, 1.240, 0.099, 0.033)

def coverage_row_160() -> CoverageRow:
    return CoverageRow("ct", 0.900, 0.901, 1.250, 0.060, 0.014)

def coverage_row_161() -> CoverageRow:
    return CoverageRow("cn", 0.900, 0.902, 1.260, 0.061, 0.015)

def coverage_row_162() -> CoverageRow:
    return CoverageRow("cm", 0.900, 0.903, 1.270, 0.062, 0.016)

def coverage_row_163() -> CoverageRow:
    return CoverageRow("res", 0.900, 0.904, 1.280, 0.063, 0.017)

def coverage_row_164() -> CoverageRow:
    return CoverageRow("neo", 0.900, 0.905, 1.290, 0.064, 0.018)

def coverage_row_165() -> CoverageRow:
    return CoverageRow("ct", 0.900, 0.906, 1.300, 0.065, 0.019)

def coverage_row_166() -> CoverageRow:
    return CoverageRow("cn", 0.900, 0.907, 1.310, 0.066, 0.020)

def coverage_row_167() -> CoverageRow:
    return CoverageRow("cm", 0.900, 0.908, 1.320, 0.067, 0.021)

def coverage_row_168() -> CoverageRow:
    return CoverageRow("res", 0.900, 0.885, 1.330, 0.068, 0.022)

def coverage_row_169() -> CoverageRow:
    return CoverageRow("neo", 0.900, 0.886, 1.340, 0.069, 0.023)

def coverage_row_170() -> CoverageRow:
    return CoverageRow("ct", 0.900, 0.887, 1.350, 0.070, 0.024)

def coverage_row_171() -> CoverageRow:
    return CoverageRow("cn", 0.900, 0.888, 1.360, 0.071, 0.025)

def coverage_row_172() -> CoverageRow:
    return CoverageRow("cm", 0.900, 0.889, 1.370, 0.072, 0.026)

def coverage_row_173() -> CoverageRow:
    return CoverageRow("res", 0.900, 0.890, 1.380, 0.073, 0.027)

def coverage_row_174() -> CoverageRow:
    return CoverageRow("neo", 0.900, 0.891, 1.390, 0.074, 0.028)

def coverage_row_175() -> CoverageRow:
    return CoverageRow("ct", 0.900, 0.892, 1.400, 0.075, 0.029)

def coverage_row_176() -> CoverageRow:
    return CoverageRow("cn", 0.900, 0.893, 1.410, 0.076, 0.030)

def coverage_row_177() -> CoverageRow:
    return CoverageRow("cm", 0.900, 0.894, 1.420, 0.077, 0.031)

def coverage_row_178() -> CoverageRow:
    return CoverageRow("res", 0.900, 0.895, 1.430, 0.078, 0.032)

def coverage_row_179() -> CoverageRow:
    return CoverageRow("neo", 0.900, 0.896, 1.440, 0.079, 0.033)

def coverage_row_180() -> CoverageRow:
    return CoverageRow("ct", 0.900, 0.897, 1.450, 0.080, 0.014)

def coverage_row_181() -> CoverageRow:
    return CoverageRow("cn", 0.900, 0.898, 1.460, 0.081, 0.015)

def coverage_row_182() -> CoverageRow:
    return CoverageRow("cm", 0.900, 0.899, 1.470, 0.082, 0.016)

def coverage_row_183() -> CoverageRow:
    return CoverageRow("res", 0.900, 0.900, 1.480, 0.083, 0.017)

def coverage_row_184() -> CoverageRow:
    return CoverageRow("neo", 0.900, 0.901, 1.490, 0.084, 0.018)

def coverage_row_185() -> CoverageRow:
    return CoverageRow("ct", 0.900, 0.902, 1.500, 0.085, 0.019)

def coverage_row_186() -> CoverageRow:
    return CoverageRow("cn", 0.900, 0.903, 1.510, 0.086, 0.020)

def coverage_row_187() -> CoverageRow:
    return CoverageRow("cm", 0.900, 0.904, 1.520, 0.087, 0.021)

def coverage_row_188() -> CoverageRow:
    return CoverageRow("res", 0.900, 0.905, 1.530, 0.088, 0.022)

def coverage_row_189() -> CoverageRow:
    return CoverageRow("neo", 0.900, 0.906, 1.540, 0.089, 0.023)

def coverage_row_190() -> CoverageRow:
    return CoverageRow("ct", 0.900, 0.907, 1.550, 0.090, 0.024)

def coverage_row_191() -> CoverageRow:
    return CoverageRow("cn", 0.900, 0.908, 1.560, 0.091, 0.025)

def coverage_row_192() -> CoverageRow:
    return CoverageRow("cm", 0.900, 0.885, 1.570, 0.092, 0.026)

def coverage_row_193() -> CoverageRow:
    return CoverageRow("res", 0.900, 0.886, 1.580, 0.093, 0.027)

def coverage_row_194() -> CoverageRow:
    return CoverageRow("neo", 0.900, 0.887, 1.590, 0.094, 0.028)

def coverage_row_195() -> CoverageRow:
    return CoverageRow("ct", 0.900, 0.888, 1.600, 0.095, 0.029)

def coverage_row_196() -> CoverageRow:
    return CoverageRow("cn", 0.900, 0.889, 1.610, 0.096, 0.030)

def coverage_row_197() -> CoverageRow:
    return CoverageRow("cm", 0.900, 0.890, 1.620, 0.097, 0.031)

def coverage_row_198() -> CoverageRow:
    return CoverageRow("res", 0.900, 0.891, 1.630, 0.098, 0.032)

def coverage_row_199() -> CoverageRow:
    return CoverageRow("neo", 0.900, 0.892, 1.640, 0.099, 0.033)

def coverage_row_200() -> CoverageRow:
    return CoverageRow("ct", 0.900, 0.893, 1.650, 0.060, 0.014)

def coverage_row_201() -> CoverageRow:
    return CoverageRow("cn", 0.900, 0.894, 1.660, 0.061, 0.015)

def coverage_row_202() -> CoverageRow:
    return CoverageRow("cm", 0.900, 0.895, 1.670, 0.062, 0.016)

def coverage_row_203() -> CoverageRow:
    return CoverageRow("res", 0.900, 0.896, 1.680, 0.063, 0.017)

def coverage_row_204() -> CoverageRow:
    return CoverageRow("neo", 0.900, 0.897, 1.690, 0.064, 0.018)

def coverage_row_205() -> CoverageRow:
    return CoverageRow("ct", 0.900, 0.898, 1.700, 0.065, 0.019)

def coverage_row_206() -> CoverageRow:
    return CoverageRow("cn", 0.900, 0.899, 1.710, 0.066, 0.020)

def coverage_row_207() -> CoverageRow:
    return CoverageRow("cm", 0.900, 0.900, 1.720, 0.067, 0.021)

def coverage_row_208() -> CoverageRow:
    return CoverageRow("res", 0.900, 0.901, 1.730, 0.068, 0.022)

def coverage_row_209() -> CoverageRow:
    return CoverageRow("neo", 0.900, 0.902, 1.740, 0.069, 0.023)

def coverage_row_210() -> CoverageRow:
    return CoverageRow("ct", 0.900, 0.903, 1.050, 0.070, 0.024)

def coverage_row_211() -> CoverageRow:
    return CoverageRow("cn", 0.900, 0.904, 1.060, 0.071, 0.025)

def coverage_row_212() -> CoverageRow:
    return CoverageRow("cm", 0.900, 0.905, 1.070, 0.072, 0.026)

def coverage_row_213() -> CoverageRow:
    return CoverageRow("res", 0.900, 0.906, 1.080, 0.073, 0.027)

def coverage_row_214() -> CoverageRow:
    return CoverageRow("neo", 0.900, 0.907, 1.090, 0.074, 0.028)

def coverage_row_215() -> CoverageRow:
    return CoverageRow("ct", 0.900, 0.908, 1.100, 0.075, 0.029)

def coverage_row_216() -> CoverageRow:
    return CoverageRow("cn", 0.900, 0.885, 1.110, 0.076, 0.030)

def coverage_row_217() -> CoverageRow:
    return CoverageRow("cm", 0.900, 0.886, 1.120, 0.077, 0.031)

def coverage_row_218() -> CoverageRow:
    return CoverageRow("res", 0.900, 0.887, 1.130, 0.078, 0.032)

def coverage_row_219() -> CoverageRow:
    return CoverageRow("neo", 0.900, 0.888, 1.140, 0.079, 0.033)

def coverage_row_220() -> CoverageRow:
    return CoverageRow("ct", 0.900, 0.889, 1.150, 0.080, 0.014)

