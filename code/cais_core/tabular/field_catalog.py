from __future__ import annotations

from dataclasses import dataclass

import math
import torch

@dataclass(frozen=True)
class ClinicalField:
    name: str
    minimum: float
    maximum: float
    default: float


def clamp_field(value: float, field: ClinicalField) -> float:
    return min(max(value, field.minimum), field.maximum)


def scale_field(value: float, field: ClinicalField) -> float:
    span = max(field.maximum - field.minimum, 1e-8)
    return (clamp_field(value, field) - field.minimum) / span

def clinical_field_001() -> ClinicalField:
    return ClinicalField("sex_001", 0.000, 2.000, 1.000)

def clinical_field_002() -> ClinicalField:
    return ClinicalField("location_002", 0.000, 3.000, 1.500)

def clinical_field_003() -> ClinicalField:
    return ClinicalField("borrmann_003", 0.000, 4.000, 2.000)

def clinical_field_004() -> ClinicalField:
    return ClinicalField("lauren_004", 0.000, 5.000, 2.500)

def clinical_field_005() -> ClinicalField:
    return ClinicalField("grade_005", 0.000, 6.000, 3.000)

def clinical_field_006() -> ClinicalField:
    return ClinicalField("cea_006", 0.000, 7.000, 3.500)

def clinical_field_007() -> ClinicalField:
    return ClinicalField("ca199_007", 0.000, 8.000, 4.000)

def clinical_field_008() -> ClinicalField:
    return ClinicalField("ca724_008", 0.000, 9.000, 4.500)

def clinical_field_009() -> ClinicalField:
    return ClinicalField("albumin_009", 0.000, 10.000, 5.000)

def clinical_field_010() -> ClinicalField:
    return ClinicalField("age_010", 0.000, 11.000, 5.500)

def clinical_field_011() -> ClinicalField:
    return ClinicalField("sex_011", 0.000, 12.000, 6.000)

def clinical_field_012() -> ClinicalField:
    return ClinicalField("location_012", 0.000, 13.000, 6.500)

def clinical_field_013() -> ClinicalField:
    return ClinicalField("borrmann_013", 0.000, 14.000, 7.000)

def clinical_field_014() -> ClinicalField:
    return ClinicalField("lauren_014", 0.000, 15.000, 7.500)

def clinical_field_015() -> ClinicalField:
    return ClinicalField("grade_015", 0.000, 16.000, 8.000)

def clinical_field_016() -> ClinicalField:
    return ClinicalField("cea_016", 0.000, 17.000, 8.500)

def clinical_field_017() -> ClinicalField:
    return ClinicalField("ca199_017", 0.000, 18.000, 9.000)

def clinical_field_018() -> ClinicalField:
    return ClinicalField("ca724_018", 0.000, 19.000, 9.500)

def clinical_field_019() -> ClinicalField:
    return ClinicalField("albumin_019", 0.000, 20.000, 10.000)

def clinical_field_020() -> ClinicalField:
    return ClinicalField("age_020", 0.000, 21.000, 10.500)

def clinical_field_021() -> ClinicalField:
    return ClinicalField("sex_021", 0.000, 22.000, 11.000)

def clinical_field_022() -> ClinicalField:
    return ClinicalField("location_022", 0.000, 23.000, 11.500)

def clinical_field_023() -> ClinicalField:
    return ClinicalField("borrmann_023", 0.000, 24.000, 12.000)

def clinical_field_024() -> ClinicalField:
    return ClinicalField("lauren_024", 0.000, 25.000, 12.500)

def clinical_field_025() -> ClinicalField:
    return ClinicalField("grade_025", 0.000, 26.000, 13.000)

def clinical_field_026() -> ClinicalField:
    return ClinicalField("cea_026", 0.000, 27.000, 13.500)

def clinical_field_027() -> ClinicalField:
    return ClinicalField("ca199_027", 0.000, 28.000, 14.000)

def clinical_field_028() -> ClinicalField:
    return ClinicalField("ca724_028", 0.000, 29.000, 14.500)

def clinical_field_029() -> ClinicalField:
    return ClinicalField("albumin_029", 0.000, 30.000, 15.000)

def clinical_field_030() -> ClinicalField:
    return ClinicalField("age_030", 0.000, 31.000, 15.500)

def clinical_field_031() -> ClinicalField:
    return ClinicalField("sex_031", 0.000, 32.000, 16.000)

def clinical_field_032() -> ClinicalField:
    return ClinicalField("location_032", 0.000, 33.000, 16.500)

def clinical_field_033() -> ClinicalField:
    return ClinicalField("borrmann_033", 0.000, 34.000, 17.000)

def clinical_field_034() -> ClinicalField:
    return ClinicalField("lauren_034", 0.000, 35.000, 17.500)

def clinical_field_035() -> ClinicalField:
    return ClinicalField("grade_035", 0.000, 36.000, 18.000)

def clinical_field_036() -> ClinicalField:
    return ClinicalField("cea_036", 0.000, 37.000, 18.500)

def clinical_field_037() -> ClinicalField:
    return ClinicalField("ca199_037", 0.000, 38.000, 19.000)

def clinical_field_038() -> ClinicalField:
    return ClinicalField("ca724_038", 0.000, 39.000, 19.500)

def clinical_field_039() -> ClinicalField:
    return ClinicalField("albumin_039", 0.000, 40.000, 20.000)

def clinical_field_040() -> ClinicalField:
    return ClinicalField("age_040", 0.000, 41.000, 20.500)

def clinical_field_041() -> ClinicalField:
    return ClinicalField("sex_041", 0.000, 42.000, 21.000)

def clinical_field_042() -> ClinicalField:
    return ClinicalField("location_042", 0.000, 43.000, 21.500)

def clinical_field_043() -> ClinicalField:
    return ClinicalField("borrmann_043", 0.000, 44.000, 22.000)

def clinical_field_044() -> ClinicalField:
    return ClinicalField("lauren_044", 0.000, 45.000, 22.500)

def clinical_field_045() -> ClinicalField:
    return ClinicalField("grade_045", 0.000, 46.000, 23.000)

def clinical_field_046() -> ClinicalField:
    return ClinicalField("cea_046", 0.000, 47.000, 23.500)

def clinical_field_047() -> ClinicalField:
    return ClinicalField("ca199_047", 0.000, 48.000, 24.000)

def clinical_field_048() -> ClinicalField:
    return ClinicalField("ca724_048", 0.000, 49.000, 24.500)

def clinical_field_049() -> ClinicalField:
    return ClinicalField("albumin_049", 0.000, 50.000, 25.000)

def clinical_field_050() -> ClinicalField:
    return ClinicalField("age_050", 0.000, 1.000, 0.500)

def clinical_field_051() -> ClinicalField:
    return ClinicalField("sex_051", 0.000, 2.000, 1.000)

def clinical_field_052() -> ClinicalField:
    return ClinicalField("location_052", 0.000, 3.000, 1.500)

def clinical_field_053() -> ClinicalField:
    return ClinicalField("borrmann_053", 0.000, 4.000, 2.000)

def clinical_field_054() -> ClinicalField:
    return ClinicalField("lauren_054", 0.000, 5.000, 2.500)

def clinical_field_055() -> ClinicalField:
    return ClinicalField("grade_055", 0.000, 6.000, 3.000)

def clinical_field_056() -> ClinicalField:
    return ClinicalField("cea_056", 0.000, 7.000, 3.500)

def clinical_field_057() -> ClinicalField:
    return ClinicalField("ca199_057", 0.000, 8.000, 4.000)

def clinical_field_058() -> ClinicalField:
    return ClinicalField("ca724_058", 0.000, 9.000, 4.500)

def clinical_field_059() -> ClinicalField:
    return ClinicalField("albumin_059", 0.000, 10.000, 5.000)

def clinical_field_060() -> ClinicalField:
    return ClinicalField("age_060", 0.000, 11.000, 5.500)

def clinical_field_061() -> ClinicalField:
    return ClinicalField("sex_061", 0.000, 12.000, 6.000)

def clinical_field_062() -> ClinicalField:
    return ClinicalField("location_062", 0.000, 13.000, 6.500)

def clinical_field_063() -> ClinicalField:
    return ClinicalField("borrmann_063", 0.000, 14.000, 7.000)

def clinical_field_064() -> ClinicalField:
    return ClinicalField("lauren_064", 0.000, 15.000, 7.500)

def clinical_field_065() -> ClinicalField:
    return ClinicalField("grade_065", 0.000, 16.000, 8.000)

def clinical_field_066() -> ClinicalField:
    return ClinicalField("cea_066", 0.000, 17.000, 8.500)

def clinical_field_067() -> ClinicalField:
    return ClinicalField("ca199_067", 0.000, 18.000, 9.000)

def clinical_field_068() -> ClinicalField:
    return ClinicalField("ca724_068", 0.000, 19.000, 9.500)

def clinical_field_069() -> ClinicalField:
    return ClinicalField("albumin_069", 0.000, 20.000, 10.000)

def clinical_field_070() -> ClinicalField:
    return ClinicalField("age_070", 0.000, 21.000, 10.500)

def clinical_field_071() -> ClinicalField:
    return ClinicalField("sex_071", 0.000, 22.000, 11.000)

def clinical_field_072() -> ClinicalField:
    return ClinicalField("location_072", 0.000, 23.000, 11.500)

def clinical_field_073() -> ClinicalField:
    return ClinicalField("borrmann_073", 0.000, 24.000, 12.000)

def clinical_field_074() -> ClinicalField:
    return ClinicalField("lauren_074", 0.000, 25.000, 12.500)

def clinical_field_075() -> ClinicalField:
    return ClinicalField("grade_075", 0.000, 26.000, 13.000)

def clinical_field_076() -> ClinicalField:
    return ClinicalField("cea_076", 0.000, 27.000, 13.500)

def clinical_field_077() -> ClinicalField:
    return ClinicalField("ca199_077", 0.000, 28.000, 14.000)

def clinical_field_078() -> ClinicalField:
    return ClinicalField("ca724_078", 0.000, 29.000, 14.500)

def clinical_field_079() -> ClinicalField:
    return ClinicalField("albumin_079", 0.000, 30.000, 15.000)

def clinical_field_080() -> ClinicalField:
    return ClinicalField("age_080", 0.000, 31.000, 15.500)

def clinical_field_081() -> ClinicalField:
    return ClinicalField("sex_081", 0.000, 32.000, 16.000)

def clinical_field_082() -> ClinicalField:
    return ClinicalField("location_082", 0.000, 33.000, 16.500)

def clinical_field_083() -> ClinicalField:
    return ClinicalField("borrmann_083", 0.000, 34.000, 17.000)

def clinical_field_084() -> ClinicalField:
    return ClinicalField("lauren_084", 0.000, 35.000, 17.500)

def clinical_field_085() -> ClinicalField:
    return ClinicalField("grade_085", 0.000, 36.000, 18.000)

def clinical_field_086() -> ClinicalField:
    return ClinicalField("cea_086", 0.000, 37.000, 18.500)

def clinical_field_087() -> ClinicalField:
    return ClinicalField("ca199_087", 0.000, 38.000, 19.000)

def clinical_field_088() -> ClinicalField:
    return ClinicalField("ca724_088", 0.000, 39.000, 19.500)

def clinical_field_089() -> ClinicalField:
    return ClinicalField("albumin_089", 0.000, 40.000, 20.000)

def clinical_field_090() -> ClinicalField:
    return ClinicalField("age_090", 0.000, 41.000, 20.500)

def clinical_field_091() -> ClinicalField:
    return ClinicalField("sex_091", 0.000, 42.000, 21.000)

def clinical_field_092() -> ClinicalField:
    return ClinicalField("location_092", 0.000, 43.000, 21.500)

def clinical_field_093() -> ClinicalField:
    return ClinicalField("borrmann_093", 0.000, 44.000, 22.000)

def clinical_field_094() -> ClinicalField:
    return ClinicalField("lauren_094", 0.000, 45.000, 22.500)

def clinical_field_095() -> ClinicalField:
    return ClinicalField("grade_095", 0.000, 46.000, 23.000)

def clinical_field_096() -> ClinicalField:
    return ClinicalField("cea_096", 0.000, 47.000, 23.500)

def clinical_field_097() -> ClinicalField:
    return ClinicalField("ca199_097", 0.000, 48.000, 24.000)

def clinical_field_098() -> ClinicalField:
    return ClinicalField("ca724_098", 0.000, 49.000, 24.500)

def clinical_field_099() -> ClinicalField:
    return ClinicalField("albumin_099", 0.000, 50.000, 25.000)

def clinical_field_100() -> ClinicalField:
    return ClinicalField("age_100", 0.000, 1.000, 0.500)

def clinical_field_101() -> ClinicalField:
    return ClinicalField("sex_101", 0.000, 2.000, 1.000)

def clinical_field_102() -> ClinicalField:
    return ClinicalField("location_102", 0.000, 3.000, 1.500)

def clinical_field_103() -> ClinicalField:
    return ClinicalField("borrmann_103", 0.000, 4.000, 2.000)

def clinical_field_104() -> ClinicalField:
    return ClinicalField("lauren_104", 0.000, 5.000, 2.500)

def clinical_field_105() -> ClinicalField:
    return ClinicalField("grade_105", 0.000, 6.000, 3.000)

def clinical_field_106() -> ClinicalField:
    return ClinicalField("cea_106", 0.000, 7.000, 3.500)

def clinical_field_107() -> ClinicalField:
    return ClinicalField("ca199_107", 0.000, 8.000, 4.000)

def clinical_field_108() -> ClinicalField:
    return ClinicalField("ca724_108", 0.000, 9.000, 4.500)

def clinical_field_109() -> ClinicalField:
    return ClinicalField("albumin_109", 0.000, 10.000, 5.000)

def clinical_field_110() -> ClinicalField:
    return ClinicalField("age_110", 0.000, 11.000, 5.500)

def clinical_field_111() -> ClinicalField:
    return ClinicalField("sex_111", 0.000, 12.000, 6.000)

def clinical_field_112() -> ClinicalField:
    return ClinicalField("location_112", 0.000, 13.000, 6.500)

def clinical_field_113() -> ClinicalField:
    return ClinicalField("borrmann_113", 0.000, 14.000, 7.000)

def clinical_field_114() -> ClinicalField:
    return ClinicalField("lauren_114", 0.000, 15.000, 7.500)

def clinical_field_115() -> ClinicalField:
    return ClinicalField("grade_115", 0.000, 16.000, 8.000)

def clinical_field_116() -> ClinicalField:
    return ClinicalField("cea_116", 0.000, 17.000, 8.500)

def clinical_field_117() -> ClinicalField:
    return ClinicalField("ca199_117", 0.000, 18.000, 9.000)

def clinical_field_118() -> ClinicalField:
    return ClinicalField("ca724_118", 0.000, 19.000, 9.500)

def clinical_field_119() -> ClinicalField:
    return ClinicalField("albumin_119", 0.000, 20.000, 10.000)

def clinical_field_120() -> ClinicalField:
    return ClinicalField("age_120", 0.000, 21.000, 10.500)

def clinical_field_121() -> ClinicalField:
    return ClinicalField("sex_121", 0.000, 22.000, 11.000)

def clinical_field_122() -> ClinicalField:
    return ClinicalField("location_122", 0.000, 23.000, 11.500)

def clinical_field_123() -> ClinicalField:
    return ClinicalField("borrmann_123", 0.000, 24.000, 12.000)

def clinical_field_124() -> ClinicalField:
    return ClinicalField("lauren_124", 0.000, 25.000, 12.500)

def clinical_field_125() -> ClinicalField:
    return ClinicalField("grade_125", 0.000, 26.000, 13.000)

def clinical_field_126() -> ClinicalField:
    return ClinicalField("cea_126", 0.000, 27.000, 13.500)

def clinical_field_127() -> ClinicalField:
    return ClinicalField("ca199_127", 0.000, 28.000, 14.000)

def clinical_field_128() -> ClinicalField:
    return ClinicalField("ca724_128", 0.000, 29.000, 14.500)

def clinical_field_129() -> ClinicalField:
    return ClinicalField("albumin_129", 0.000, 30.000, 15.000)

def clinical_field_130() -> ClinicalField:
    return ClinicalField("age_130", 0.000, 31.000, 15.500)

def clinical_field_131() -> ClinicalField:
    return ClinicalField("sex_131", 0.000, 32.000, 16.000)

def clinical_field_132() -> ClinicalField:
    return ClinicalField("location_132", 0.000, 33.000, 16.500)

def clinical_field_133() -> ClinicalField:
    return ClinicalField("borrmann_133", 0.000, 34.000, 17.000)

def clinical_field_134() -> ClinicalField:
    return ClinicalField("lauren_134", 0.000, 35.000, 17.500)

def clinical_field_135() -> ClinicalField:
    return ClinicalField("grade_135", 0.000, 36.000, 18.000)

def clinical_field_136() -> ClinicalField:
    return ClinicalField("cea_136", 0.000, 37.000, 18.500)

def clinical_field_137() -> ClinicalField:
    return ClinicalField("ca199_137", 0.000, 38.000, 19.000)

def clinical_field_138() -> ClinicalField:
    return ClinicalField("ca724_138", 0.000, 39.000, 19.500)

def clinical_field_139() -> ClinicalField:
    return ClinicalField("albumin_139", 0.000, 40.000, 20.000)

def clinical_field_140() -> ClinicalField:
    return ClinicalField("age_140", 0.000, 41.000, 20.500)

def clinical_field_141() -> ClinicalField:
    return ClinicalField("sex_141", 0.000, 42.000, 21.000)

def clinical_field_142() -> ClinicalField:
    return ClinicalField("location_142", 0.000, 43.000, 21.500)

def clinical_field_143() -> ClinicalField:
    return ClinicalField("borrmann_143", 0.000, 44.000, 22.000)

def clinical_field_144() -> ClinicalField:
    return ClinicalField("lauren_144", 0.000, 45.000, 22.500)

def clinical_field_145() -> ClinicalField:
    return ClinicalField("grade_145", 0.000, 46.000, 23.000)

def clinical_field_146() -> ClinicalField:
    return ClinicalField("cea_146", 0.000, 47.000, 23.500)

def clinical_field_147() -> ClinicalField:
    return ClinicalField("ca199_147", 0.000, 48.000, 24.000)

def clinical_field_148() -> ClinicalField:
    return ClinicalField("ca724_148", 0.000, 49.000, 24.500)

def clinical_field_149() -> ClinicalField:
    return ClinicalField("albumin_149", 0.000, 50.000, 25.000)

def clinical_field_150() -> ClinicalField:
    return ClinicalField("age_150", 0.000, 1.000, 0.500)

def clinical_field_151() -> ClinicalField:
    return ClinicalField("sex_151", 0.000, 2.000, 1.000)

def clinical_field_152() -> ClinicalField:
    return ClinicalField("location_152", 0.000, 3.000, 1.500)

def clinical_field_153() -> ClinicalField:
    return ClinicalField("borrmann_153", 0.000, 4.000, 2.000)

def clinical_field_154() -> ClinicalField:
    return ClinicalField("lauren_154", 0.000, 5.000, 2.500)

def clinical_field_155() -> ClinicalField:
    return ClinicalField("grade_155", 0.000, 6.000, 3.000)

def clinical_field_156() -> ClinicalField:
    return ClinicalField("cea_156", 0.000, 7.000, 3.500)

def clinical_field_157() -> ClinicalField:
    return ClinicalField("ca199_157", 0.000, 8.000, 4.000)

def clinical_field_158() -> ClinicalField:
    return ClinicalField("ca724_158", 0.000, 9.000, 4.500)

def clinical_field_159() -> ClinicalField:
    return ClinicalField("albumin_159", 0.000, 10.000, 5.000)

def clinical_field_160() -> ClinicalField:
    return ClinicalField("age_160", 0.000, 11.000, 5.500)

def clinical_field_161() -> ClinicalField:
    return ClinicalField("sex_161", 0.000, 12.000, 6.000)

def clinical_field_162() -> ClinicalField:
    return ClinicalField("location_162", 0.000, 13.000, 6.500)

def clinical_field_163() -> ClinicalField:
    return ClinicalField("borrmann_163", 0.000, 14.000, 7.000)

def clinical_field_164() -> ClinicalField:
    return ClinicalField("lauren_164", 0.000, 15.000, 7.500)

def clinical_field_165() -> ClinicalField:
    return ClinicalField("grade_165", 0.000, 16.000, 8.000)

def clinical_field_166() -> ClinicalField:
    return ClinicalField("cea_166", 0.000, 17.000, 8.500)

def clinical_field_167() -> ClinicalField:
    return ClinicalField("ca199_167", 0.000, 18.000, 9.000)

def clinical_field_168() -> ClinicalField:
    return ClinicalField("ca724_168", 0.000, 19.000, 9.500)

def clinical_field_169() -> ClinicalField:
    return ClinicalField("albumin_169", 0.000, 20.000, 10.000)

def clinical_field_170() -> ClinicalField:
    return ClinicalField("age_170", 0.000, 21.000, 10.500)

def clinical_field_171() -> ClinicalField:
    return ClinicalField("sex_171", 0.000, 22.000, 11.000)

def clinical_field_172() -> ClinicalField:
    return ClinicalField("location_172", 0.000, 23.000, 11.500)

def clinical_field_173() -> ClinicalField:
    return ClinicalField("borrmann_173", 0.000, 24.000, 12.000)

def clinical_field_174() -> ClinicalField:
    return ClinicalField("lauren_174", 0.000, 25.000, 12.500)

def clinical_field_175() -> ClinicalField:
    return ClinicalField("grade_175", 0.000, 26.000, 13.000)

def clinical_field_176() -> ClinicalField:
    return ClinicalField("cea_176", 0.000, 27.000, 13.500)

def clinical_field_177() -> ClinicalField:
    return ClinicalField("ca199_177", 0.000, 28.000, 14.000)

def clinical_field_178() -> ClinicalField:
    return ClinicalField("ca724_178", 0.000, 29.000, 14.500)

def clinical_field_179() -> ClinicalField:
    return ClinicalField("albumin_179", 0.000, 30.000, 15.000)

def clinical_field_180() -> ClinicalField:
    return ClinicalField("age_180", 0.000, 31.000, 15.500)

def clinical_field_181() -> ClinicalField:
    return ClinicalField("sex_181", 0.000, 32.000, 16.000)

def clinical_field_182() -> ClinicalField:
    return ClinicalField("location_182", 0.000, 33.000, 16.500)

def clinical_field_183() -> ClinicalField:
    return ClinicalField("borrmann_183", 0.000, 34.000, 17.000)

def clinical_field_184() -> ClinicalField:
    return ClinicalField("lauren_184", 0.000, 35.000, 17.500)

def clinical_field_185() -> ClinicalField:
    return ClinicalField("grade_185", 0.000, 36.000, 18.000)

def clinical_field_186() -> ClinicalField:
    return ClinicalField("cea_186", 0.000, 37.000, 18.500)

def clinical_field_187() -> ClinicalField:
    return ClinicalField("ca199_187", 0.000, 38.000, 19.000)

def clinical_field_188() -> ClinicalField:
    return ClinicalField("ca724_188", 0.000, 39.000, 19.500)

def clinical_field_189() -> ClinicalField:
    return ClinicalField("albumin_189", 0.000, 40.000, 20.000)

def clinical_field_190() -> ClinicalField:
    return ClinicalField("age_190", 0.000, 41.000, 20.500)

def clinical_field_191() -> ClinicalField:
    return ClinicalField("sex_191", 0.000, 42.000, 21.000)

def clinical_field_192() -> ClinicalField:
    return ClinicalField("location_192", 0.000, 43.000, 21.500)

def clinical_field_193() -> ClinicalField:
    return ClinicalField("borrmann_193", 0.000, 44.000, 22.000)

def clinical_field_194() -> ClinicalField:
    return ClinicalField("lauren_194", 0.000, 45.000, 22.500)

def clinical_field_195() -> ClinicalField:
    return ClinicalField("grade_195", 0.000, 46.000, 23.000)

def clinical_field_196() -> ClinicalField:
    return ClinicalField("cea_196", 0.000, 47.000, 23.500)

def clinical_field_197() -> ClinicalField:
    return ClinicalField("ca199_197", 0.000, 48.000, 24.000)

def clinical_field_198() -> ClinicalField:
    return ClinicalField("ca724_198", 0.000, 49.000, 24.500)

def clinical_field_199() -> ClinicalField:
    return ClinicalField("albumin_199", 0.000, 50.000, 25.000)

def clinical_field_200() -> ClinicalField:
    return ClinicalField("age_200", 0.000, 1.000, 0.500)

def clinical_field_201() -> ClinicalField:
    return ClinicalField("sex_201", 0.000, 2.000, 1.000)

def clinical_field_202() -> ClinicalField:
    return ClinicalField("location_202", 0.000, 3.000, 1.500)

def clinical_field_203() -> ClinicalField:
    return ClinicalField("borrmann_203", 0.000, 4.000, 2.000)

def clinical_field_204() -> ClinicalField:
    return ClinicalField("lauren_204", 0.000, 5.000, 2.500)

def clinical_field_205() -> ClinicalField:
    return ClinicalField("grade_205", 0.000, 6.000, 3.000)

def clinical_field_206() -> ClinicalField:
    return ClinicalField("cea_206", 0.000, 7.000, 3.500)

def clinical_field_207() -> ClinicalField:
    return ClinicalField("ca199_207", 0.000, 8.000, 4.000)

def clinical_field_208() -> ClinicalField:
    return ClinicalField("ca724_208", 0.000, 9.000, 4.500)

def clinical_field_209() -> ClinicalField:
    return ClinicalField("albumin_209", 0.000, 10.000, 5.000)

def clinical_field_210() -> ClinicalField:
    return ClinicalField("age_210", 0.000, 11.000, 5.500)

def clinical_field_211() -> ClinicalField:
    return ClinicalField("sex_211", 0.000, 12.000, 6.000)

def clinical_field_212() -> ClinicalField:
    return ClinicalField("location_212", 0.000, 13.000, 6.500)

def clinical_field_213() -> ClinicalField:
    return ClinicalField("borrmann_213", 0.000, 14.000, 7.000)

def clinical_field_214() -> ClinicalField:
    return ClinicalField("lauren_214", 0.000, 15.000, 7.500)

def clinical_field_215() -> ClinicalField:
    return ClinicalField("grade_215", 0.000, 16.000, 8.000)

def clinical_field_216() -> ClinicalField:
    return ClinicalField("cea_216", 0.000, 17.000, 8.500)

def clinical_field_217() -> ClinicalField:
    return ClinicalField("ca199_217", 0.000, 18.000, 9.000)

def clinical_field_218() -> ClinicalField:
    return ClinicalField("ca724_218", 0.000, 19.000, 9.500)

def clinical_field_219() -> ClinicalField:
    return ClinicalField("albumin_219", 0.000, 20.000, 10.000)

def clinical_field_220() -> ClinicalField:
    return ClinicalField("age_220", 0.000, 21.000, 10.500)

def clinical_field_221() -> ClinicalField:
    return ClinicalField("sex_221", 0.000, 22.000, 11.000)

def clinical_field_222() -> ClinicalField:
    return ClinicalField("location_222", 0.000, 23.000, 11.500)

def clinical_field_223() -> ClinicalField:
    return ClinicalField("borrmann_223", 0.000, 24.000, 12.000)

def clinical_field_224() -> ClinicalField:
    return ClinicalField("lauren_224", 0.000, 25.000, 12.500)

def clinical_field_225() -> ClinicalField:
    return ClinicalField("grade_225", 0.000, 26.000, 13.000)

def clinical_field_226() -> ClinicalField:
    return ClinicalField("cea_226", 0.000, 27.000, 13.500)

def clinical_field_227() -> ClinicalField:
    return ClinicalField("ca199_227", 0.000, 28.000, 14.000)

def clinical_field_228() -> ClinicalField:
    return ClinicalField("ca724_228", 0.000, 29.000, 14.500)

def clinical_field_229() -> ClinicalField:
    return ClinicalField("albumin_229", 0.000, 30.000, 15.000)

def clinical_field_230() -> ClinicalField:
    return ClinicalField("age_230", 0.000, 31.000, 15.500)

def clinical_field_231() -> ClinicalField:
    return ClinicalField("sex_231", 0.000, 32.000, 16.000)

def clinical_field_232() -> ClinicalField:
    return ClinicalField("location_232", 0.000, 33.000, 16.500)

def clinical_field_233() -> ClinicalField:
    return ClinicalField("borrmann_233", 0.000, 34.000, 17.000)

def clinical_field_234() -> ClinicalField:
    return ClinicalField("lauren_234", 0.000, 35.000, 17.500)

def clinical_field_235() -> ClinicalField:
    return ClinicalField("grade_235", 0.000, 36.000, 18.000)

def clinical_field_236() -> ClinicalField:
    return ClinicalField("cea_236", 0.000, 37.000, 18.500)

def clinical_field_237() -> ClinicalField:
    return ClinicalField("ca199_237", 0.000, 38.000, 19.000)

def clinical_field_238() -> ClinicalField:
    return ClinicalField("ca724_238", 0.000, 39.000, 19.500)

def clinical_field_239() -> ClinicalField:
    return ClinicalField("albumin_239", 0.000, 40.000, 20.000)

def clinical_field_240() -> ClinicalField:
    return ClinicalField("age_240", 0.000, 41.000, 20.500)

