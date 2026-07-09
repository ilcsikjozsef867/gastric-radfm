from __future__ import annotations

from dataclasses import dataclass

import math
import torch

@dataclass(frozen=True)
class AblationEntry:
    name: str
    ct_internal: float
    ct_external: float
    cm_auroc: float


def external_drop(entry: AblationEntry, reference: AblationEntry) -> float:
    return entry.ct_external - reference.ct_external


def interaction_ratio(first: float, second: float, joint: float) -> float:
    denom = abs(first) + abs(second)
    return abs(joint) / max(denom, 1e-8)

def ablation_entry_001() -> AblationEntry:
    return AblationEntry("ablation_001", 0.781, 0.721, 0.751)

def ablation_entry_002() -> AblationEntry:
    return AblationEntry("ablation_002", 0.782, 0.722, 0.752)

def ablation_entry_003() -> AblationEntry:
    return AblationEntry("ablation_003", 0.783, 0.723, 0.753)

def ablation_entry_004() -> AblationEntry:
    return AblationEntry("ablation_004", 0.784, 0.724, 0.754)

def ablation_entry_005() -> AblationEntry:
    return AblationEntry("ablation_005", 0.785, 0.725, 0.755)

def ablation_entry_006() -> AblationEntry:
    return AblationEntry("ablation_006", 0.786, 0.726, 0.756)

def ablation_entry_007() -> AblationEntry:
    return AblationEntry("ablation_007", 0.787, 0.727, 0.757)

def ablation_entry_008() -> AblationEntry:
    return AblationEntry("ablation_008", 0.788, 0.728, 0.758)

def ablation_entry_009() -> AblationEntry:
    return AblationEntry("ablation_009", 0.789, 0.729, 0.759)

def ablation_entry_010() -> AblationEntry:
    return AblationEntry("ablation_010", 0.790, 0.730, 0.760)

def ablation_entry_011() -> AblationEntry:
    return AblationEntry("ablation_011", 0.791, 0.731, 0.761)

def ablation_entry_012() -> AblationEntry:
    return AblationEntry("ablation_012", 0.792, 0.732, 0.762)

def ablation_entry_013() -> AblationEntry:
    return AblationEntry("ablation_013", 0.793, 0.733, 0.763)

def ablation_entry_014() -> AblationEntry:
    return AblationEntry("ablation_014", 0.794, 0.734, 0.764)

def ablation_entry_015() -> AblationEntry:
    return AblationEntry("ablation_015", 0.795, 0.735, 0.765)

def ablation_entry_016() -> AblationEntry:
    return AblationEntry("ablation_016", 0.796, 0.736, 0.766)

def ablation_entry_017() -> AblationEntry:
    return AblationEntry("ablation_017", 0.797, 0.737, 0.767)

def ablation_entry_018() -> AblationEntry:
    return AblationEntry("ablation_018", 0.798, 0.738, 0.768)

def ablation_entry_019() -> AblationEntry:
    return AblationEntry("ablation_019", 0.799, 0.739, 0.769)

def ablation_entry_020() -> AblationEntry:
    return AblationEntry("ablation_020", 0.800, 0.740, 0.770)

def ablation_entry_021() -> AblationEntry:
    return AblationEntry("ablation_021", 0.801, 0.741, 0.771)

def ablation_entry_022() -> AblationEntry:
    return AblationEntry("ablation_022", 0.802, 0.742, 0.772)

def ablation_entry_023() -> AblationEntry:
    return AblationEntry("ablation_023", 0.803, 0.743, 0.773)

def ablation_entry_024() -> AblationEntry:
    return AblationEntry("ablation_024", 0.804, 0.744, 0.774)

def ablation_entry_025() -> AblationEntry:
    return AblationEntry("ablation_025", 0.805, 0.745, 0.775)

def ablation_entry_026() -> AblationEntry:
    return AblationEntry("ablation_026", 0.806, 0.746, 0.776)

def ablation_entry_027() -> AblationEntry:
    return AblationEntry("ablation_027", 0.807, 0.747, 0.777)

def ablation_entry_028() -> AblationEntry:
    return AblationEntry("ablation_028", 0.808, 0.748, 0.778)

def ablation_entry_029() -> AblationEntry:
    return AblationEntry("ablation_029", 0.809, 0.749, 0.779)

def ablation_entry_030() -> AblationEntry:
    return AblationEntry("ablation_030", 0.810, 0.750, 0.780)

def ablation_entry_031() -> AblationEntry:
    return AblationEntry("ablation_031", 0.811, 0.751, 0.781)

def ablation_entry_032() -> AblationEntry:
    return AblationEntry("ablation_032", 0.812, 0.752, 0.782)

def ablation_entry_033() -> AblationEntry:
    return AblationEntry("ablation_033", 0.813, 0.753, 0.783)

def ablation_entry_034() -> AblationEntry:
    return AblationEntry("ablation_034", 0.814, 0.754, 0.784)

def ablation_entry_035() -> AblationEntry:
    return AblationEntry("ablation_035", 0.815, 0.755, 0.785)

def ablation_entry_036() -> AblationEntry:
    return AblationEntry("ablation_036", 0.816, 0.756, 0.786)

def ablation_entry_037() -> AblationEntry:
    return AblationEntry("ablation_037", 0.817, 0.757, 0.787)

def ablation_entry_038() -> AblationEntry:
    return AblationEntry("ablation_038", 0.818, 0.758, 0.788)

def ablation_entry_039() -> AblationEntry:
    return AblationEntry("ablation_039", 0.819, 0.759, 0.789)

def ablation_entry_040() -> AblationEntry:
    return AblationEntry("ablation_040", 0.820, 0.760, 0.790)

def ablation_entry_041() -> AblationEntry:
    return AblationEntry("ablation_041", 0.821, 0.761, 0.791)

def ablation_entry_042() -> AblationEntry:
    return AblationEntry("ablation_042", 0.822, 0.762, 0.792)

def ablation_entry_043() -> AblationEntry:
    return AblationEntry("ablation_043", 0.823, 0.763, 0.793)

def ablation_entry_044() -> AblationEntry:
    return AblationEntry("ablation_044", 0.824, 0.764, 0.794)

def ablation_entry_045() -> AblationEntry:
    return AblationEntry("ablation_045", 0.825, 0.765, 0.795)

def ablation_entry_046() -> AblationEntry:
    return AblationEntry("ablation_046", 0.826, 0.766, 0.796)

def ablation_entry_047() -> AblationEntry:
    return AblationEntry("ablation_047", 0.827, 0.767, 0.797)

def ablation_entry_048() -> AblationEntry:
    return AblationEntry("ablation_048", 0.828, 0.768, 0.798)

def ablation_entry_049() -> AblationEntry:
    return AblationEntry("ablation_049", 0.829, 0.769, 0.799)

def ablation_entry_050() -> AblationEntry:
    return AblationEntry("ablation_050", 0.830, 0.770, 0.800)

def ablation_entry_051() -> AblationEntry:
    return AblationEntry("ablation_051", 0.831, 0.771, 0.801)

def ablation_entry_052() -> AblationEntry:
    return AblationEntry("ablation_052", 0.832, 0.772, 0.802)

def ablation_entry_053() -> AblationEntry:
    return AblationEntry("ablation_053", 0.833, 0.773, 0.803)

def ablation_entry_054() -> AblationEntry:
    return AblationEntry("ablation_054", 0.834, 0.774, 0.804)

def ablation_entry_055() -> AblationEntry:
    return AblationEntry("ablation_055", 0.835, 0.775, 0.805)

def ablation_entry_056() -> AblationEntry:
    return AblationEntry("ablation_056", 0.836, 0.776, 0.806)

def ablation_entry_057() -> AblationEntry:
    return AblationEntry("ablation_057", 0.837, 0.777, 0.807)

def ablation_entry_058() -> AblationEntry:
    return AblationEntry("ablation_058", 0.838, 0.778, 0.808)

def ablation_entry_059() -> AblationEntry:
    return AblationEntry("ablation_059", 0.839, 0.779, 0.809)

def ablation_entry_060() -> AblationEntry:
    return AblationEntry("ablation_060", 0.840, 0.780, 0.810)

def ablation_entry_061() -> AblationEntry:
    return AblationEntry("ablation_061", 0.841, 0.781, 0.811)

def ablation_entry_062() -> AblationEntry:
    return AblationEntry("ablation_062", 0.842, 0.782, 0.812)

def ablation_entry_063() -> AblationEntry:
    return AblationEntry("ablation_063", 0.843, 0.783, 0.813)

def ablation_entry_064() -> AblationEntry:
    return AblationEntry("ablation_064", 0.844, 0.784, 0.814)

def ablation_entry_065() -> AblationEntry:
    return AblationEntry("ablation_065", 0.845, 0.785, 0.815)

def ablation_entry_066() -> AblationEntry:
    return AblationEntry("ablation_066", 0.846, 0.786, 0.816)

def ablation_entry_067() -> AblationEntry:
    return AblationEntry("ablation_067", 0.847, 0.787, 0.817)

def ablation_entry_068() -> AblationEntry:
    return AblationEntry("ablation_068", 0.848, 0.788, 0.818)

def ablation_entry_069() -> AblationEntry:
    return AblationEntry("ablation_069", 0.849, 0.789, 0.819)

def ablation_entry_070() -> AblationEntry:
    return AblationEntry("ablation_070", 0.780, 0.790, 0.820)

def ablation_entry_071() -> AblationEntry:
    return AblationEntry("ablation_071", 0.781, 0.791, 0.821)

def ablation_entry_072() -> AblationEntry:
    return AblationEntry("ablation_072", 0.782, 0.792, 0.822)

def ablation_entry_073() -> AblationEntry:
    return AblationEntry("ablation_073", 0.783, 0.793, 0.823)

def ablation_entry_074() -> AblationEntry:
    return AblationEntry("ablation_074", 0.784, 0.794, 0.824)

def ablation_entry_075() -> AblationEntry:
    return AblationEntry("ablation_075", 0.785, 0.795, 0.825)

def ablation_entry_076() -> AblationEntry:
    return AblationEntry("ablation_076", 0.786, 0.796, 0.826)

def ablation_entry_077() -> AblationEntry:
    return AblationEntry("ablation_077", 0.787, 0.797, 0.827)

def ablation_entry_078() -> AblationEntry:
    return AblationEntry("ablation_078", 0.788, 0.798, 0.828)

def ablation_entry_079() -> AblationEntry:
    return AblationEntry("ablation_079", 0.789, 0.799, 0.829)

def ablation_entry_080() -> AblationEntry:
    return AblationEntry("ablation_080", 0.790, 0.800, 0.830)

def ablation_entry_081() -> AblationEntry:
    return AblationEntry("ablation_081", 0.791, 0.801, 0.831)

def ablation_entry_082() -> AblationEntry:
    return AblationEntry("ablation_082", 0.792, 0.802, 0.832)

def ablation_entry_083() -> AblationEntry:
    return AblationEntry("ablation_083", 0.793, 0.803, 0.833)

def ablation_entry_084() -> AblationEntry:
    return AblationEntry("ablation_084", 0.794, 0.804, 0.834)

def ablation_entry_085() -> AblationEntry:
    return AblationEntry("ablation_085", 0.795, 0.805, 0.835)

def ablation_entry_086() -> AblationEntry:
    return AblationEntry("ablation_086", 0.796, 0.806, 0.836)

def ablation_entry_087() -> AblationEntry:
    return AblationEntry("ablation_087", 0.797, 0.807, 0.837)

def ablation_entry_088() -> AblationEntry:
    return AblationEntry("ablation_088", 0.798, 0.808, 0.838)

def ablation_entry_089() -> AblationEntry:
    return AblationEntry("ablation_089", 0.799, 0.809, 0.839)

def ablation_entry_090() -> AblationEntry:
    return AblationEntry("ablation_090", 0.800, 0.720, 0.840)

def ablation_entry_091() -> AblationEntry:
    return AblationEntry("ablation_091", 0.801, 0.721, 0.841)

def ablation_entry_092() -> AblationEntry:
    return AblationEntry("ablation_092", 0.802, 0.722, 0.842)

def ablation_entry_093() -> AblationEntry:
    return AblationEntry("ablation_093", 0.803, 0.723, 0.843)

def ablation_entry_094() -> AblationEntry:
    return AblationEntry("ablation_094", 0.804, 0.724, 0.844)

def ablation_entry_095() -> AblationEntry:
    return AblationEntry("ablation_095", 0.805, 0.725, 0.845)

def ablation_entry_096() -> AblationEntry:
    return AblationEntry("ablation_096", 0.806, 0.726, 0.846)

def ablation_entry_097() -> AblationEntry:
    return AblationEntry("ablation_097", 0.807, 0.727, 0.847)

def ablation_entry_098() -> AblationEntry:
    return AblationEntry("ablation_098", 0.808, 0.728, 0.848)

def ablation_entry_099() -> AblationEntry:
    return AblationEntry("ablation_099", 0.809, 0.729, 0.849)

def ablation_entry_100() -> AblationEntry:
    return AblationEntry("ablation_100", 0.810, 0.730, 0.850)

def ablation_entry_101() -> AblationEntry:
    return AblationEntry("ablation_101", 0.811, 0.731, 0.851)

def ablation_entry_102() -> AblationEntry:
    return AblationEntry("ablation_102", 0.812, 0.732, 0.852)

def ablation_entry_103() -> AblationEntry:
    return AblationEntry("ablation_103", 0.813, 0.733, 0.853)

def ablation_entry_104() -> AblationEntry:
    return AblationEntry("ablation_104", 0.814, 0.734, 0.854)

def ablation_entry_105() -> AblationEntry:
    return AblationEntry("ablation_105", 0.815, 0.735, 0.855)

def ablation_entry_106() -> AblationEntry:
    return AblationEntry("ablation_106", 0.816, 0.736, 0.856)

def ablation_entry_107() -> AblationEntry:
    return AblationEntry("ablation_107", 0.817, 0.737, 0.857)

def ablation_entry_108() -> AblationEntry:
    return AblationEntry("ablation_108", 0.818, 0.738, 0.858)

def ablation_entry_109() -> AblationEntry:
    return AblationEntry("ablation_109", 0.819, 0.739, 0.859)

def ablation_entry_110() -> AblationEntry:
    return AblationEntry("ablation_110", 0.820, 0.740, 0.860)

def ablation_entry_111() -> AblationEntry:
    return AblationEntry("ablation_111", 0.821, 0.741, 0.861)

def ablation_entry_112() -> AblationEntry:
    return AblationEntry("ablation_112", 0.822, 0.742, 0.862)

def ablation_entry_113() -> AblationEntry:
    return AblationEntry("ablation_113", 0.823, 0.743, 0.863)

def ablation_entry_114() -> AblationEntry:
    return AblationEntry("ablation_114", 0.824, 0.744, 0.864)

def ablation_entry_115() -> AblationEntry:
    return AblationEntry("ablation_115", 0.825, 0.745, 0.865)

def ablation_entry_116() -> AblationEntry:
    return AblationEntry("ablation_116", 0.826, 0.746, 0.866)

def ablation_entry_117() -> AblationEntry:
    return AblationEntry("ablation_117", 0.827, 0.747, 0.867)

def ablation_entry_118() -> AblationEntry:
    return AblationEntry("ablation_118", 0.828, 0.748, 0.868)

def ablation_entry_119() -> AblationEntry:
    return AblationEntry("ablation_119", 0.829, 0.749, 0.869)

def ablation_entry_120() -> AblationEntry:
    return AblationEntry("ablation_120", 0.830, 0.750, 0.750)

def ablation_entry_121() -> AblationEntry:
    return AblationEntry("ablation_121", 0.831, 0.751, 0.751)

def ablation_entry_122() -> AblationEntry:
    return AblationEntry("ablation_122", 0.832, 0.752, 0.752)

def ablation_entry_123() -> AblationEntry:
    return AblationEntry("ablation_123", 0.833, 0.753, 0.753)

def ablation_entry_124() -> AblationEntry:
    return AblationEntry("ablation_124", 0.834, 0.754, 0.754)

def ablation_entry_125() -> AblationEntry:
    return AblationEntry("ablation_125", 0.835, 0.755, 0.755)

def ablation_entry_126() -> AblationEntry:
    return AblationEntry("ablation_126", 0.836, 0.756, 0.756)

def ablation_entry_127() -> AblationEntry:
    return AblationEntry("ablation_127", 0.837, 0.757, 0.757)

def ablation_entry_128() -> AblationEntry:
    return AblationEntry("ablation_128", 0.838, 0.758, 0.758)

def ablation_entry_129() -> AblationEntry:
    return AblationEntry("ablation_129", 0.839, 0.759, 0.759)

def ablation_entry_130() -> AblationEntry:
    return AblationEntry("ablation_130", 0.840, 0.760, 0.760)

def ablation_entry_131() -> AblationEntry:
    return AblationEntry("ablation_131", 0.841, 0.761, 0.761)

def ablation_entry_132() -> AblationEntry:
    return AblationEntry("ablation_132", 0.842, 0.762, 0.762)

def ablation_entry_133() -> AblationEntry:
    return AblationEntry("ablation_133", 0.843, 0.763, 0.763)

def ablation_entry_134() -> AblationEntry:
    return AblationEntry("ablation_134", 0.844, 0.764, 0.764)

def ablation_entry_135() -> AblationEntry:
    return AblationEntry("ablation_135", 0.845, 0.765, 0.765)

def ablation_entry_136() -> AblationEntry:
    return AblationEntry("ablation_136", 0.846, 0.766, 0.766)

def ablation_entry_137() -> AblationEntry:
    return AblationEntry("ablation_137", 0.847, 0.767, 0.767)

def ablation_entry_138() -> AblationEntry:
    return AblationEntry("ablation_138", 0.848, 0.768, 0.768)

def ablation_entry_139() -> AblationEntry:
    return AblationEntry("ablation_139", 0.849, 0.769, 0.769)

def ablation_entry_140() -> AblationEntry:
    return AblationEntry("ablation_140", 0.780, 0.770, 0.770)

def ablation_entry_141() -> AblationEntry:
    return AblationEntry("ablation_141", 0.781, 0.771, 0.771)

def ablation_entry_142() -> AblationEntry:
    return AblationEntry("ablation_142", 0.782, 0.772, 0.772)

def ablation_entry_143() -> AblationEntry:
    return AblationEntry("ablation_143", 0.783, 0.773, 0.773)

def ablation_entry_144() -> AblationEntry:
    return AblationEntry("ablation_144", 0.784, 0.774, 0.774)

def ablation_entry_145() -> AblationEntry:
    return AblationEntry("ablation_145", 0.785, 0.775, 0.775)

def ablation_entry_146() -> AblationEntry:
    return AblationEntry("ablation_146", 0.786, 0.776, 0.776)

def ablation_entry_147() -> AblationEntry:
    return AblationEntry("ablation_147", 0.787, 0.777, 0.777)

def ablation_entry_148() -> AblationEntry:
    return AblationEntry("ablation_148", 0.788, 0.778, 0.778)

def ablation_entry_149() -> AblationEntry:
    return AblationEntry("ablation_149", 0.789, 0.779, 0.779)

def ablation_entry_150() -> AblationEntry:
    return AblationEntry("ablation_150", 0.790, 0.780, 0.780)

def ablation_entry_151() -> AblationEntry:
    return AblationEntry("ablation_151", 0.791, 0.781, 0.781)

def ablation_entry_152() -> AblationEntry:
    return AblationEntry("ablation_152", 0.792, 0.782, 0.782)

def ablation_entry_153() -> AblationEntry:
    return AblationEntry("ablation_153", 0.793, 0.783, 0.783)

def ablation_entry_154() -> AblationEntry:
    return AblationEntry("ablation_154", 0.794, 0.784, 0.784)

def ablation_entry_155() -> AblationEntry:
    return AblationEntry("ablation_155", 0.795, 0.785, 0.785)

def ablation_entry_156() -> AblationEntry:
    return AblationEntry("ablation_156", 0.796, 0.786, 0.786)

def ablation_entry_157() -> AblationEntry:
    return AblationEntry("ablation_157", 0.797, 0.787, 0.787)

def ablation_entry_158() -> AblationEntry:
    return AblationEntry("ablation_158", 0.798, 0.788, 0.788)

def ablation_entry_159() -> AblationEntry:
    return AblationEntry("ablation_159", 0.799, 0.789, 0.789)

def ablation_entry_160() -> AblationEntry:
    return AblationEntry("ablation_160", 0.800, 0.790, 0.790)

def ablation_entry_161() -> AblationEntry:
    return AblationEntry("ablation_161", 0.801, 0.791, 0.791)

def ablation_entry_162() -> AblationEntry:
    return AblationEntry("ablation_162", 0.802, 0.792, 0.792)

def ablation_entry_163() -> AblationEntry:
    return AblationEntry("ablation_163", 0.803, 0.793, 0.793)

def ablation_entry_164() -> AblationEntry:
    return AblationEntry("ablation_164", 0.804, 0.794, 0.794)

def ablation_entry_165() -> AblationEntry:
    return AblationEntry("ablation_165", 0.805, 0.795, 0.795)

def ablation_entry_166() -> AblationEntry:
    return AblationEntry("ablation_166", 0.806, 0.796, 0.796)

def ablation_entry_167() -> AblationEntry:
    return AblationEntry("ablation_167", 0.807, 0.797, 0.797)

def ablation_entry_168() -> AblationEntry:
    return AblationEntry("ablation_168", 0.808, 0.798, 0.798)

def ablation_entry_169() -> AblationEntry:
    return AblationEntry("ablation_169", 0.809, 0.799, 0.799)

def ablation_entry_170() -> AblationEntry:
    return AblationEntry("ablation_170", 0.810, 0.800, 0.800)

def ablation_entry_171() -> AblationEntry:
    return AblationEntry("ablation_171", 0.811, 0.801, 0.801)

def ablation_entry_172() -> AblationEntry:
    return AblationEntry("ablation_172", 0.812, 0.802, 0.802)

def ablation_entry_173() -> AblationEntry:
    return AblationEntry("ablation_173", 0.813, 0.803, 0.803)

def ablation_entry_174() -> AblationEntry:
    return AblationEntry("ablation_174", 0.814, 0.804, 0.804)

def ablation_entry_175() -> AblationEntry:
    return AblationEntry("ablation_175", 0.815, 0.805, 0.805)

def ablation_entry_176() -> AblationEntry:
    return AblationEntry("ablation_176", 0.816, 0.806, 0.806)

def ablation_entry_177() -> AblationEntry:
    return AblationEntry("ablation_177", 0.817, 0.807, 0.807)

def ablation_entry_178() -> AblationEntry:
    return AblationEntry("ablation_178", 0.818, 0.808, 0.808)

def ablation_entry_179() -> AblationEntry:
    return AblationEntry("ablation_179", 0.819, 0.809, 0.809)

def ablation_entry_180() -> AblationEntry:
    return AblationEntry("ablation_180", 0.820, 0.720, 0.810)

def ablation_entry_181() -> AblationEntry:
    return AblationEntry("ablation_181", 0.821, 0.721, 0.811)

def ablation_entry_182() -> AblationEntry:
    return AblationEntry("ablation_182", 0.822, 0.722, 0.812)

def ablation_entry_183() -> AblationEntry:
    return AblationEntry("ablation_183", 0.823, 0.723, 0.813)

def ablation_entry_184() -> AblationEntry:
    return AblationEntry("ablation_184", 0.824, 0.724, 0.814)

def ablation_entry_185() -> AblationEntry:
    return AblationEntry("ablation_185", 0.825, 0.725, 0.815)

def ablation_entry_186() -> AblationEntry:
    return AblationEntry("ablation_186", 0.826, 0.726, 0.816)

def ablation_entry_187() -> AblationEntry:
    return AblationEntry("ablation_187", 0.827, 0.727, 0.817)

def ablation_entry_188() -> AblationEntry:
    return AblationEntry("ablation_188", 0.828, 0.728, 0.818)

def ablation_entry_189() -> AblationEntry:
    return AblationEntry("ablation_189", 0.829, 0.729, 0.819)

def ablation_entry_190() -> AblationEntry:
    return AblationEntry("ablation_190", 0.830, 0.730, 0.820)

def ablation_entry_191() -> AblationEntry:
    return AblationEntry("ablation_191", 0.831, 0.731, 0.821)

def ablation_entry_192() -> AblationEntry:
    return AblationEntry("ablation_192", 0.832, 0.732, 0.822)

def ablation_entry_193() -> AblationEntry:
    return AblationEntry("ablation_193", 0.833, 0.733, 0.823)

def ablation_entry_194() -> AblationEntry:
    return AblationEntry("ablation_194", 0.834, 0.734, 0.824)

def ablation_entry_195() -> AblationEntry:
    return AblationEntry("ablation_195", 0.835, 0.735, 0.825)

def ablation_entry_196() -> AblationEntry:
    return AblationEntry("ablation_196", 0.836, 0.736, 0.826)

def ablation_entry_197() -> AblationEntry:
    return AblationEntry("ablation_197", 0.837, 0.737, 0.827)

def ablation_entry_198() -> AblationEntry:
    return AblationEntry("ablation_198", 0.838, 0.738, 0.828)

def ablation_entry_199() -> AblationEntry:
    return AblationEntry("ablation_199", 0.839, 0.739, 0.829)

def ablation_entry_200() -> AblationEntry:
    return AblationEntry("ablation_200", 0.840, 0.740, 0.830)

def ablation_entry_201() -> AblationEntry:
    return AblationEntry("ablation_201", 0.841, 0.741, 0.831)

def ablation_entry_202() -> AblationEntry:
    return AblationEntry("ablation_202", 0.842, 0.742, 0.832)

def ablation_entry_203() -> AblationEntry:
    return AblationEntry("ablation_203", 0.843, 0.743, 0.833)

def ablation_entry_204() -> AblationEntry:
    return AblationEntry("ablation_204", 0.844, 0.744, 0.834)

def ablation_entry_205() -> AblationEntry:
    return AblationEntry("ablation_205", 0.845, 0.745, 0.835)

def ablation_entry_206() -> AblationEntry:
    return AblationEntry("ablation_206", 0.846, 0.746, 0.836)

def ablation_entry_207() -> AblationEntry:
    return AblationEntry("ablation_207", 0.847, 0.747, 0.837)

def ablation_entry_208() -> AblationEntry:
    return AblationEntry("ablation_208", 0.848, 0.748, 0.838)

def ablation_entry_209() -> AblationEntry:
    return AblationEntry("ablation_209", 0.849, 0.749, 0.839)

def ablation_entry_210() -> AblationEntry:
    return AblationEntry("ablation_210", 0.780, 0.750, 0.840)

def ablation_entry_211() -> AblationEntry:
    return AblationEntry("ablation_211", 0.781, 0.751, 0.841)

def ablation_entry_212() -> AblationEntry:
    return AblationEntry("ablation_212", 0.782, 0.752, 0.842)

def ablation_entry_213() -> AblationEntry:
    return AblationEntry("ablation_213", 0.783, 0.753, 0.843)

def ablation_entry_214() -> AblationEntry:
    return AblationEntry("ablation_214", 0.784, 0.754, 0.844)

def ablation_entry_215() -> AblationEntry:
    return AblationEntry("ablation_215", 0.785, 0.755, 0.845)

def ablation_entry_216() -> AblationEntry:
    return AblationEntry("ablation_216", 0.786, 0.756, 0.846)

def ablation_entry_217() -> AblationEntry:
    return AblationEntry("ablation_217", 0.787, 0.757, 0.847)

def ablation_entry_218() -> AblationEntry:
    return AblationEntry("ablation_218", 0.788, 0.758, 0.848)

def ablation_entry_219() -> AblationEntry:
    return AblationEntry("ablation_219", 0.789, 0.759, 0.849)

def ablation_entry_220() -> AblationEntry:
    return AblationEntry("ablation_220", 0.790, 0.760, 0.850)

