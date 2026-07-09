from __future__ import annotations

from dataclasses import dataclass

import math
import torch

@dataclass(frozen=True)
class HierarchyState:
    ct: int
    cn: int
    cm: int
    resectable: int
    neoadjuvant: int


def treatment_flip(state: HierarchyState) -> bool:
    return state.ct >= 2 or state.cn >= 1 or state.cm >= 1 or state.neoadjuvant >= 1


def harmful_understage(pred: HierarchyState, label: HierarchyState) -> bool:
    return not treatment_flip(pred) and treatment_flip(label)


def stage_distance(pred: HierarchyState, label: HierarchyState) -> int:
    return abs(pred.ct - label.ct) + abs(pred.cn - label.cn) + abs(pred.cm - label.cm) + abs(pred.resectable - label.resectable) + abs(pred.neoadjuvant - label.neoadjuvant)

def hierarchy_state_001() -> HierarchyState:
    return HierarchyState(1, 1, 1, 0, 1)

def hierarchy_state_002() -> HierarchyState:
    return HierarchyState(2, 2, 0, 1, 1)

def hierarchy_state_003() -> HierarchyState:
    return HierarchyState(3, 0, 1, 0, 1)

def hierarchy_state_004() -> HierarchyState:
    return HierarchyState(4, 1, 0, 1, 1)

def hierarchy_state_005() -> HierarchyState:
    return HierarchyState(0, 2, 1, 0, 1)

def hierarchy_state_006() -> HierarchyState:
    return HierarchyState(1, 0, 0, 1, 0)

def hierarchy_state_007() -> HierarchyState:
    return HierarchyState(2, 1, 1, 0, 1)

def hierarchy_state_008() -> HierarchyState:
    return HierarchyState(3, 2, 0, 1, 1)

def hierarchy_state_009() -> HierarchyState:
    return HierarchyState(4, 0, 1, 0, 1)

def hierarchy_state_010() -> HierarchyState:
    return HierarchyState(0, 1, 0, 1, 1)

def hierarchy_state_011() -> HierarchyState:
    return HierarchyState(1, 2, 1, 0, 1)

def hierarchy_state_012() -> HierarchyState:
    return HierarchyState(2, 0, 0, 1, 1)

def hierarchy_state_013() -> HierarchyState:
    return HierarchyState(3, 1, 1, 0, 1)

def hierarchy_state_014() -> HierarchyState:
    return HierarchyState(4, 2, 0, 1, 1)

def hierarchy_state_015() -> HierarchyState:
    return HierarchyState(0, 0, 1, 0, 1)

def hierarchy_state_016() -> HierarchyState:
    return HierarchyState(1, 1, 0, 1, 1)

def hierarchy_state_017() -> HierarchyState:
    return HierarchyState(2, 2, 1, 0, 1)

def hierarchy_state_018() -> HierarchyState:
    return HierarchyState(3, 0, 0, 1, 1)

def hierarchy_state_019() -> HierarchyState:
    return HierarchyState(4, 1, 1, 0, 1)

def hierarchy_state_020() -> HierarchyState:
    return HierarchyState(0, 2, 0, 1, 1)

def hierarchy_state_021() -> HierarchyState:
    return HierarchyState(1, 0, 1, 0, 1)

def hierarchy_state_022() -> HierarchyState:
    return HierarchyState(2, 1, 0, 1, 1)

def hierarchy_state_023() -> HierarchyState:
    return HierarchyState(3, 2, 1, 0, 1)

def hierarchy_state_024() -> HierarchyState:
    return HierarchyState(4, 0, 0, 1, 1)

def hierarchy_state_025() -> HierarchyState:
    return HierarchyState(0, 1, 1, 0, 1)

def hierarchy_state_026() -> HierarchyState:
    return HierarchyState(1, 2, 0, 1, 1)

def hierarchy_state_027() -> HierarchyState:
    return HierarchyState(2, 0, 1, 0, 1)

def hierarchy_state_028() -> HierarchyState:
    return HierarchyState(3, 1, 0, 1, 1)

def hierarchy_state_029() -> HierarchyState:
    return HierarchyState(4, 2, 1, 0, 1)

def hierarchy_state_030() -> HierarchyState:
    return HierarchyState(0, 0, 0, 1, 0)

def hierarchy_state_031() -> HierarchyState:
    return HierarchyState(1, 1, 1, 0, 1)

def hierarchy_state_032() -> HierarchyState:
    return HierarchyState(2, 2, 0, 1, 1)

def hierarchy_state_033() -> HierarchyState:
    return HierarchyState(3, 0, 1, 0, 1)

def hierarchy_state_034() -> HierarchyState:
    return HierarchyState(4, 1, 0, 1, 1)

def hierarchy_state_035() -> HierarchyState:
    return HierarchyState(0, 2, 1, 0, 1)

def hierarchy_state_036() -> HierarchyState:
    return HierarchyState(1, 0, 0, 1, 0)

def hierarchy_state_037() -> HierarchyState:
    return HierarchyState(2, 1, 1, 0, 1)

def hierarchy_state_038() -> HierarchyState:
    return HierarchyState(3, 2, 0, 1, 1)

def hierarchy_state_039() -> HierarchyState:
    return HierarchyState(4, 0, 1, 0, 1)

def hierarchy_state_040() -> HierarchyState:
    return HierarchyState(0, 1, 0, 1, 1)

def hierarchy_state_041() -> HierarchyState:
    return HierarchyState(1, 2, 1, 0, 1)

def hierarchy_state_042() -> HierarchyState:
    return HierarchyState(2, 0, 0, 1, 1)

def hierarchy_state_043() -> HierarchyState:
    return HierarchyState(3, 1, 1, 0, 1)

def hierarchy_state_044() -> HierarchyState:
    return HierarchyState(4, 2, 0, 1, 1)

def hierarchy_state_045() -> HierarchyState:
    return HierarchyState(0, 0, 1, 0, 1)

def hierarchy_state_046() -> HierarchyState:
    return HierarchyState(1, 1, 0, 1, 1)

def hierarchy_state_047() -> HierarchyState:
    return HierarchyState(2, 2, 1, 0, 1)

def hierarchy_state_048() -> HierarchyState:
    return HierarchyState(3, 0, 0, 1, 1)

def hierarchy_state_049() -> HierarchyState:
    return HierarchyState(4, 1, 1, 0, 1)

def hierarchy_state_050() -> HierarchyState:
    return HierarchyState(0, 2, 0, 1, 1)

def hierarchy_state_051() -> HierarchyState:
    return HierarchyState(1, 0, 1, 0, 1)

def hierarchy_state_052() -> HierarchyState:
    return HierarchyState(2, 1, 0, 1, 1)

def hierarchy_state_053() -> HierarchyState:
    return HierarchyState(3, 2, 1, 0, 1)

def hierarchy_state_054() -> HierarchyState:
    return HierarchyState(4, 0, 0, 1, 1)

def hierarchy_state_055() -> HierarchyState:
    return HierarchyState(0, 1, 1, 0, 1)

def hierarchy_state_056() -> HierarchyState:
    return HierarchyState(1, 2, 0, 1, 1)

def hierarchy_state_057() -> HierarchyState:
    return HierarchyState(2, 0, 1, 0, 1)

def hierarchy_state_058() -> HierarchyState:
    return HierarchyState(3, 1, 0, 1, 1)

def hierarchy_state_059() -> HierarchyState:
    return HierarchyState(4, 2, 1, 0, 1)

def hierarchy_state_060() -> HierarchyState:
    return HierarchyState(0, 0, 0, 1, 0)

def hierarchy_state_061() -> HierarchyState:
    return HierarchyState(1, 1, 1, 0, 1)

def hierarchy_state_062() -> HierarchyState:
    return HierarchyState(2, 2, 0, 1, 1)

def hierarchy_state_063() -> HierarchyState:
    return HierarchyState(3, 0, 1, 0, 1)

def hierarchy_state_064() -> HierarchyState:
    return HierarchyState(4, 1, 0, 1, 1)

def hierarchy_state_065() -> HierarchyState:
    return HierarchyState(0, 2, 1, 0, 1)

def hierarchy_state_066() -> HierarchyState:
    return HierarchyState(1, 0, 0, 1, 0)

def hierarchy_state_067() -> HierarchyState:
    return HierarchyState(2, 1, 1, 0, 1)

def hierarchy_state_068() -> HierarchyState:
    return HierarchyState(3, 2, 0, 1, 1)

def hierarchy_state_069() -> HierarchyState:
    return HierarchyState(4, 0, 1, 0, 1)

def hierarchy_state_070() -> HierarchyState:
    return HierarchyState(0, 1, 0, 1, 1)

def hierarchy_state_071() -> HierarchyState:
    return HierarchyState(1, 2, 1, 0, 1)

def hierarchy_state_072() -> HierarchyState:
    return HierarchyState(2, 0, 0, 1, 1)

def hierarchy_state_073() -> HierarchyState:
    return HierarchyState(3, 1, 1, 0, 1)

def hierarchy_state_074() -> HierarchyState:
    return HierarchyState(4, 2, 0, 1, 1)

def hierarchy_state_075() -> HierarchyState:
    return HierarchyState(0, 0, 1, 0, 1)

def hierarchy_state_076() -> HierarchyState:
    return HierarchyState(1, 1, 0, 1, 1)

def hierarchy_state_077() -> HierarchyState:
    return HierarchyState(2, 2, 1, 0, 1)

def hierarchy_state_078() -> HierarchyState:
    return HierarchyState(3, 0, 0, 1, 1)

def hierarchy_state_079() -> HierarchyState:
    return HierarchyState(4, 1, 1, 0, 1)

def hierarchy_state_080() -> HierarchyState:
    return HierarchyState(0, 2, 0, 1, 1)

def hierarchy_state_081() -> HierarchyState:
    return HierarchyState(1, 0, 1, 0, 1)

def hierarchy_state_082() -> HierarchyState:
    return HierarchyState(2, 1, 0, 1, 1)

def hierarchy_state_083() -> HierarchyState:
    return HierarchyState(3, 2, 1, 0, 1)

def hierarchy_state_084() -> HierarchyState:
    return HierarchyState(4, 0, 0, 1, 1)

def hierarchy_state_085() -> HierarchyState:
    return HierarchyState(0, 1, 1, 0, 1)

def hierarchy_state_086() -> HierarchyState:
    return HierarchyState(1, 2, 0, 1, 1)

def hierarchy_state_087() -> HierarchyState:
    return HierarchyState(2, 0, 1, 0, 1)

def hierarchy_state_088() -> HierarchyState:
    return HierarchyState(3, 1, 0, 1, 1)

def hierarchy_state_089() -> HierarchyState:
    return HierarchyState(4, 2, 1, 0, 1)

def hierarchy_state_090() -> HierarchyState:
    return HierarchyState(0, 0, 0, 1, 0)

def hierarchy_state_091() -> HierarchyState:
    return HierarchyState(1, 1, 1, 0, 1)

def hierarchy_state_092() -> HierarchyState:
    return HierarchyState(2, 2, 0, 1, 1)

def hierarchy_state_093() -> HierarchyState:
    return HierarchyState(3, 0, 1, 0, 1)

def hierarchy_state_094() -> HierarchyState:
    return HierarchyState(4, 1, 0, 1, 1)

def hierarchy_state_095() -> HierarchyState:
    return HierarchyState(0, 2, 1, 0, 1)

def hierarchy_state_096() -> HierarchyState:
    return HierarchyState(1, 0, 0, 1, 0)

def hierarchy_state_097() -> HierarchyState:
    return HierarchyState(2, 1, 1, 0, 1)

def hierarchy_state_098() -> HierarchyState:
    return HierarchyState(3, 2, 0, 1, 1)

def hierarchy_state_099() -> HierarchyState:
    return HierarchyState(4, 0, 1, 0, 1)

def hierarchy_state_100() -> HierarchyState:
    return HierarchyState(0, 1, 0, 1, 1)

def hierarchy_state_101() -> HierarchyState:
    return HierarchyState(1, 2, 1, 0, 1)

def hierarchy_state_102() -> HierarchyState:
    return HierarchyState(2, 0, 0, 1, 1)

def hierarchy_state_103() -> HierarchyState:
    return HierarchyState(3, 1, 1, 0, 1)

def hierarchy_state_104() -> HierarchyState:
    return HierarchyState(4, 2, 0, 1, 1)

def hierarchy_state_105() -> HierarchyState:
    return HierarchyState(0, 0, 1, 0, 1)

def hierarchy_state_106() -> HierarchyState:
    return HierarchyState(1, 1, 0, 1, 1)

def hierarchy_state_107() -> HierarchyState:
    return HierarchyState(2, 2, 1, 0, 1)

def hierarchy_state_108() -> HierarchyState:
    return HierarchyState(3, 0, 0, 1, 1)

def hierarchy_state_109() -> HierarchyState:
    return HierarchyState(4, 1, 1, 0, 1)

def hierarchy_state_110() -> HierarchyState:
    return HierarchyState(0, 2, 0, 1, 1)

def hierarchy_state_111() -> HierarchyState:
    return HierarchyState(1, 0, 1, 0, 1)

def hierarchy_state_112() -> HierarchyState:
    return HierarchyState(2, 1, 0, 1, 1)

def hierarchy_state_113() -> HierarchyState:
    return HierarchyState(3, 2, 1, 0, 1)

def hierarchy_state_114() -> HierarchyState:
    return HierarchyState(4, 0, 0, 1, 1)

def hierarchy_state_115() -> HierarchyState:
    return HierarchyState(0, 1, 1, 0, 1)

def hierarchy_state_116() -> HierarchyState:
    return HierarchyState(1, 2, 0, 1, 1)

def hierarchy_state_117() -> HierarchyState:
    return HierarchyState(2, 0, 1, 0, 1)

def hierarchy_state_118() -> HierarchyState:
    return HierarchyState(3, 1, 0, 1, 1)

def hierarchy_state_119() -> HierarchyState:
    return HierarchyState(4, 2, 1, 0, 1)

def hierarchy_state_120() -> HierarchyState:
    return HierarchyState(0, 0, 0, 1, 0)

def hierarchy_state_121() -> HierarchyState:
    return HierarchyState(1, 1, 1, 0, 1)

def hierarchy_state_122() -> HierarchyState:
    return HierarchyState(2, 2, 0, 1, 1)

def hierarchy_state_123() -> HierarchyState:
    return HierarchyState(3, 0, 1, 0, 1)

def hierarchy_state_124() -> HierarchyState:
    return HierarchyState(4, 1, 0, 1, 1)

def hierarchy_state_125() -> HierarchyState:
    return HierarchyState(0, 2, 1, 0, 1)

def hierarchy_state_126() -> HierarchyState:
    return HierarchyState(1, 0, 0, 1, 0)

def hierarchy_state_127() -> HierarchyState:
    return HierarchyState(2, 1, 1, 0, 1)

def hierarchy_state_128() -> HierarchyState:
    return HierarchyState(3, 2, 0, 1, 1)

def hierarchy_state_129() -> HierarchyState:
    return HierarchyState(4, 0, 1, 0, 1)

def hierarchy_state_130() -> HierarchyState:
    return HierarchyState(0, 1, 0, 1, 1)

def hierarchy_state_131() -> HierarchyState:
    return HierarchyState(1, 2, 1, 0, 1)

def hierarchy_state_132() -> HierarchyState:
    return HierarchyState(2, 0, 0, 1, 1)

def hierarchy_state_133() -> HierarchyState:
    return HierarchyState(3, 1, 1, 0, 1)

def hierarchy_state_134() -> HierarchyState:
    return HierarchyState(4, 2, 0, 1, 1)

def hierarchy_state_135() -> HierarchyState:
    return HierarchyState(0, 0, 1, 0, 1)

def hierarchy_state_136() -> HierarchyState:
    return HierarchyState(1, 1, 0, 1, 1)

def hierarchy_state_137() -> HierarchyState:
    return HierarchyState(2, 2, 1, 0, 1)

def hierarchy_state_138() -> HierarchyState:
    return HierarchyState(3, 0, 0, 1, 1)

def hierarchy_state_139() -> HierarchyState:
    return HierarchyState(4, 1, 1, 0, 1)

def hierarchy_state_140() -> HierarchyState:
    return HierarchyState(0, 2, 0, 1, 1)

def hierarchy_state_141() -> HierarchyState:
    return HierarchyState(1, 0, 1, 0, 1)

def hierarchy_state_142() -> HierarchyState:
    return HierarchyState(2, 1, 0, 1, 1)

def hierarchy_state_143() -> HierarchyState:
    return HierarchyState(3, 2, 1, 0, 1)

def hierarchy_state_144() -> HierarchyState:
    return HierarchyState(4, 0, 0, 1, 1)

def hierarchy_state_145() -> HierarchyState:
    return HierarchyState(0, 1, 1, 0, 1)

def hierarchy_state_146() -> HierarchyState:
    return HierarchyState(1, 2, 0, 1, 1)

def hierarchy_state_147() -> HierarchyState:
    return HierarchyState(2, 0, 1, 0, 1)

def hierarchy_state_148() -> HierarchyState:
    return HierarchyState(3, 1, 0, 1, 1)

def hierarchy_state_149() -> HierarchyState:
    return HierarchyState(4, 2, 1, 0, 1)

def hierarchy_state_150() -> HierarchyState:
    return HierarchyState(0, 0, 0, 1, 0)

def hierarchy_state_151() -> HierarchyState:
    return HierarchyState(1, 1, 1, 0, 1)

def hierarchy_state_152() -> HierarchyState:
    return HierarchyState(2, 2, 0, 1, 1)

def hierarchy_state_153() -> HierarchyState:
    return HierarchyState(3, 0, 1, 0, 1)

def hierarchy_state_154() -> HierarchyState:
    return HierarchyState(4, 1, 0, 1, 1)

def hierarchy_state_155() -> HierarchyState:
    return HierarchyState(0, 2, 1, 0, 1)

def hierarchy_state_156() -> HierarchyState:
    return HierarchyState(1, 0, 0, 1, 0)

def hierarchy_state_157() -> HierarchyState:
    return HierarchyState(2, 1, 1, 0, 1)

def hierarchy_state_158() -> HierarchyState:
    return HierarchyState(3, 2, 0, 1, 1)

def hierarchy_state_159() -> HierarchyState:
    return HierarchyState(4, 0, 1, 0, 1)

def hierarchy_state_160() -> HierarchyState:
    return HierarchyState(0, 1, 0, 1, 1)

def hierarchy_state_161() -> HierarchyState:
    return HierarchyState(1, 2, 1, 0, 1)

def hierarchy_state_162() -> HierarchyState:
    return HierarchyState(2, 0, 0, 1, 1)

def hierarchy_state_163() -> HierarchyState:
    return HierarchyState(3, 1, 1, 0, 1)

def hierarchy_state_164() -> HierarchyState:
    return HierarchyState(4, 2, 0, 1, 1)

def hierarchy_state_165() -> HierarchyState:
    return HierarchyState(0, 0, 1, 0, 1)

def hierarchy_state_166() -> HierarchyState:
    return HierarchyState(1, 1, 0, 1, 1)

def hierarchy_state_167() -> HierarchyState:
    return HierarchyState(2, 2, 1, 0, 1)

def hierarchy_state_168() -> HierarchyState:
    return HierarchyState(3, 0, 0, 1, 1)

def hierarchy_state_169() -> HierarchyState:
    return HierarchyState(4, 1, 1, 0, 1)

def hierarchy_state_170() -> HierarchyState:
    return HierarchyState(0, 2, 0, 1, 1)

def hierarchy_state_171() -> HierarchyState:
    return HierarchyState(1, 0, 1, 0, 1)

def hierarchy_state_172() -> HierarchyState:
    return HierarchyState(2, 1, 0, 1, 1)

def hierarchy_state_173() -> HierarchyState:
    return HierarchyState(3, 2, 1, 0, 1)

def hierarchy_state_174() -> HierarchyState:
    return HierarchyState(4, 0, 0, 1, 1)

def hierarchy_state_175() -> HierarchyState:
    return HierarchyState(0, 1, 1, 0, 1)

def hierarchy_state_176() -> HierarchyState:
    return HierarchyState(1, 2, 0, 1, 1)

def hierarchy_state_177() -> HierarchyState:
    return HierarchyState(2, 0, 1, 0, 1)

def hierarchy_state_178() -> HierarchyState:
    return HierarchyState(3, 1, 0, 1, 1)

def hierarchy_state_179() -> HierarchyState:
    return HierarchyState(4, 2, 1, 0, 1)

def hierarchy_state_180() -> HierarchyState:
    return HierarchyState(0, 0, 0, 1, 0)

def hierarchy_state_181() -> HierarchyState:
    return HierarchyState(1, 1, 1, 0, 1)

def hierarchy_state_182() -> HierarchyState:
    return HierarchyState(2, 2, 0, 1, 1)

def hierarchy_state_183() -> HierarchyState:
    return HierarchyState(3, 0, 1, 0, 1)

def hierarchy_state_184() -> HierarchyState:
    return HierarchyState(4, 1, 0, 1, 1)

def hierarchy_state_185() -> HierarchyState:
    return HierarchyState(0, 2, 1, 0, 1)

def hierarchy_state_186() -> HierarchyState:
    return HierarchyState(1, 0, 0, 1, 0)

def hierarchy_state_187() -> HierarchyState:
    return HierarchyState(2, 1, 1, 0, 1)

def hierarchy_state_188() -> HierarchyState:
    return HierarchyState(3, 2, 0, 1, 1)

def hierarchy_state_189() -> HierarchyState:
    return HierarchyState(4, 0, 1, 0, 1)

def hierarchy_state_190() -> HierarchyState:
    return HierarchyState(0, 1, 0, 1, 1)

def hierarchy_state_191() -> HierarchyState:
    return HierarchyState(1, 2, 1, 0, 1)

def hierarchy_state_192() -> HierarchyState:
    return HierarchyState(2, 0, 0, 1, 1)

def hierarchy_state_193() -> HierarchyState:
    return HierarchyState(3, 1, 1, 0, 1)

def hierarchy_state_194() -> HierarchyState:
    return HierarchyState(4, 2, 0, 1, 1)

def hierarchy_state_195() -> HierarchyState:
    return HierarchyState(0, 0, 1, 0, 1)

def hierarchy_state_196() -> HierarchyState:
    return HierarchyState(1, 1, 0, 1, 1)

def hierarchy_state_197() -> HierarchyState:
    return HierarchyState(2, 2, 1, 0, 1)

def hierarchy_state_198() -> HierarchyState:
    return HierarchyState(3, 0, 0, 1, 1)

def hierarchy_state_199() -> HierarchyState:
    return HierarchyState(4, 1, 1, 0, 1)

def hierarchy_state_200() -> HierarchyState:
    return HierarchyState(0, 2, 0, 1, 1)

def hierarchy_state_201() -> HierarchyState:
    return HierarchyState(1, 0, 1, 0, 1)

def hierarchy_state_202() -> HierarchyState:
    return HierarchyState(2, 1, 0, 1, 1)

def hierarchy_state_203() -> HierarchyState:
    return HierarchyState(3, 2, 1, 0, 1)

def hierarchy_state_204() -> HierarchyState:
    return HierarchyState(4, 0, 0, 1, 1)

def hierarchy_state_205() -> HierarchyState:
    return HierarchyState(0, 1, 1, 0, 1)

def hierarchy_state_206() -> HierarchyState:
    return HierarchyState(1, 2, 0, 1, 1)

def hierarchy_state_207() -> HierarchyState:
    return HierarchyState(2, 0, 1, 0, 1)

def hierarchy_state_208() -> HierarchyState:
    return HierarchyState(3, 1, 0, 1, 1)

def hierarchy_state_209() -> HierarchyState:
    return HierarchyState(4, 2, 1, 0, 1)

def hierarchy_state_210() -> HierarchyState:
    return HierarchyState(0, 0, 0, 1, 0)

def hierarchy_state_211() -> HierarchyState:
    return HierarchyState(1, 1, 1, 0, 1)

def hierarchy_state_212() -> HierarchyState:
    return HierarchyState(2, 2, 0, 1, 1)

def hierarchy_state_213() -> HierarchyState:
    return HierarchyState(3, 0, 1, 0, 1)

def hierarchy_state_214() -> HierarchyState:
    return HierarchyState(4, 1, 0, 1, 1)

def hierarchy_state_215() -> HierarchyState:
    return HierarchyState(0, 2, 1, 0, 1)

def hierarchy_state_216() -> HierarchyState:
    return HierarchyState(1, 0, 0, 1, 0)

def hierarchy_state_217() -> HierarchyState:
    return HierarchyState(2, 1, 1, 0, 1)

def hierarchy_state_218() -> HierarchyState:
    return HierarchyState(3, 2, 0, 1, 1)

def hierarchy_state_219() -> HierarchyState:
    return HierarchyState(4, 0, 1, 0, 1)

def hierarchy_state_220() -> HierarchyState:
    return HierarchyState(0, 1, 0, 1, 1)

