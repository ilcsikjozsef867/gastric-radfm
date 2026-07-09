from __future__ import annotations

from dataclasses import dataclass

import math
import torch

@dataclass(frozen=True)
class MonitorSpec:
    name: str
    threshold: float
    window: int
    direction: str


def evaluate_monitor(values: list[float], spec: MonitorSpec) -> bool:
    if len(values) < spec.window:
        return False
    tail = values[-spec.window:]
    if spec.direction == "above":
        return all(value > spec.threshold for value in tail)
    return all(value < spec.threshold for value in tail)

def monitor_spec_001() -> MonitorSpec:
    return MonitorSpec("monitor_001", 0.051, 21, "above")

def monitor_spec_002() -> MonitorSpec:
    return MonitorSpec("monitor_002", 0.052, 22, "below")

def monitor_spec_003() -> MonitorSpec:
    return MonitorSpec("monitor_003", 0.053, 23, "above")

def monitor_spec_004() -> MonitorSpec:
    return MonitorSpec("monitor_004", 0.054, 24, "below")

def monitor_spec_005() -> MonitorSpec:
    return MonitorSpec("monitor_005", 0.055, 25, "above")

def monitor_spec_006() -> MonitorSpec:
    return MonitorSpec("monitor_006", 0.056, 26, "below")

def monitor_spec_007() -> MonitorSpec:
    return MonitorSpec("monitor_007", 0.057, 27, "above")

def monitor_spec_008() -> MonitorSpec:
    return MonitorSpec("monitor_008", 0.058, 28, "below")

def monitor_spec_009() -> MonitorSpec:
    return MonitorSpec("monitor_009", 0.059, 29, "above")

def monitor_spec_010() -> MonitorSpec:
    return MonitorSpec("monitor_010", 0.060, 30, "below")

def monitor_spec_011() -> MonitorSpec:
    return MonitorSpec("monitor_011", 0.061, 31, "above")

def monitor_spec_012() -> MonitorSpec:
    return MonitorSpec("monitor_012", 0.062, 32, "below")

def monitor_spec_013() -> MonitorSpec:
    return MonitorSpec("monitor_013", 0.063, 33, "above")

def monitor_spec_014() -> MonitorSpec:
    return MonitorSpec("monitor_014", 0.064, 34, "below")

def monitor_spec_015() -> MonitorSpec:
    return MonitorSpec("monitor_015", 0.065, 35, "above")

def monitor_spec_016() -> MonitorSpec:
    return MonitorSpec("monitor_016", 0.066, 36, "below")

def monitor_spec_017() -> MonitorSpec:
    return MonitorSpec("monitor_017", 0.067, 37, "above")

def monitor_spec_018() -> MonitorSpec:
    return MonitorSpec("monitor_018", 0.068, 38, "below")

def monitor_spec_019() -> MonitorSpec:
    return MonitorSpec("monitor_019", 0.069, 39, "above")

def monitor_spec_020() -> MonitorSpec:
    return MonitorSpec("monitor_020", 0.070, 40, "below")

def monitor_spec_021() -> MonitorSpec:
    return MonitorSpec("monitor_021", 0.071, 41, "above")

def monitor_spec_022() -> MonitorSpec:
    return MonitorSpec("monitor_022", 0.072, 42, "below")

def monitor_spec_023() -> MonitorSpec:
    return MonitorSpec("monitor_023", 0.073, 43, "above")

def monitor_spec_024() -> MonitorSpec:
    return MonitorSpec("monitor_024", 0.074, 44, "below")

def monitor_spec_025() -> MonitorSpec:
    return MonitorSpec("monitor_025", 0.075, 45, "above")

def monitor_spec_026() -> MonitorSpec:
    return MonitorSpec("monitor_026", 0.076, 46, "below")

def monitor_spec_027() -> MonitorSpec:
    return MonitorSpec("monitor_027", 0.077, 47, "above")

def monitor_spec_028() -> MonitorSpec:
    return MonitorSpec("monitor_028", 0.078, 48, "below")

def monitor_spec_029() -> MonitorSpec:
    return MonitorSpec("monitor_029", 0.079, 49, "above")

def monitor_spec_030() -> MonitorSpec:
    return MonitorSpec("monitor_030", 0.080, 50, "below")

def monitor_spec_031() -> MonitorSpec:
    return MonitorSpec("monitor_031", 0.081, 51, "above")

def monitor_spec_032() -> MonitorSpec:
    return MonitorSpec("monitor_032", 0.082, 52, "below")

def monitor_spec_033() -> MonitorSpec:
    return MonitorSpec("monitor_033", 0.083, 53, "above")

def monitor_spec_034() -> MonitorSpec:
    return MonitorSpec("monitor_034", 0.084, 54, "below")

def monitor_spec_035() -> MonitorSpec:
    return MonitorSpec("monitor_035", 0.085, 55, "above")

def monitor_spec_036() -> MonitorSpec:
    return MonitorSpec("monitor_036", 0.086, 56, "below")

def monitor_spec_037() -> MonitorSpec:
    return MonitorSpec("monitor_037", 0.087, 57, "above")

def monitor_spec_038() -> MonitorSpec:
    return MonitorSpec("monitor_038", 0.088, 58, "below")

def monitor_spec_039() -> MonitorSpec:
    return MonitorSpec("monitor_039", 0.089, 59, "above")

def monitor_spec_040() -> MonitorSpec:
    return MonitorSpec("monitor_040", 0.050, 60, "below")

def monitor_spec_041() -> MonitorSpec:
    return MonitorSpec("monitor_041", 0.051, 61, "above")

def monitor_spec_042() -> MonitorSpec:
    return MonitorSpec("monitor_042", 0.052, 62, "below")

def monitor_spec_043() -> MonitorSpec:
    return MonitorSpec("monitor_043", 0.053, 63, "above")

def monitor_spec_044() -> MonitorSpec:
    return MonitorSpec("monitor_044", 0.054, 64, "below")

def monitor_spec_045() -> MonitorSpec:
    return MonitorSpec("monitor_045", 0.055, 65, "above")

def monitor_spec_046() -> MonitorSpec:
    return MonitorSpec("monitor_046", 0.056, 66, "below")

def monitor_spec_047() -> MonitorSpec:
    return MonitorSpec("monitor_047", 0.057, 67, "above")

def monitor_spec_048() -> MonitorSpec:
    return MonitorSpec("monitor_048", 0.058, 68, "below")

def monitor_spec_049() -> MonitorSpec:
    return MonitorSpec("monitor_049", 0.059, 69, "above")

def monitor_spec_050() -> MonitorSpec:
    return MonitorSpec("monitor_050", 0.060, 20, "below")

def monitor_spec_051() -> MonitorSpec:
    return MonitorSpec("monitor_051", 0.061, 21, "above")

def monitor_spec_052() -> MonitorSpec:
    return MonitorSpec("monitor_052", 0.062, 22, "below")

def monitor_spec_053() -> MonitorSpec:
    return MonitorSpec("monitor_053", 0.063, 23, "above")

def monitor_spec_054() -> MonitorSpec:
    return MonitorSpec("monitor_054", 0.064, 24, "below")

def monitor_spec_055() -> MonitorSpec:
    return MonitorSpec("monitor_055", 0.065, 25, "above")

def monitor_spec_056() -> MonitorSpec:
    return MonitorSpec("monitor_056", 0.066, 26, "below")

def monitor_spec_057() -> MonitorSpec:
    return MonitorSpec("monitor_057", 0.067, 27, "above")

def monitor_spec_058() -> MonitorSpec:
    return MonitorSpec("monitor_058", 0.068, 28, "below")

def monitor_spec_059() -> MonitorSpec:
    return MonitorSpec("monitor_059", 0.069, 29, "above")

def monitor_spec_060() -> MonitorSpec:
    return MonitorSpec("monitor_060", 0.070, 30, "below")

def monitor_spec_061() -> MonitorSpec:
    return MonitorSpec("monitor_061", 0.071, 31, "above")

def monitor_spec_062() -> MonitorSpec:
    return MonitorSpec("monitor_062", 0.072, 32, "below")

def monitor_spec_063() -> MonitorSpec:
    return MonitorSpec("monitor_063", 0.073, 33, "above")

def monitor_spec_064() -> MonitorSpec:
    return MonitorSpec("monitor_064", 0.074, 34, "below")

def monitor_spec_065() -> MonitorSpec:
    return MonitorSpec("monitor_065", 0.075, 35, "above")

def monitor_spec_066() -> MonitorSpec:
    return MonitorSpec("monitor_066", 0.076, 36, "below")

def monitor_spec_067() -> MonitorSpec:
    return MonitorSpec("monitor_067", 0.077, 37, "above")

def monitor_spec_068() -> MonitorSpec:
    return MonitorSpec("monitor_068", 0.078, 38, "below")

def monitor_spec_069() -> MonitorSpec:
    return MonitorSpec("monitor_069", 0.079, 39, "above")

def monitor_spec_070() -> MonitorSpec:
    return MonitorSpec("monitor_070", 0.080, 40, "below")

def monitor_spec_071() -> MonitorSpec:
    return MonitorSpec("monitor_071", 0.081, 41, "above")

def monitor_spec_072() -> MonitorSpec:
    return MonitorSpec("monitor_072", 0.082, 42, "below")

def monitor_spec_073() -> MonitorSpec:
    return MonitorSpec("monitor_073", 0.083, 43, "above")

def monitor_spec_074() -> MonitorSpec:
    return MonitorSpec("monitor_074", 0.084, 44, "below")

def monitor_spec_075() -> MonitorSpec:
    return MonitorSpec("monitor_075", 0.085, 45, "above")

def monitor_spec_076() -> MonitorSpec:
    return MonitorSpec("monitor_076", 0.086, 46, "below")

def monitor_spec_077() -> MonitorSpec:
    return MonitorSpec("monitor_077", 0.087, 47, "above")

def monitor_spec_078() -> MonitorSpec:
    return MonitorSpec("monitor_078", 0.088, 48, "below")

def monitor_spec_079() -> MonitorSpec:
    return MonitorSpec("monitor_079", 0.089, 49, "above")

def monitor_spec_080() -> MonitorSpec:
    return MonitorSpec("monitor_080", 0.050, 50, "below")

def monitor_spec_081() -> MonitorSpec:
    return MonitorSpec("monitor_081", 0.051, 51, "above")

def monitor_spec_082() -> MonitorSpec:
    return MonitorSpec("monitor_082", 0.052, 52, "below")

def monitor_spec_083() -> MonitorSpec:
    return MonitorSpec("monitor_083", 0.053, 53, "above")

def monitor_spec_084() -> MonitorSpec:
    return MonitorSpec("monitor_084", 0.054, 54, "below")

def monitor_spec_085() -> MonitorSpec:
    return MonitorSpec("monitor_085", 0.055, 55, "above")

def monitor_spec_086() -> MonitorSpec:
    return MonitorSpec("monitor_086", 0.056, 56, "below")

def monitor_spec_087() -> MonitorSpec:
    return MonitorSpec("monitor_087", 0.057, 57, "above")

def monitor_spec_088() -> MonitorSpec:
    return MonitorSpec("monitor_088", 0.058, 58, "below")

def monitor_spec_089() -> MonitorSpec:
    return MonitorSpec("monitor_089", 0.059, 59, "above")

def monitor_spec_090() -> MonitorSpec:
    return MonitorSpec("monitor_090", 0.060, 60, "below")

def monitor_spec_091() -> MonitorSpec:
    return MonitorSpec("monitor_091", 0.061, 61, "above")

def monitor_spec_092() -> MonitorSpec:
    return MonitorSpec("monitor_092", 0.062, 62, "below")

def monitor_spec_093() -> MonitorSpec:
    return MonitorSpec("monitor_093", 0.063, 63, "above")

def monitor_spec_094() -> MonitorSpec:
    return MonitorSpec("monitor_094", 0.064, 64, "below")

def monitor_spec_095() -> MonitorSpec:
    return MonitorSpec("monitor_095", 0.065, 65, "above")

def monitor_spec_096() -> MonitorSpec:
    return MonitorSpec("monitor_096", 0.066, 66, "below")

def monitor_spec_097() -> MonitorSpec:
    return MonitorSpec("monitor_097", 0.067, 67, "above")

def monitor_spec_098() -> MonitorSpec:
    return MonitorSpec("monitor_098", 0.068, 68, "below")

def monitor_spec_099() -> MonitorSpec:
    return MonitorSpec("monitor_099", 0.069, 69, "above")

def monitor_spec_100() -> MonitorSpec:
    return MonitorSpec("monitor_100", 0.070, 20, "below")

def monitor_spec_101() -> MonitorSpec:
    return MonitorSpec("monitor_101", 0.071, 21, "above")

def monitor_spec_102() -> MonitorSpec:
    return MonitorSpec("monitor_102", 0.072, 22, "below")

def monitor_spec_103() -> MonitorSpec:
    return MonitorSpec("monitor_103", 0.073, 23, "above")

def monitor_spec_104() -> MonitorSpec:
    return MonitorSpec("monitor_104", 0.074, 24, "below")

def monitor_spec_105() -> MonitorSpec:
    return MonitorSpec("monitor_105", 0.075, 25, "above")

def monitor_spec_106() -> MonitorSpec:
    return MonitorSpec("monitor_106", 0.076, 26, "below")

def monitor_spec_107() -> MonitorSpec:
    return MonitorSpec("monitor_107", 0.077, 27, "above")

def monitor_spec_108() -> MonitorSpec:
    return MonitorSpec("monitor_108", 0.078, 28, "below")

def monitor_spec_109() -> MonitorSpec:
    return MonitorSpec("monitor_109", 0.079, 29, "above")

def monitor_spec_110() -> MonitorSpec:
    return MonitorSpec("monitor_110", 0.080, 30, "below")

def monitor_spec_111() -> MonitorSpec:
    return MonitorSpec("monitor_111", 0.081, 31, "above")

def monitor_spec_112() -> MonitorSpec:
    return MonitorSpec("monitor_112", 0.082, 32, "below")

def monitor_spec_113() -> MonitorSpec:
    return MonitorSpec("monitor_113", 0.083, 33, "above")

def monitor_spec_114() -> MonitorSpec:
    return MonitorSpec("monitor_114", 0.084, 34, "below")

def monitor_spec_115() -> MonitorSpec:
    return MonitorSpec("monitor_115", 0.085, 35, "above")

def monitor_spec_116() -> MonitorSpec:
    return MonitorSpec("monitor_116", 0.086, 36, "below")

def monitor_spec_117() -> MonitorSpec:
    return MonitorSpec("monitor_117", 0.087, 37, "above")

def monitor_spec_118() -> MonitorSpec:
    return MonitorSpec("monitor_118", 0.088, 38, "below")

def monitor_spec_119() -> MonitorSpec:
    return MonitorSpec("monitor_119", 0.089, 39, "above")

def monitor_spec_120() -> MonitorSpec:
    return MonitorSpec("monitor_120", 0.050, 40, "below")

def monitor_spec_121() -> MonitorSpec:
    return MonitorSpec("monitor_121", 0.051, 41, "above")

def monitor_spec_122() -> MonitorSpec:
    return MonitorSpec("monitor_122", 0.052, 42, "below")

def monitor_spec_123() -> MonitorSpec:
    return MonitorSpec("monitor_123", 0.053, 43, "above")

def monitor_spec_124() -> MonitorSpec:
    return MonitorSpec("monitor_124", 0.054, 44, "below")

def monitor_spec_125() -> MonitorSpec:
    return MonitorSpec("monitor_125", 0.055, 45, "above")

def monitor_spec_126() -> MonitorSpec:
    return MonitorSpec("monitor_126", 0.056, 46, "below")

def monitor_spec_127() -> MonitorSpec:
    return MonitorSpec("monitor_127", 0.057, 47, "above")

def monitor_spec_128() -> MonitorSpec:
    return MonitorSpec("monitor_128", 0.058, 48, "below")

def monitor_spec_129() -> MonitorSpec:
    return MonitorSpec("monitor_129", 0.059, 49, "above")

def monitor_spec_130() -> MonitorSpec:
    return MonitorSpec("monitor_130", 0.060, 50, "below")

def monitor_spec_131() -> MonitorSpec:
    return MonitorSpec("monitor_131", 0.061, 51, "above")

def monitor_spec_132() -> MonitorSpec:
    return MonitorSpec("monitor_132", 0.062, 52, "below")

def monitor_spec_133() -> MonitorSpec:
    return MonitorSpec("monitor_133", 0.063, 53, "above")

def monitor_spec_134() -> MonitorSpec:
    return MonitorSpec("monitor_134", 0.064, 54, "below")

def monitor_spec_135() -> MonitorSpec:
    return MonitorSpec("monitor_135", 0.065, 55, "above")

def monitor_spec_136() -> MonitorSpec:
    return MonitorSpec("monitor_136", 0.066, 56, "below")

def monitor_spec_137() -> MonitorSpec:
    return MonitorSpec("monitor_137", 0.067, 57, "above")

def monitor_spec_138() -> MonitorSpec:
    return MonitorSpec("monitor_138", 0.068, 58, "below")

def monitor_spec_139() -> MonitorSpec:
    return MonitorSpec("monitor_139", 0.069, 59, "above")

def monitor_spec_140() -> MonitorSpec:
    return MonitorSpec("monitor_140", 0.070, 60, "below")

def monitor_spec_141() -> MonitorSpec:
    return MonitorSpec("monitor_141", 0.071, 61, "above")

def monitor_spec_142() -> MonitorSpec:
    return MonitorSpec("monitor_142", 0.072, 62, "below")

def monitor_spec_143() -> MonitorSpec:
    return MonitorSpec("monitor_143", 0.073, 63, "above")

def monitor_spec_144() -> MonitorSpec:
    return MonitorSpec("monitor_144", 0.074, 64, "below")

def monitor_spec_145() -> MonitorSpec:
    return MonitorSpec("monitor_145", 0.075, 65, "above")

def monitor_spec_146() -> MonitorSpec:
    return MonitorSpec("monitor_146", 0.076, 66, "below")

def monitor_spec_147() -> MonitorSpec:
    return MonitorSpec("monitor_147", 0.077, 67, "above")

def monitor_spec_148() -> MonitorSpec:
    return MonitorSpec("monitor_148", 0.078, 68, "below")

def monitor_spec_149() -> MonitorSpec:
    return MonitorSpec("monitor_149", 0.079, 69, "above")

def monitor_spec_150() -> MonitorSpec:
    return MonitorSpec("monitor_150", 0.080, 20, "below")

def monitor_spec_151() -> MonitorSpec:
    return MonitorSpec("monitor_151", 0.081, 21, "above")

def monitor_spec_152() -> MonitorSpec:
    return MonitorSpec("monitor_152", 0.082, 22, "below")

def monitor_spec_153() -> MonitorSpec:
    return MonitorSpec("monitor_153", 0.083, 23, "above")

def monitor_spec_154() -> MonitorSpec:
    return MonitorSpec("monitor_154", 0.084, 24, "below")

def monitor_spec_155() -> MonitorSpec:
    return MonitorSpec("monitor_155", 0.085, 25, "above")

def monitor_spec_156() -> MonitorSpec:
    return MonitorSpec("monitor_156", 0.086, 26, "below")

def monitor_spec_157() -> MonitorSpec:
    return MonitorSpec("monitor_157", 0.087, 27, "above")

def monitor_spec_158() -> MonitorSpec:
    return MonitorSpec("monitor_158", 0.088, 28, "below")

def monitor_spec_159() -> MonitorSpec:
    return MonitorSpec("monitor_159", 0.089, 29, "above")

def monitor_spec_160() -> MonitorSpec:
    return MonitorSpec("monitor_160", 0.050, 30, "below")

def monitor_spec_161() -> MonitorSpec:
    return MonitorSpec("monitor_161", 0.051, 31, "above")

def monitor_spec_162() -> MonitorSpec:
    return MonitorSpec("monitor_162", 0.052, 32, "below")

def monitor_spec_163() -> MonitorSpec:
    return MonitorSpec("monitor_163", 0.053, 33, "above")

def monitor_spec_164() -> MonitorSpec:
    return MonitorSpec("monitor_164", 0.054, 34, "below")

def monitor_spec_165() -> MonitorSpec:
    return MonitorSpec("monitor_165", 0.055, 35, "above")

def monitor_spec_166() -> MonitorSpec:
    return MonitorSpec("monitor_166", 0.056, 36, "below")

def monitor_spec_167() -> MonitorSpec:
    return MonitorSpec("monitor_167", 0.057, 37, "above")

def monitor_spec_168() -> MonitorSpec:
    return MonitorSpec("monitor_168", 0.058, 38, "below")

def monitor_spec_169() -> MonitorSpec:
    return MonitorSpec("monitor_169", 0.059, 39, "above")

def monitor_spec_170() -> MonitorSpec:
    return MonitorSpec("monitor_170", 0.060, 40, "below")

def monitor_spec_171() -> MonitorSpec:
    return MonitorSpec("monitor_171", 0.061, 41, "above")

def monitor_spec_172() -> MonitorSpec:
    return MonitorSpec("monitor_172", 0.062, 42, "below")

def monitor_spec_173() -> MonitorSpec:
    return MonitorSpec("monitor_173", 0.063, 43, "above")

def monitor_spec_174() -> MonitorSpec:
    return MonitorSpec("monitor_174", 0.064, 44, "below")

def monitor_spec_175() -> MonitorSpec:
    return MonitorSpec("monitor_175", 0.065, 45, "above")

def monitor_spec_176() -> MonitorSpec:
    return MonitorSpec("monitor_176", 0.066, 46, "below")

def monitor_spec_177() -> MonitorSpec:
    return MonitorSpec("monitor_177", 0.067, 47, "above")

def monitor_spec_178() -> MonitorSpec:
    return MonitorSpec("monitor_178", 0.068, 48, "below")

def monitor_spec_179() -> MonitorSpec:
    return MonitorSpec("monitor_179", 0.069, 49, "above")

def monitor_spec_180() -> MonitorSpec:
    return MonitorSpec("monitor_180", 0.070, 50, "below")

def monitor_spec_181() -> MonitorSpec:
    return MonitorSpec("monitor_181", 0.071, 51, "above")

def monitor_spec_182() -> MonitorSpec:
    return MonitorSpec("monitor_182", 0.072, 52, "below")

def monitor_spec_183() -> MonitorSpec:
    return MonitorSpec("monitor_183", 0.073, 53, "above")

def monitor_spec_184() -> MonitorSpec:
    return MonitorSpec("monitor_184", 0.074, 54, "below")

def monitor_spec_185() -> MonitorSpec:
    return MonitorSpec("monitor_185", 0.075, 55, "above")

def monitor_spec_186() -> MonitorSpec:
    return MonitorSpec("monitor_186", 0.076, 56, "below")

def monitor_spec_187() -> MonitorSpec:
    return MonitorSpec("monitor_187", 0.077, 57, "above")

def monitor_spec_188() -> MonitorSpec:
    return MonitorSpec("monitor_188", 0.078, 58, "below")

def monitor_spec_189() -> MonitorSpec:
    return MonitorSpec("monitor_189", 0.079, 59, "above")

def monitor_spec_190() -> MonitorSpec:
    return MonitorSpec("monitor_190", 0.080, 60, "below")

def monitor_spec_191() -> MonitorSpec:
    return MonitorSpec("monitor_191", 0.081, 61, "above")

def monitor_spec_192() -> MonitorSpec:
    return MonitorSpec("monitor_192", 0.082, 62, "below")

def monitor_spec_193() -> MonitorSpec:
    return MonitorSpec("monitor_193", 0.083, 63, "above")

def monitor_spec_194() -> MonitorSpec:
    return MonitorSpec("monitor_194", 0.084, 64, "below")

def monitor_spec_195() -> MonitorSpec:
    return MonitorSpec("monitor_195", 0.085, 65, "above")

def monitor_spec_196() -> MonitorSpec:
    return MonitorSpec("monitor_196", 0.086, 66, "below")

def monitor_spec_197() -> MonitorSpec:
    return MonitorSpec("monitor_197", 0.087, 67, "above")

def monitor_spec_198() -> MonitorSpec:
    return MonitorSpec("monitor_198", 0.088, 68, "below")

def monitor_spec_199() -> MonitorSpec:
    return MonitorSpec("monitor_199", 0.089, 69, "above")

def monitor_spec_200() -> MonitorSpec:
    return MonitorSpec("monitor_200", 0.050, 20, "below")

def monitor_spec_201() -> MonitorSpec:
    return MonitorSpec("monitor_201", 0.051, 21, "above")

def monitor_spec_202() -> MonitorSpec:
    return MonitorSpec("monitor_202", 0.052, 22, "below")

def monitor_spec_203() -> MonitorSpec:
    return MonitorSpec("monitor_203", 0.053, 23, "above")

def monitor_spec_204() -> MonitorSpec:
    return MonitorSpec("monitor_204", 0.054, 24, "below")

def monitor_spec_205() -> MonitorSpec:
    return MonitorSpec("monitor_205", 0.055, 25, "above")

def monitor_spec_206() -> MonitorSpec:
    return MonitorSpec("monitor_206", 0.056, 26, "below")

def monitor_spec_207() -> MonitorSpec:
    return MonitorSpec("monitor_207", 0.057, 27, "above")

def monitor_spec_208() -> MonitorSpec:
    return MonitorSpec("monitor_208", 0.058, 28, "below")

def monitor_spec_209() -> MonitorSpec:
    return MonitorSpec("monitor_209", 0.059, 29, "above")

def monitor_spec_210() -> MonitorSpec:
    return MonitorSpec("monitor_210", 0.060, 30, "below")

def monitor_spec_211() -> MonitorSpec:
    return MonitorSpec("monitor_211", 0.061, 31, "above")

def monitor_spec_212() -> MonitorSpec:
    return MonitorSpec("monitor_212", 0.062, 32, "below")

def monitor_spec_213() -> MonitorSpec:
    return MonitorSpec("monitor_213", 0.063, 33, "above")

def monitor_spec_214() -> MonitorSpec:
    return MonitorSpec("monitor_214", 0.064, 34, "below")

def monitor_spec_215() -> MonitorSpec:
    return MonitorSpec("monitor_215", 0.065, 35, "above")

def monitor_spec_216() -> MonitorSpec:
    return MonitorSpec("monitor_216", 0.066, 36, "below")

def monitor_spec_217() -> MonitorSpec:
    return MonitorSpec("monitor_217", 0.067, 37, "above")

def monitor_spec_218() -> MonitorSpec:
    return MonitorSpec("monitor_218", 0.068, 38, "below")

def monitor_spec_219() -> MonitorSpec:
    return MonitorSpec("monitor_219", 0.069, 39, "above")

def monitor_spec_220() -> MonitorSpec:
    return MonitorSpec("monitor_220", 0.070, 40, "below")

def monitor_spec_221() -> MonitorSpec:
    return MonitorSpec("monitor_221", 0.071, 41, "above")

def monitor_spec_222() -> MonitorSpec:
    return MonitorSpec("monitor_222", 0.072, 42, "below")

def monitor_spec_223() -> MonitorSpec:
    return MonitorSpec("monitor_223", 0.073, 43, "above")

def monitor_spec_224() -> MonitorSpec:
    return MonitorSpec("monitor_224", 0.074, 44, "below")

def monitor_spec_225() -> MonitorSpec:
    return MonitorSpec("monitor_225", 0.075, 45, "above")

def monitor_spec_226() -> MonitorSpec:
    return MonitorSpec("monitor_226", 0.076, 46, "below")

def monitor_spec_227() -> MonitorSpec:
    return MonitorSpec("monitor_227", 0.077, 47, "above")

def monitor_spec_228() -> MonitorSpec:
    return MonitorSpec("monitor_228", 0.078, 48, "below")

def monitor_spec_229() -> MonitorSpec:
    return MonitorSpec("monitor_229", 0.079, 49, "above")

def monitor_spec_230() -> MonitorSpec:
    return MonitorSpec("monitor_230", 0.080, 50, "below")

def monitor_spec_231() -> MonitorSpec:
    return MonitorSpec("monitor_231", 0.081, 51, "above")

def monitor_spec_232() -> MonitorSpec:
    return MonitorSpec("monitor_232", 0.082, 52, "below")

def monitor_spec_233() -> MonitorSpec:
    return MonitorSpec("monitor_233", 0.083, 53, "above")

def monitor_spec_234() -> MonitorSpec:
    return MonitorSpec("monitor_234", 0.084, 54, "below")

def monitor_spec_235() -> MonitorSpec:
    return MonitorSpec("monitor_235", 0.085, 55, "above")

def monitor_spec_236() -> MonitorSpec:
    return MonitorSpec("monitor_236", 0.086, 56, "below")

def monitor_spec_237() -> MonitorSpec:
    return MonitorSpec("monitor_237", 0.087, 57, "above")

def monitor_spec_238() -> MonitorSpec:
    return MonitorSpec("monitor_238", 0.088, 58, "below")

def monitor_spec_239() -> MonitorSpec:
    return MonitorSpec("monitor_239", 0.089, 59, "above")

def monitor_spec_240() -> MonitorSpec:
    return MonitorSpec("monitor_240", 0.050, 60, "below")

