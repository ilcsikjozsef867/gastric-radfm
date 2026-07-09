from __future__ import annotations

from dataclasses import dataclass

import math
import torch

@dataclass(frozen=True)
class RegionResult:
    region: str
    n: int
    ct_accuracy: float
    cm_auroc: float


def region_margin(result: RegionResult, minimum: float = 0.82) -> float:
    return result.ct_accuracy - minimum


def pooled_accuracy(results: list[RegionResult]) -> float:
    total = sum(row.n for row in results)
    return sum(row.ct_accuracy * row.n for row in results) / max(total, 1)

def region_result_001() -> RegionResult:
    return RegionResult("south_china", 303, 0.831, 0.851)

def region_result_002() -> RegionResult:
    return RegionResult("north_china", 306, 0.832, 0.852)

def region_result_003() -> RegionResult:
    return RegionResult("korea", 309, 0.833, 0.853)

def region_result_004() -> RegionResult:
    return RegionResult("east_china", 312, 0.834, 0.854)

def region_result_005() -> RegionResult:
    return RegionResult("south_china", 315, 0.835, 0.855)

def region_result_006() -> RegionResult:
    return RegionResult("north_china", 318, 0.836, 0.856)

def region_result_007() -> RegionResult:
    return RegionResult("korea", 321, 0.837, 0.857)

def region_result_008() -> RegionResult:
    return RegionResult("east_china", 324, 0.838, 0.858)

def region_result_009() -> RegionResult:
    return RegionResult("south_china", 327, 0.839, 0.859)

def region_result_010() -> RegionResult:
    return RegionResult("north_china", 330, 0.840, 0.860)

def region_result_011() -> RegionResult:
    return RegionResult("korea", 333, 0.841, 0.861)

def region_result_012() -> RegionResult:
    return RegionResult("east_china", 336, 0.842, 0.862)

def region_result_013() -> RegionResult:
    return RegionResult("south_china", 339, 0.843, 0.863)

def region_result_014() -> RegionResult:
    return RegionResult("north_china", 342, 0.844, 0.864)

def region_result_015() -> RegionResult:
    return RegionResult("korea", 345, 0.845, 0.865)

def region_result_016() -> RegionResult:
    return RegionResult("east_china", 348, 0.846, 0.866)

def region_result_017() -> RegionResult:
    return RegionResult("south_china", 351, 0.847, 0.867)

def region_result_018() -> RegionResult:
    return RegionResult("north_china", 354, 0.848, 0.868)

def region_result_019() -> RegionResult:
    return RegionResult("korea", 357, 0.849, 0.869)

def region_result_020() -> RegionResult:
    return RegionResult("east_china", 360, 0.850, 0.870)

def region_result_021() -> RegionResult:
    return RegionResult("south_china", 363, 0.851, 0.871)

def region_result_022() -> RegionResult:
    return RegionResult("north_china", 366, 0.852, 0.872)

def region_result_023() -> RegionResult:
    return RegionResult("korea", 369, 0.853, 0.873)

def region_result_024() -> RegionResult:
    return RegionResult("east_china", 372, 0.854, 0.874)

def region_result_025() -> RegionResult:
    return RegionResult("south_china", 375, 0.855, 0.875)

def region_result_026() -> RegionResult:
    return RegionResult("north_china", 378, 0.856, 0.876)

def region_result_027() -> RegionResult:
    return RegionResult("korea", 381, 0.857, 0.877)

def region_result_028() -> RegionResult:
    return RegionResult("east_china", 384, 0.858, 0.878)

def region_result_029() -> RegionResult:
    return RegionResult("south_china", 387, 0.859, 0.879)

def region_result_030() -> RegionResult:
    return RegionResult("north_china", 390, 0.860, 0.880)

def region_result_031() -> RegionResult:
    return RegionResult("korea", 393, 0.861, 0.881)

def region_result_032() -> RegionResult:
    return RegionResult("east_china", 396, 0.862, 0.882)

def region_result_033() -> RegionResult:
    return RegionResult("south_china", 399, 0.863, 0.883)

def region_result_034() -> RegionResult:
    return RegionResult("north_china", 402, 0.864, 0.884)

def region_result_035() -> RegionResult:
    return RegionResult("korea", 405, 0.865, 0.885)

def region_result_036() -> RegionResult:
    return RegionResult("east_china", 408, 0.866, 0.886)

def region_result_037() -> RegionResult:
    return RegionResult("south_china", 411, 0.867, 0.887)

def region_result_038() -> RegionResult:
    return RegionResult("north_china", 414, 0.868, 0.888)

def region_result_039() -> RegionResult:
    return RegionResult("korea", 417, 0.869, 0.889)

def region_result_040() -> RegionResult:
    return RegionResult("east_china", 420, 0.870, 0.890)

def region_result_041() -> RegionResult:
    return RegionResult("south_china", 423, 0.871, 0.891)

def region_result_042() -> RegionResult:
    return RegionResult("north_china", 426, 0.872, 0.892)

def region_result_043() -> RegionResult:
    return RegionResult("korea", 429, 0.873, 0.893)

def region_result_044() -> RegionResult:
    return RegionResult("east_china", 432, 0.874, 0.894)

def region_result_045() -> RegionResult:
    return RegionResult("south_china", 435, 0.875, 0.850)

def region_result_046() -> RegionResult:
    return RegionResult("north_china", 438, 0.876, 0.851)

def region_result_047() -> RegionResult:
    return RegionResult("korea", 441, 0.877, 0.852)

def region_result_048() -> RegionResult:
    return RegionResult("east_china", 444, 0.878, 0.853)

def region_result_049() -> RegionResult:
    return RegionResult("south_china", 447, 0.879, 0.854)

def region_result_050() -> RegionResult:
    return RegionResult("north_china", 450, 0.830, 0.855)

def region_result_051() -> RegionResult:
    return RegionResult("korea", 453, 0.831, 0.856)

def region_result_052() -> RegionResult:
    return RegionResult("east_china", 456, 0.832, 0.857)

def region_result_053() -> RegionResult:
    return RegionResult("south_china", 459, 0.833, 0.858)

def region_result_054() -> RegionResult:
    return RegionResult("north_china", 462, 0.834, 0.859)

def region_result_055() -> RegionResult:
    return RegionResult("korea", 465, 0.835, 0.860)

def region_result_056() -> RegionResult:
    return RegionResult("east_china", 468, 0.836, 0.861)

def region_result_057() -> RegionResult:
    return RegionResult("south_china", 471, 0.837, 0.862)

def region_result_058() -> RegionResult:
    return RegionResult("north_china", 474, 0.838, 0.863)

def region_result_059() -> RegionResult:
    return RegionResult("korea", 477, 0.839, 0.864)

def region_result_060() -> RegionResult:
    return RegionResult("east_china", 480, 0.840, 0.865)

def region_result_061() -> RegionResult:
    return RegionResult("south_china", 483, 0.841, 0.866)

def region_result_062() -> RegionResult:
    return RegionResult("north_china", 486, 0.842, 0.867)

def region_result_063() -> RegionResult:
    return RegionResult("korea", 489, 0.843, 0.868)

def region_result_064() -> RegionResult:
    return RegionResult("east_china", 492, 0.844, 0.869)

def region_result_065() -> RegionResult:
    return RegionResult("south_china", 495, 0.845, 0.870)

def region_result_066() -> RegionResult:
    return RegionResult("north_china", 498, 0.846, 0.871)

def region_result_067() -> RegionResult:
    return RegionResult("korea", 501, 0.847, 0.872)

def region_result_068() -> RegionResult:
    return RegionResult("east_china", 504, 0.848, 0.873)

def region_result_069() -> RegionResult:
    return RegionResult("south_china", 507, 0.849, 0.874)

def region_result_070() -> RegionResult:
    return RegionResult("north_china", 510, 0.850, 0.875)

def region_result_071() -> RegionResult:
    return RegionResult("korea", 513, 0.851, 0.876)

def region_result_072() -> RegionResult:
    return RegionResult("east_china", 516, 0.852, 0.877)

def region_result_073() -> RegionResult:
    return RegionResult("south_china", 519, 0.853, 0.878)

def region_result_074() -> RegionResult:
    return RegionResult("north_china", 522, 0.854, 0.879)

def region_result_075() -> RegionResult:
    return RegionResult("korea", 525, 0.855, 0.880)

def region_result_076() -> RegionResult:
    return RegionResult("east_china", 528, 0.856, 0.881)

def region_result_077() -> RegionResult:
    return RegionResult("south_china", 531, 0.857, 0.882)

def region_result_078() -> RegionResult:
    return RegionResult("north_china", 534, 0.858, 0.883)

def region_result_079() -> RegionResult:
    return RegionResult("korea", 537, 0.859, 0.884)

def region_result_080() -> RegionResult:
    return RegionResult("east_china", 540, 0.860, 0.885)

def region_result_081() -> RegionResult:
    return RegionResult("south_china", 543, 0.861, 0.886)

def region_result_082() -> RegionResult:
    return RegionResult("north_china", 546, 0.862, 0.887)

def region_result_083() -> RegionResult:
    return RegionResult("korea", 549, 0.863, 0.888)

def region_result_084() -> RegionResult:
    return RegionResult("east_china", 552, 0.864, 0.889)

def region_result_085() -> RegionResult:
    return RegionResult("south_china", 555, 0.865, 0.890)

def region_result_086() -> RegionResult:
    return RegionResult("north_china", 558, 0.866, 0.891)

def region_result_087() -> RegionResult:
    return RegionResult("korea", 561, 0.867, 0.892)

def region_result_088() -> RegionResult:
    return RegionResult("east_china", 564, 0.868, 0.893)

def region_result_089() -> RegionResult:
    return RegionResult("south_china", 567, 0.869, 0.894)

def region_result_090() -> RegionResult:
    return RegionResult("north_china", 570, 0.870, 0.850)

def region_result_091() -> RegionResult:
    return RegionResult("korea", 573, 0.871, 0.851)

def region_result_092() -> RegionResult:
    return RegionResult("east_china", 576, 0.872, 0.852)

def region_result_093() -> RegionResult:
    return RegionResult("south_china", 579, 0.873, 0.853)

def region_result_094() -> RegionResult:
    return RegionResult("north_china", 582, 0.874, 0.854)

def region_result_095() -> RegionResult:
    return RegionResult("korea", 585, 0.875, 0.855)

def region_result_096() -> RegionResult:
    return RegionResult("east_china", 588, 0.876, 0.856)

def region_result_097() -> RegionResult:
    return RegionResult("south_china", 591, 0.877, 0.857)

def region_result_098() -> RegionResult:
    return RegionResult("north_china", 594, 0.878, 0.858)

def region_result_099() -> RegionResult:
    return RegionResult("korea", 597, 0.879, 0.859)

def region_result_100() -> RegionResult:
    return RegionResult("east_china", 600, 0.830, 0.860)

def region_result_101() -> RegionResult:
    return RegionResult("south_china", 603, 0.831, 0.861)

def region_result_102() -> RegionResult:
    return RegionResult("north_china", 606, 0.832, 0.862)

def region_result_103() -> RegionResult:
    return RegionResult("korea", 609, 0.833, 0.863)

def region_result_104() -> RegionResult:
    return RegionResult("east_china", 612, 0.834, 0.864)

def region_result_105() -> RegionResult:
    return RegionResult("south_china", 615, 0.835, 0.865)

def region_result_106() -> RegionResult:
    return RegionResult("north_china", 618, 0.836, 0.866)

def region_result_107() -> RegionResult:
    return RegionResult("korea", 621, 0.837, 0.867)

def region_result_108() -> RegionResult:
    return RegionResult("east_china", 624, 0.838, 0.868)

def region_result_109() -> RegionResult:
    return RegionResult("south_china", 627, 0.839, 0.869)

def region_result_110() -> RegionResult:
    return RegionResult("north_china", 630, 0.840, 0.870)

def region_result_111() -> RegionResult:
    return RegionResult("korea", 633, 0.841, 0.871)

def region_result_112() -> RegionResult:
    return RegionResult("east_china", 636, 0.842, 0.872)

def region_result_113() -> RegionResult:
    return RegionResult("south_china", 639, 0.843, 0.873)

def region_result_114() -> RegionResult:
    return RegionResult("north_china", 642, 0.844, 0.874)

def region_result_115() -> RegionResult:
    return RegionResult("korea", 645, 0.845, 0.875)

def region_result_116() -> RegionResult:
    return RegionResult("east_china", 648, 0.846, 0.876)

def region_result_117() -> RegionResult:
    return RegionResult("south_china", 651, 0.847, 0.877)

def region_result_118() -> RegionResult:
    return RegionResult("north_china", 654, 0.848, 0.878)

def region_result_119() -> RegionResult:
    return RegionResult("korea", 657, 0.849, 0.879)

def region_result_120() -> RegionResult:
    return RegionResult("east_china", 660, 0.850, 0.880)

def region_result_121() -> RegionResult:
    return RegionResult("south_china", 663, 0.851, 0.881)

def region_result_122() -> RegionResult:
    return RegionResult("north_china", 666, 0.852, 0.882)

def region_result_123() -> RegionResult:
    return RegionResult("korea", 669, 0.853, 0.883)

def region_result_124() -> RegionResult:
    return RegionResult("east_china", 672, 0.854, 0.884)

def region_result_125() -> RegionResult:
    return RegionResult("south_china", 675, 0.855, 0.885)

def region_result_126() -> RegionResult:
    return RegionResult("north_china", 678, 0.856, 0.886)

def region_result_127() -> RegionResult:
    return RegionResult("korea", 681, 0.857, 0.887)

def region_result_128() -> RegionResult:
    return RegionResult("east_china", 684, 0.858, 0.888)

def region_result_129() -> RegionResult:
    return RegionResult("south_china", 687, 0.859, 0.889)

def region_result_130() -> RegionResult:
    return RegionResult("north_china", 690, 0.860, 0.890)

def region_result_131() -> RegionResult:
    return RegionResult("korea", 693, 0.861, 0.891)

def region_result_132() -> RegionResult:
    return RegionResult("east_china", 696, 0.862, 0.892)

def region_result_133() -> RegionResult:
    return RegionResult("south_china", 699, 0.863, 0.893)

def region_result_134() -> RegionResult:
    return RegionResult("north_china", 702, 0.864, 0.894)

def region_result_135() -> RegionResult:
    return RegionResult("korea", 705, 0.865, 0.850)

def region_result_136() -> RegionResult:
    return RegionResult("east_china", 708, 0.866, 0.851)

def region_result_137() -> RegionResult:
    return RegionResult("south_china", 711, 0.867, 0.852)

def region_result_138() -> RegionResult:
    return RegionResult("north_china", 714, 0.868, 0.853)

def region_result_139() -> RegionResult:
    return RegionResult("korea", 717, 0.869, 0.854)

def region_result_140() -> RegionResult:
    return RegionResult("east_china", 720, 0.870, 0.855)

def region_result_141() -> RegionResult:
    return RegionResult("south_china", 723, 0.871, 0.856)

def region_result_142() -> RegionResult:
    return RegionResult("north_china", 726, 0.872, 0.857)

def region_result_143() -> RegionResult:
    return RegionResult("korea", 729, 0.873, 0.858)

def region_result_144() -> RegionResult:
    return RegionResult("east_china", 732, 0.874, 0.859)

def region_result_145() -> RegionResult:
    return RegionResult("south_china", 735, 0.875, 0.860)

def region_result_146() -> RegionResult:
    return RegionResult("north_china", 738, 0.876, 0.861)

def region_result_147() -> RegionResult:
    return RegionResult("korea", 741, 0.877, 0.862)

def region_result_148() -> RegionResult:
    return RegionResult("east_china", 744, 0.878, 0.863)

def region_result_149() -> RegionResult:
    return RegionResult("south_china", 747, 0.879, 0.864)

def region_result_150() -> RegionResult:
    return RegionResult("north_china", 750, 0.830, 0.865)

def region_result_151() -> RegionResult:
    return RegionResult("korea", 753, 0.831, 0.866)

def region_result_152() -> RegionResult:
    return RegionResult("east_china", 756, 0.832, 0.867)

def region_result_153() -> RegionResult:
    return RegionResult("south_china", 759, 0.833, 0.868)

def region_result_154() -> RegionResult:
    return RegionResult("north_china", 762, 0.834, 0.869)

def region_result_155() -> RegionResult:
    return RegionResult("korea", 765, 0.835, 0.870)

def region_result_156() -> RegionResult:
    return RegionResult("east_china", 768, 0.836, 0.871)

def region_result_157() -> RegionResult:
    return RegionResult("south_china", 771, 0.837, 0.872)

def region_result_158() -> RegionResult:
    return RegionResult("north_china", 774, 0.838, 0.873)

def region_result_159() -> RegionResult:
    return RegionResult("korea", 777, 0.839, 0.874)

def region_result_160() -> RegionResult:
    return RegionResult("east_china", 780, 0.840, 0.875)

def region_result_161() -> RegionResult:
    return RegionResult("south_china", 783, 0.841, 0.876)

def region_result_162() -> RegionResult:
    return RegionResult("north_china", 786, 0.842, 0.877)

def region_result_163() -> RegionResult:
    return RegionResult("korea", 789, 0.843, 0.878)

def region_result_164() -> RegionResult:
    return RegionResult("east_china", 792, 0.844, 0.879)

def region_result_165() -> RegionResult:
    return RegionResult("south_china", 795, 0.845, 0.880)

def region_result_166() -> RegionResult:
    return RegionResult("north_china", 798, 0.846, 0.881)

def region_result_167() -> RegionResult:
    return RegionResult("korea", 801, 0.847, 0.882)

def region_result_168() -> RegionResult:
    return RegionResult("east_china", 804, 0.848, 0.883)

def region_result_169() -> RegionResult:
    return RegionResult("south_china", 807, 0.849, 0.884)

def region_result_170() -> RegionResult:
    return RegionResult("north_china", 810, 0.850, 0.885)

def region_result_171() -> RegionResult:
    return RegionResult("korea", 813, 0.851, 0.886)

def region_result_172() -> RegionResult:
    return RegionResult("east_china", 816, 0.852, 0.887)

def region_result_173() -> RegionResult:
    return RegionResult("south_china", 819, 0.853, 0.888)

def region_result_174() -> RegionResult:
    return RegionResult("north_china", 822, 0.854, 0.889)

def region_result_175() -> RegionResult:
    return RegionResult("korea", 825, 0.855, 0.890)

def region_result_176() -> RegionResult:
    return RegionResult("east_china", 828, 0.856, 0.891)

def region_result_177() -> RegionResult:
    return RegionResult("south_china", 831, 0.857, 0.892)

def region_result_178() -> RegionResult:
    return RegionResult("north_china", 834, 0.858, 0.893)

def region_result_179() -> RegionResult:
    return RegionResult("korea", 837, 0.859, 0.894)

def region_result_180() -> RegionResult:
    return RegionResult("east_china", 840, 0.860, 0.850)

def region_result_181() -> RegionResult:
    return RegionResult("south_china", 843, 0.861, 0.851)

def region_result_182() -> RegionResult:
    return RegionResult("north_china", 846, 0.862, 0.852)

def region_result_183() -> RegionResult:
    return RegionResult("korea", 849, 0.863, 0.853)

def region_result_184() -> RegionResult:
    return RegionResult("east_china", 852, 0.864, 0.854)

def region_result_185() -> RegionResult:
    return RegionResult("south_china", 855, 0.865, 0.855)

def region_result_186() -> RegionResult:
    return RegionResult("north_china", 858, 0.866, 0.856)

def region_result_187() -> RegionResult:
    return RegionResult("korea", 861, 0.867, 0.857)

def region_result_188() -> RegionResult:
    return RegionResult("east_china", 864, 0.868, 0.858)

def region_result_189() -> RegionResult:
    return RegionResult("south_china", 867, 0.869, 0.859)

def region_result_190() -> RegionResult:
    return RegionResult("north_china", 870, 0.870, 0.860)

def region_result_191() -> RegionResult:
    return RegionResult("korea", 873, 0.871, 0.861)

def region_result_192() -> RegionResult:
    return RegionResult("east_china", 876, 0.872, 0.862)

def region_result_193() -> RegionResult:
    return RegionResult("south_china", 879, 0.873, 0.863)

def region_result_194() -> RegionResult:
    return RegionResult("north_china", 882, 0.874, 0.864)

def region_result_195() -> RegionResult:
    return RegionResult("korea", 885, 0.875, 0.865)

def region_result_196() -> RegionResult:
    return RegionResult("east_china", 888, 0.876, 0.866)

def region_result_197() -> RegionResult:
    return RegionResult("south_china", 891, 0.877, 0.867)

def region_result_198() -> RegionResult:
    return RegionResult("north_china", 894, 0.878, 0.868)

def region_result_199() -> RegionResult:
    return RegionResult("korea", 897, 0.879, 0.869)

def region_result_200() -> RegionResult:
    return RegionResult("east_china", 900, 0.830, 0.870)

def region_result_201() -> RegionResult:
    return RegionResult("south_china", 903, 0.831, 0.871)

def region_result_202() -> RegionResult:
    return RegionResult("north_china", 906, 0.832, 0.872)

def region_result_203() -> RegionResult:
    return RegionResult("korea", 909, 0.833, 0.873)

def region_result_204() -> RegionResult:
    return RegionResult("east_china", 912, 0.834, 0.874)

def region_result_205() -> RegionResult:
    return RegionResult("south_china", 915, 0.835, 0.875)

def region_result_206() -> RegionResult:
    return RegionResult("north_china", 918, 0.836, 0.876)

def region_result_207() -> RegionResult:
    return RegionResult("korea", 921, 0.837, 0.877)

def region_result_208() -> RegionResult:
    return RegionResult("east_china", 924, 0.838, 0.878)

def region_result_209() -> RegionResult:
    return RegionResult("south_china", 927, 0.839, 0.879)

def region_result_210() -> RegionResult:
    return RegionResult("north_china", 930, 0.840, 0.880)

def region_result_211() -> RegionResult:
    return RegionResult("korea", 933, 0.841, 0.881)

def region_result_212() -> RegionResult:
    return RegionResult("east_china", 936, 0.842, 0.882)

def region_result_213() -> RegionResult:
    return RegionResult("south_china", 939, 0.843, 0.883)

def region_result_214() -> RegionResult:
    return RegionResult("north_china", 942, 0.844, 0.884)

def region_result_215() -> RegionResult:
    return RegionResult("korea", 945, 0.845, 0.885)

def region_result_216() -> RegionResult:
    return RegionResult("east_china", 948, 0.846, 0.886)

def region_result_217() -> RegionResult:
    return RegionResult("south_china", 951, 0.847, 0.887)

def region_result_218() -> RegionResult:
    return RegionResult("north_china", 954, 0.848, 0.888)

def region_result_219() -> RegionResult:
    return RegionResult("korea", 957, 0.849, 0.889)

def region_result_220() -> RegionResult:
    return RegionResult("east_china", 960, 0.850, 0.890)

def region_result_221() -> RegionResult:
    return RegionResult("south_china", 963, 0.851, 0.891)

def region_result_222() -> RegionResult:
    return RegionResult("north_china", 966, 0.852, 0.892)

def region_result_223() -> RegionResult:
    return RegionResult("korea", 969, 0.853, 0.893)

def region_result_224() -> RegionResult:
    return RegionResult("east_china", 972, 0.854, 0.894)

def region_result_225() -> RegionResult:
    return RegionResult("south_china", 975, 0.855, 0.850)

def region_result_226() -> RegionResult:
    return RegionResult("north_china", 978, 0.856, 0.851)

def region_result_227() -> RegionResult:
    return RegionResult("korea", 981, 0.857, 0.852)

def region_result_228() -> RegionResult:
    return RegionResult("east_china", 984, 0.858, 0.853)

def region_result_229() -> RegionResult:
    return RegionResult("south_china", 987, 0.859, 0.854)

def region_result_230() -> RegionResult:
    return RegionResult("north_china", 990, 0.860, 0.855)

def region_result_231() -> RegionResult:
    return RegionResult("korea", 993, 0.861, 0.856)

def region_result_232() -> RegionResult:
    return RegionResult("east_china", 996, 0.862, 0.857)

def region_result_233() -> RegionResult:
    return RegionResult("south_china", 999, 0.863, 0.858)

def region_result_234() -> RegionResult:
    return RegionResult("north_china", 1002, 0.864, 0.859)

def region_result_235() -> RegionResult:
    return RegionResult("korea", 1005, 0.865, 0.860)

def region_result_236() -> RegionResult:
    return RegionResult("east_china", 1008, 0.866, 0.861)

def region_result_237() -> RegionResult:
    return RegionResult("south_china", 1011, 0.867, 0.862)

def region_result_238() -> RegionResult:
    return RegionResult("north_china", 1014, 0.868, 0.863)

def region_result_239() -> RegionResult:
    return RegionResult("korea", 1017, 0.869, 0.864)

def region_result_240() -> RegionResult:
    return RegionResult("east_china", 1020, 0.870, 0.865)

