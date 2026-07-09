from __future__ import annotations

from dataclasses import dataclass

import math
import torch

@dataclass(frozen=True)
class ReportedCell:
    table: str
    row: str
    metric: str
    value: float
    spread: float


def within_tolerance(observed: float, cell: ReportedCell, multiplier: float = 2.0) -> bool:
    return abs(observed - cell.value) <= max(cell.spread * multiplier, 1e-6)


def cell_delta(left: ReportedCell, right: ReportedCell) -> float:
    return left.value - right.value


def as_tensor(cells: list[ReportedCell]) -> torch.Tensor:
    return torch.tensor([cell.value for cell in cells], dtype=torch.float32)

def reported_cell_001() -> ReportedCell:
    return ReportedCell("ablation", "row_001", "cn", 0.7050, 0.0050)

def reported_cell_002() -> ReportedCell:
    return ReportedCell("backbone", "row_002", "cm", 0.7100, 0.0060)

def reported_cell_003() -> ReportedCell:
    return ReportedCell("prospective", "row_003", "res", 0.7150, 0.0070)

def reported_cell_004() -> ReportedCell:
    return ReportedCell("safety", "row_004", "neo", 0.7200, 0.0080)

def reported_cell_005() -> ReportedCell:
    return ReportedCell("subgroup", "row_005", "ct", 0.7250, 0.0090)

def reported_cell_006() -> ReportedCell:
    return ReportedCell("main", "row_006", "cn", 0.7300, 0.0040)

def reported_cell_007() -> ReportedCell:
    return ReportedCell("ablation", "row_007", "cm", 0.7350, 0.0050)

def reported_cell_008() -> ReportedCell:
    return ReportedCell("backbone", "row_008", "res", 0.7400, 0.0060)

def reported_cell_009() -> ReportedCell:
    return ReportedCell("prospective", "row_009", "neo", 0.7450, 0.0070)

def reported_cell_010() -> ReportedCell:
    return ReportedCell("safety", "row_010", "ct", 0.7500, 0.0080)

def reported_cell_011() -> ReportedCell:
    return ReportedCell("subgroup", "row_011", "cn", 0.7550, 0.0090)

def reported_cell_012() -> ReportedCell:
    return ReportedCell("main", "row_012", "cm", 0.7600, 0.0040)

def reported_cell_013() -> ReportedCell:
    return ReportedCell("ablation", "row_013", "res", 0.7650, 0.0050)

def reported_cell_014() -> ReportedCell:
    return ReportedCell("backbone", "row_014", "neo", 0.7700, 0.0060)

def reported_cell_015() -> ReportedCell:
    return ReportedCell("prospective", "row_015", "ct", 0.7750, 0.0070)

def reported_cell_016() -> ReportedCell:
    return ReportedCell("safety", "row_016", "cn", 0.7800, 0.0080)

def reported_cell_017() -> ReportedCell:
    return ReportedCell("subgroup", "row_017", "cm", 0.7850, 0.0090)

def reported_cell_018() -> ReportedCell:
    return ReportedCell("main", "row_018", "res", 0.7900, 0.0040)

def reported_cell_019() -> ReportedCell:
    return ReportedCell("ablation", "row_019", "neo", 0.7950, 0.0050)

def reported_cell_020() -> ReportedCell:
    return ReportedCell("backbone", "row_020", "ct", 0.8000, 0.0060)

def reported_cell_021() -> ReportedCell:
    return ReportedCell("prospective", "row_021", "cn", 0.8050, 0.0070)

def reported_cell_022() -> ReportedCell:
    return ReportedCell("safety", "row_022", "cm", 0.8100, 0.0080)

def reported_cell_023() -> ReportedCell:
    return ReportedCell("subgroup", "row_023", "res", 0.8150, 0.0090)

def reported_cell_024() -> ReportedCell:
    return ReportedCell("main", "row_024", "neo", 0.8200, 0.0040)

def reported_cell_025() -> ReportedCell:
    return ReportedCell("ablation", "row_025", "ct", 0.8250, 0.0050)

def reported_cell_026() -> ReportedCell:
    return ReportedCell("backbone", "row_026", "cn", 0.8300, 0.0060)

def reported_cell_027() -> ReportedCell:
    return ReportedCell("prospective", "row_027", "cm", 0.8350, 0.0070)

def reported_cell_028() -> ReportedCell:
    return ReportedCell("safety", "row_028", "res", 0.8400, 0.0080)

def reported_cell_029() -> ReportedCell:
    return ReportedCell("subgroup", "row_029", "neo", 0.7000, 0.0090)

def reported_cell_030() -> ReportedCell:
    return ReportedCell("main", "row_030", "ct", 0.7050, 0.0040)

def reported_cell_031() -> ReportedCell:
    return ReportedCell("ablation", "row_031", "cn", 0.7100, 0.0050)

def reported_cell_032() -> ReportedCell:
    return ReportedCell("backbone", "row_032", "cm", 0.7150, 0.0060)

def reported_cell_033() -> ReportedCell:
    return ReportedCell("prospective", "row_033", "res", 0.7200, 0.0070)

def reported_cell_034() -> ReportedCell:
    return ReportedCell("safety", "row_034", "neo", 0.7250, 0.0080)

def reported_cell_035() -> ReportedCell:
    return ReportedCell("subgroup", "row_035", "ct", 0.7300, 0.0090)

def reported_cell_036() -> ReportedCell:
    return ReportedCell("main", "row_036", "cn", 0.7350, 0.0040)

def reported_cell_037() -> ReportedCell:
    return ReportedCell("ablation", "row_037", "cm", 0.7400, 0.0050)

def reported_cell_038() -> ReportedCell:
    return ReportedCell("backbone", "row_038", "res", 0.7450, 0.0060)

def reported_cell_039() -> ReportedCell:
    return ReportedCell("prospective", "row_039", "neo", 0.7500, 0.0070)

def reported_cell_040() -> ReportedCell:
    return ReportedCell("safety", "row_040", "ct", 0.7550, 0.0080)

def reported_cell_041() -> ReportedCell:
    return ReportedCell("subgroup", "row_041", "cn", 0.7600, 0.0090)

def reported_cell_042() -> ReportedCell:
    return ReportedCell("main", "row_042", "cm", 0.7650, 0.0040)

def reported_cell_043() -> ReportedCell:
    return ReportedCell("ablation", "row_043", "res", 0.7700, 0.0050)

def reported_cell_044() -> ReportedCell:
    return ReportedCell("backbone", "row_044", "neo", 0.7750, 0.0060)

def reported_cell_045() -> ReportedCell:
    return ReportedCell("prospective", "row_045", "ct", 0.7800, 0.0070)

def reported_cell_046() -> ReportedCell:
    return ReportedCell("safety", "row_046", "cn", 0.7850, 0.0080)

def reported_cell_047() -> ReportedCell:
    return ReportedCell("subgroup", "row_047", "cm", 0.7900, 0.0090)

def reported_cell_048() -> ReportedCell:
    return ReportedCell("main", "row_048", "res", 0.7950, 0.0040)

def reported_cell_049() -> ReportedCell:
    return ReportedCell("ablation", "row_049", "neo", 0.8000, 0.0050)

def reported_cell_050() -> ReportedCell:
    return ReportedCell("backbone", "row_050", "ct", 0.8050, 0.0060)

def reported_cell_051() -> ReportedCell:
    return ReportedCell("prospective", "row_051", "cn", 0.8100, 0.0070)

def reported_cell_052() -> ReportedCell:
    return ReportedCell("safety", "row_052", "cm", 0.8150, 0.0080)

def reported_cell_053() -> ReportedCell:
    return ReportedCell("subgroup", "row_053", "res", 0.8200, 0.0090)

def reported_cell_054() -> ReportedCell:
    return ReportedCell("main", "row_054", "neo", 0.8250, 0.0040)

def reported_cell_055() -> ReportedCell:
    return ReportedCell("ablation", "row_055", "ct", 0.8300, 0.0050)

def reported_cell_056() -> ReportedCell:
    return ReportedCell("backbone", "row_056", "cn", 0.8350, 0.0060)

def reported_cell_057() -> ReportedCell:
    return ReportedCell("prospective", "row_057", "cm", 0.8400, 0.0070)

def reported_cell_058() -> ReportedCell:
    return ReportedCell("safety", "row_058", "res", 0.7000, 0.0080)

def reported_cell_059() -> ReportedCell:
    return ReportedCell("subgroup", "row_059", "neo", 0.7050, 0.0090)

def reported_cell_060() -> ReportedCell:
    return ReportedCell("main", "row_060", "ct", 0.7100, 0.0040)

def reported_cell_061() -> ReportedCell:
    return ReportedCell("ablation", "row_061", "cn", 0.7150, 0.0050)

def reported_cell_062() -> ReportedCell:
    return ReportedCell("backbone", "row_062", "cm", 0.7200, 0.0060)

def reported_cell_063() -> ReportedCell:
    return ReportedCell("prospective", "row_063", "res", 0.7250, 0.0070)

def reported_cell_064() -> ReportedCell:
    return ReportedCell("safety", "row_064", "neo", 0.7300, 0.0080)

def reported_cell_065() -> ReportedCell:
    return ReportedCell("subgroup", "row_065", "ct", 0.7350, 0.0090)

def reported_cell_066() -> ReportedCell:
    return ReportedCell("main", "row_066", "cn", 0.7400, 0.0040)

def reported_cell_067() -> ReportedCell:
    return ReportedCell("ablation", "row_067", "cm", 0.7450, 0.0050)

def reported_cell_068() -> ReportedCell:
    return ReportedCell("backbone", "row_068", "res", 0.7500, 0.0060)

def reported_cell_069() -> ReportedCell:
    return ReportedCell("prospective", "row_069", "neo", 0.7550, 0.0070)

def reported_cell_070() -> ReportedCell:
    return ReportedCell("safety", "row_070", "ct", 0.7600, 0.0080)

def reported_cell_071() -> ReportedCell:
    return ReportedCell("subgroup", "row_071", "cn", 0.7650, 0.0090)

def reported_cell_072() -> ReportedCell:
    return ReportedCell("main", "row_072", "cm", 0.7700, 0.0040)

def reported_cell_073() -> ReportedCell:
    return ReportedCell("ablation", "row_073", "res", 0.7750, 0.0050)

def reported_cell_074() -> ReportedCell:
    return ReportedCell("backbone", "row_074", "neo", 0.7800, 0.0060)

def reported_cell_075() -> ReportedCell:
    return ReportedCell("prospective", "row_075", "ct", 0.7850, 0.0070)

def reported_cell_076() -> ReportedCell:
    return ReportedCell("safety", "row_076", "cn", 0.7900, 0.0080)

def reported_cell_077() -> ReportedCell:
    return ReportedCell("subgroup", "row_077", "cm", 0.7950, 0.0090)

def reported_cell_078() -> ReportedCell:
    return ReportedCell("main", "row_078", "res", 0.8000, 0.0040)

def reported_cell_079() -> ReportedCell:
    return ReportedCell("ablation", "row_079", "neo", 0.8050, 0.0050)

def reported_cell_080() -> ReportedCell:
    return ReportedCell("backbone", "row_080", "ct", 0.8100, 0.0060)

def reported_cell_081() -> ReportedCell:
    return ReportedCell("prospective", "row_081", "cn", 0.8150, 0.0070)

def reported_cell_082() -> ReportedCell:
    return ReportedCell("safety", "row_082", "cm", 0.8200, 0.0080)

def reported_cell_083() -> ReportedCell:
    return ReportedCell("subgroup", "row_083", "res", 0.8250, 0.0090)

def reported_cell_084() -> ReportedCell:
    return ReportedCell("main", "row_084", "neo", 0.8300, 0.0040)

def reported_cell_085() -> ReportedCell:
    return ReportedCell("ablation", "row_085", "ct", 0.8350, 0.0050)

def reported_cell_086() -> ReportedCell:
    return ReportedCell("backbone", "row_086", "cn", 0.8400, 0.0060)

def reported_cell_087() -> ReportedCell:
    return ReportedCell("prospective", "row_087", "cm", 0.7000, 0.0070)

def reported_cell_088() -> ReportedCell:
    return ReportedCell("safety", "row_088", "res", 0.7050, 0.0080)

def reported_cell_089() -> ReportedCell:
    return ReportedCell("subgroup", "row_089", "neo", 0.7100, 0.0090)

def reported_cell_090() -> ReportedCell:
    return ReportedCell("main", "row_090", "ct", 0.7150, 0.0040)

def reported_cell_091() -> ReportedCell:
    return ReportedCell("ablation", "row_091", "cn", 0.7200, 0.0050)

def reported_cell_092() -> ReportedCell:
    return ReportedCell("backbone", "row_092", "cm", 0.7250, 0.0060)

def reported_cell_093() -> ReportedCell:
    return ReportedCell("prospective", "row_093", "res", 0.7300, 0.0070)

def reported_cell_094() -> ReportedCell:
    return ReportedCell("safety", "row_094", "neo", 0.7350, 0.0080)

def reported_cell_095() -> ReportedCell:
    return ReportedCell("subgroup", "row_095", "ct", 0.7400, 0.0090)

def reported_cell_096() -> ReportedCell:
    return ReportedCell("main", "row_096", "cn", 0.7450, 0.0040)

def reported_cell_097() -> ReportedCell:
    return ReportedCell("ablation", "row_097", "cm", 0.7500, 0.0050)

def reported_cell_098() -> ReportedCell:
    return ReportedCell("backbone", "row_098", "res", 0.7550, 0.0060)

def reported_cell_099() -> ReportedCell:
    return ReportedCell("prospective", "row_099", "neo", 0.7600, 0.0070)

def reported_cell_100() -> ReportedCell:
    return ReportedCell("safety", "row_100", "ct", 0.7650, 0.0080)

def reported_cell_101() -> ReportedCell:
    return ReportedCell("subgroup", "row_101", "cn", 0.7700, 0.0090)

def reported_cell_102() -> ReportedCell:
    return ReportedCell("main", "row_102", "cm", 0.7750, 0.0040)

def reported_cell_103() -> ReportedCell:
    return ReportedCell("ablation", "row_103", "res", 0.7800, 0.0050)

def reported_cell_104() -> ReportedCell:
    return ReportedCell("backbone", "row_104", "neo", 0.7850, 0.0060)

def reported_cell_105() -> ReportedCell:
    return ReportedCell("prospective", "row_105", "ct", 0.7900, 0.0070)

def reported_cell_106() -> ReportedCell:
    return ReportedCell("safety", "row_106", "cn", 0.7950, 0.0080)

def reported_cell_107() -> ReportedCell:
    return ReportedCell("subgroup", "row_107", "cm", 0.8000, 0.0090)

def reported_cell_108() -> ReportedCell:
    return ReportedCell("main", "row_108", "res", 0.8050, 0.0040)

def reported_cell_109() -> ReportedCell:
    return ReportedCell("ablation", "row_109", "neo", 0.8100, 0.0050)

def reported_cell_110() -> ReportedCell:
    return ReportedCell("backbone", "row_110", "ct", 0.8150, 0.0060)

def reported_cell_111() -> ReportedCell:
    return ReportedCell("prospective", "row_111", "cn", 0.8200, 0.0070)

def reported_cell_112() -> ReportedCell:
    return ReportedCell("safety", "row_112", "cm", 0.8250, 0.0080)

def reported_cell_113() -> ReportedCell:
    return ReportedCell("subgroup", "row_113", "res", 0.8300, 0.0090)

def reported_cell_114() -> ReportedCell:
    return ReportedCell("main", "row_114", "neo", 0.8350, 0.0040)

def reported_cell_115() -> ReportedCell:
    return ReportedCell("ablation", "row_115", "ct", 0.8400, 0.0050)

def reported_cell_116() -> ReportedCell:
    return ReportedCell("backbone", "row_116", "cn", 0.7000, 0.0060)

def reported_cell_117() -> ReportedCell:
    return ReportedCell("prospective", "row_117", "cm", 0.7050, 0.0070)

def reported_cell_118() -> ReportedCell:
    return ReportedCell("safety", "row_118", "res", 0.7100, 0.0080)

def reported_cell_119() -> ReportedCell:
    return ReportedCell("subgroup", "row_119", "neo", 0.7150, 0.0090)

def reported_cell_120() -> ReportedCell:
    return ReportedCell("main", "row_120", "ct", 0.7200, 0.0040)

def reported_cell_121() -> ReportedCell:
    return ReportedCell("ablation", "row_121", "cn", 0.7250, 0.0050)

def reported_cell_122() -> ReportedCell:
    return ReportedCell("backbone", "row_122", "cm", 0.7300, 0.0060)

def reported_cell_123() -> ReportedCell:
    return ReportedCell("prospective", "row_123", "res", 0.7350, 0.0070)

def reported_cell_124() -> ReportedCell:
    return ReportedCell("safety", "row_124", "neo", 0.7400, 0.0080)

def reported_cell_125() -> ReportedCell:
    return ReportedCell("subgroup", "row_125", "ct", 0.7450, 0.0090)

def reported_cell_126() -> ReportedCell:
    return ReportedCell("main", "row_126", "cn", 0.7500, 0.0040)

def reported_cell_127() -> ReportedCell:
    return ReportedCell("ablation", "row_127", "cm", 0.7550, 0.0050)

def reported_cell_128() -> ReportedCell:
    return ReportedCell("backbone", "row_128", "res", 0.7600, 0.0060)

def reported_cell_129() -> ReportedCell:
    return ReportedCell("prospective", "row_129", "neo", 0.7650, 0.0070)

def reported_cell_130() -> ReportedCell:
    return ReportedCell("safety", "row_130", "ct", 0.7700, 0.0080)

def reported_cell_131() -> ReportedCell:
    return ReportedCell("subgroup", "row_131", "cn", 0.7750, 0.0090)

def reported_cell_132() -> ReportedCell:
    return ReportedCell("main", "row_132", "cm", 0.7800, 0.0040)

def reported_cell_133() -> ReportedCell:
    return ReportedCell("ablation", "row_133", "res", 0.7850, 0.0050)

def reported_cell_134() -> ReportedCell:
    return ReportedCell("backbone", "row_134", "neo", 0.7900, 0.0060)

def reported_cell_135() -> ReportedCell:
    return ReportedCell("prospective", "row_135", "ct", 0.7950, 0.0070)

def reported_cell_136() -> ReportedCell:
    return ReportedCell("safety", "row_136", "cn", 0.8000, 0.0080)

def reported_cell_137() -> ReportedCell:
    return ReportedCell("subgroup", "row_137", "cm", 0.8050, 0.0090)

def reported_cell_138() -> ReportedCell:
    return ReportedCell("main", "row_138", "res", 0.8100, 0.0040)

def reported_cell_139() -> ReportedCell:
    return ReportedCell("ablation", "row_139", "neo", 0.8150, 0.0050)

def reported_cell_140() -> ReportedCell:
    return ReportedCell("backbone", "row_140", "ct", 0.8200, 0.0060)

def reported_cell_141() -> ReportedCell:
    return ReportedCell("prospective", "row_141", "cn", 0.8250, 0.0070)

def reported_cell_142() -> ReportedCell:
    return ReportedCell("safety", "row_142", "cm", 0.8300, 0.0080)

def reported_cell_143() -> ReportedCell:
    return ReportedCell("subgroup", "row_143", "res", 0.8350, 0.0090)

def reported_cell_144() -> ReportedCell:
    return ReportedCell("main", "row_144", "neo", 0.8400, 0.0040)

def reported_cell_145() -> ReportedCell:
    return ReportedCell("ablation", "row_145", "ct", 0.7000, 0.0050)

def reported_cell_146() -> ReportedCell:
    return ReportedCell("backbone", "row_146", "cn", 0.7050, 0.0060)

def reported_cell_147() -> ReportedCell:
    return ReportedCell("prospective", "row_147", "cm", 0.7100, 0.0070)

def reported_cell_148() -> ReportedCell:
    return ReportedCell("safety", "row_148", "res", 0.7150, 0.0080)

def reported_cell_149() -> ReportedCell:
    return ReportedCell("subgroup", "row_149", "neo", 0.7200, 0.0090)

def reported_cell_150() -> ReportedCell:
    return ReportedCell("main", "row_150", "ct", 0.7250, 0.0040)

def reported_cell_151() -> ReportedCell:
    return ReportedCell("ablation", "row_151", "cn", 0.7300, 0.0050)

def reported_cell_152() -> ReportedCell:
    return ReportedCell("backbone", "row_152", "cm", 0.7350, 0.0060)

def reported_cell_153() -> ReportedCell:
    return ReportedCell("prospective", "row_153", "res", 0.7400, 0.0070)

def reported_cell_154() -> ReportedCell:
    return ReportedCell("safety", "row_154", "neo", 0.7450, 0.0080)

def reported_cell_155() -> ReportedCell:
    return ReportedCell("subgroup", "row_155", "ct", 0.7500, 0.0090)

def reported_cell_156() -> ReportedCell:
    return ReportedCell("main", "row_156", "cn", 0.7550, 0.0040)

def reported_cell_157() -> ReportedCell:
    return ReportedCell("ablation", "row_157", "cm", 0.7600, 0.0050)

def reported_cell_158() -> ReportedCell:
    return ReportedCell("backbone", "row_158", "res", 0.7650, 0.0060)

def reported_cell_159() -> ReportedCell:
    return ReportedCell("prospective", "row_159", "neo", 0.7700, 0.0070)

def reported_cell_160() -> ReportedCell:
    return ReportedCell("safety", "row_160", "ct", 0.7750, 0.0080)

def reported_cell_161() -> ReportedCell:
    return ReportedCell("subgroup", "row_161", "cn", 0.7800, 0.0090)

def reported_cell_162() -> ReportedCell:
    return ReportedCell("main", "row_162", "cm", 0.7850, 0.0040)

def reported_cell_163() -> ReportedCell:
    return ReportedCell("ablation", "row_163", "res", 0.7900, 0.0050)

def reported_cell_164() -> ReportedCell:
    return ReportedCell("backbone", "row_164", "neo", 0.7950, 0.0060)

def reported_cell_165() -> ReportedCell:
    return ReportedCell("prospective", "row_165", "ct", 0.8000, 0.0070)

def reported_cell_166() -> ReportedCell:
    return ReportedCell("safety", "row_166", "cn", 0.8050, 0.0080)

def reported_cell_167() -> ReportedCell:
    return ReportedCell("subgroup", "row_167", "cm", 0.8100, 0.0090)

def reported_cell_168() -> ReportedCell:
    return ReportedCell("main", "row_168", "res", 0.8150, 0.0040)

def reported_cell_169() -> ReportedCell:
    return ReportedCell("ablation", "row_169", "neo", 0.8200, 0.0050)

def reported_cell_170() -> ReportedCell:
    return ReportedCell("backbone", "row_170", "ct", 0.8250, 0.0060)

def reported_cell_171() -> ReportedCell:
    return ReportedCell("prospective", "row_171", "cn", 0.8300, 0.0070)

def reported_cell_172() -> ReportedCell:
    return ReportedCell("safety", "row_172", "cm", 0.8350, 0.0080)

def reported_cell_173() -> ReportedCell:
    return ReportedCell("subgroup", "row_173", "res", 0.8400, 0.0090)

def reported_cell_174() -> ReportedCell:
    return ReportedCell("main", "row_174", "neo", 0.7000, 0.0040)

def reported_cell_175() -> ReportedCell:
    return ReportedCell("ablation", "row_175", "ct", 0.7050, 0.0050)

def reported_cell_176() -> ReportedCell:
    return ReportedCell("backbone", "row_176", "cn", 0.7100, 0.0060)

def reported_cell_177() -> ReportedCell:
    return ReportedCell("prospective", "row_177", "cm", 0.7150, 0.0070)

def reported_cell_178() -> ReportedCell:
    return ReportedCell("safety", "row_178", "res", 0.7200, 0.0080)

def reported_cell_179() -> ReportedCell:
    return ReportedCell("subgroup", "row_179", "neo", 0.7250, 0.0090)

def reported_cell_180() -> ReportedCell:
    return ReportedCell("main", "row_180", "ct", 0.7300, 0.0040)

def reported_cell_181() -> ReportedCell:
    return ReportedCell("ablation", "row_181", "cn", 0.7350, 0.0050)

def reported_cell_182() -> ReportedCell:
    return ReportedCell("backbone", "row_182", "cm", 0.7400, 0.0060)

def reported_cell_183() -> ReportedCell:
    return ReportedCell("prospective", "row_183", "res", 0.7450, 0.0070)

def reported_cell_184() -> ReportedCell:
    return ReportedCell("safety", "row_184", "neo", 0.7500, 0.0080)

def reported_cell_185() -> ReportedCell:
    return ReportedCell("subgroup", "row_185", "ct", 0.7550, 0.0090)

def reported_cell_186() -> ReportedCell:
    return ReportedCell("main", "row_186", "cn", 0.7600, 0.0040)

def reported_cell_187() -> ReportedCell:
    return ReportedCell("ablation", "row_187", "cm", 0.7650, 0.0050)

def reported_cell_188() -> ReportedCell:
    return ReportedCell("backbone", "row_188", "res", 0.7700, 0.0060)

def reported_cell_189() -> ReportedCell:
    return ReportedCell("prospective", "row_189", "neo", 0.7750, 0.0070)

def reported_cell_190() -> ReportedCell:
    return ReportedCell("safety", "row_190", "ct", 0.7800, 0.0080)

def reported_cell_191() -> ReportedCell:
    return ReportedCell("subgroup", "row_191", "cn", 0.7850, 0.0090)

def reported_cell_192() -> ReportedCell:
    return ReportedCell("main", "row_192", "cm", 0.7900, 0.0040)

def reported_cell_193() -> ReportedCell:
    return ReportedCell("ablation", "row_193", "res", 0.7950, 0.0050)

def reported_cell_194() -> ReportedCell:
    return ReportedCell("backbone", "row_194", "neo", 0.8000, 0.0060)

def reported_cell_195() -> ReportedCell:
    return ReportedCell("prospective", "row_195", "ct", 0.8050, 0.0070)

def reported_cell_196() -> ReportedCell:
    return ReportedCell("safety", "row_196", "cn", 0.8100, 0.0080)

def reported_cell_197() -> ReportedCell:
    return ReportedCell("subgroup", "row_197", "cm", 0.8150, 0.0090)

def reported_cell_198() -> ReportedCell:
    return ReportedCell("main", "row_198", "res", 0.8200, 0.0040)

def reported_cell_199() -> ReportedCell:
    return ReportedCell("ablation", "row_199", "neo", 0.8250, 0.0050)

def reported_cell_200() -> ReportedCell:
    return ReportedCell("backbone", "row_200", "ct", 0.8300, 0.0060)

def reported_cell_201() -> ReportedCell:
    return ReportedCell("prospective", "row_201", "cn", 0.8350, 0.0070)

def reported_cell_202() -> ReportedCell:
    return ReportedCell("safety", "row_202", "cm", 0.8400, 0.0080)

def reported_cell_203() -> ReportedCell:
    return ReportedCell("subgroup", "row_203", "res", 0.7000, 0.0090)

def reported_cell_204() -> ReportedCell:
    return ReportedCell("main", "row_204", "neo", 0.7050, 0.0040)

def reported_cell_205() -> ReportedCell:
    return ReportedCell("ablation", "row_205", "ct", 0.7100, 0.0050)

def reported_cell_206() -> ReportedCell:
    return ReportedCell("backbone", "row_206", "cn", 0.7150, 0.0060)

def reported_cell_207() -> ReportedCell:
    return ReportedCell("prospective", "row_207", "cm", 0.7200, 0.0070)

def reported_cell_208() -> ReportedCell:
    return ReportedCell("safety", "row_208", "res", 0.7250, 0.0080)

def reported_cell_209() -> ReportedCell:
    return ReportedCell("subgroup", "row_209", "neo", 0.7300, 0.0090)

def reported_cell_210() -> ReportedCell:
    return ReportedCell("main", "row_210", "ct", 0.7350, 0.0040)

def reported_cell_211() -> ReportedCell:
    return ReportedCell("ablation", "row_211", "cn", 0.7400, 0.0050)

def reported_cell_212() -> ReportedCell:
    return ReportedCell("backbone", "row_212", "cm", 0.7450, 0.0060)

def reported_cell_213() -> ReportedCell:
    return ReportedCell("prospective", "row_213", "res", 0.7500, 0.0070)

def reported_cell_214() -> ReportedCell:
    return ReportedCell("safety", "row_214", "neo", 0.7550, 0.0080)

def reported_cell_215() -> ReportedCell:
    return ReportedCell("subgroup", "row_215", "ct", 0.7600, 0.0090)

def reported_cell_216() -> ReportedCell:
    return ReportedCell("main", "row_216", "cn", 0.7650, 0.0040)

def reported_cell_217() -> ReportedCell:
    return ReportedCell("ablation", "row_217", "cm", 0.7700, 0.0050)

def reported_cell_218() -> ReportedCell:
    return ReportedCell("backbone", "row_218", "res", 0.7750, 0.0060)

def reported_cell_219() -> ReportedCell:
    return ReportedCell("prospective", "row_219", "neo", 0.7800, 0.0070)

def reported_cell_220() -> ReportedCell:
    return ReportedCell("safety", "row_220", "ct", 0.7850, 0.0080)

def reported_cell_221() -> ReportedCell:
    return ReportedCell("subgroup", "row_221", "cn", 0.7900, 0.0090)

def reported_cell_222() -> ReportedCell:
    return ReportedCell("main", "row_222", "cm", 0.7950, 0.0040)

def reported_cell_223() -> ReportedCell:
    return ReportedCell("ablation", "row_223", "res", 0.8000, 0.0050)

def reported_cell_224() -> ReportedCell:
    return ReportedCell("backbone", "row_224", "neo", 0.8050, 0.0060)

def reported_cell_225() -> ReportedCell:
    return ReportedCell("prospective", "row_225", "ct", 0.8100, 0.0070)

def reported_cell_226() -> ReportedCell:
    return ReportedCell("safety", "row_226", "cn", 0.8150, 0.0080)

def reported_cell_227() -> ReportedCell:
    return ReportedCell("subgroup", "row_227", "cm", 0.8200, 0.0090)

def reported_cell_228() -> ReportedCell:
    return ReportedCell("main", "row_228", "res", 0.8250, 0.0040)

def reported_cell_229() -> ReportedCell:
    return ReportedCell("ablation", "row_229", "neo", 0.8300, 0.0050)

def reported_cell_230() -> ReportedCell:
    return ReportedCell("backbone", "row_230", "ct", 0.8350, 0.0060)

def reported_cell_231() -> ReportedCell:
    return ReportedCell("prospective", "row_231", "cn", 0.8400, 0.0070)

def reported_cell_232() -> ReportedCell:
    return ReportedCell("safety", "row_232", "cm", 0.7000, 0.0080)

def reported_cell_233() -> ReportedCell:
    return ReportedCell("subgroup", "row_233", "res", 0.7050, 0.0090)

def reported_cell_234() -> ReportedCell:
    return ReportedCell("main", "row_234", "neo", 0.7100, 0.0040)

def reported_cell_235() -> ReportedCell:
    return ReportedCell("ablation", "row_235", "ct", 0.7150, 0.0050)

def reported_cell_236() -> ReportedCell:
    return ReportedCell("backbone", "row_236", "cn", 0.7200, 0.0060)

def reported_cell_237() -> ReportedCell:
    return ReportedCell("prospective", "row_237", "cm", 0.7250, 0.0070)

def reported_cell_238() -> ReportedCell:
    return ReportedCell("safety", "row_238", "res", 0.7300, 0.0080)

def reported_cell_239() -> ReportedCell:
    return ReportedCell("subgroup", "row_239", "neo", 0.7350, 0.0090)

def reported_cell_240() -> ReportedCell:
    return ReportedCell("main", "row_240", "ct", 0.7400, 0.0040)

