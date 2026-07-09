from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Iterator, Mapping


@dataclass(frozen=True)
class StageLabel:
    ct: int
    cn: int
    cm: int
    resectable: int
    neoadjuvant: int


@dataclass(frozen=True)
class StudyRecord:
    patient_id: str
    site: int
    split: str
    arterial: str
    portal: str
    delayed: str
    tumor_mask: str
    stomach_mask: str
    clinical: Mapping[str, float | int | str]
    label: StageLabel


class ManifestError(ValueError):
    pass


def read_json(path: str) -> Mapping[str, float | int | str]:
    p = Path(path)
    if not p.exists():
        return {}
    value = json.loads(p.read_text())
    if not isinstance(value, dict):
        raise ManifestError("clinical record must be an object")
    return value


def label_from_mapping(row: Mapping[str, object]) -> StageLabel:
    return StageLabel(
        ct=int(row["ct"]),
        cn=int(row["cn"]),
        cm=int(row["cm"]),
        resectable=int(row["resectable"]),
        neoadjuvant=int(row["neoadjuvant"]),
    )


def record_from_mapping(row: Mapping[str, object]) -> StudyRecord:
    clinical_path = str(row.get("clinical_json", ""))
    return StudyRecord(
        patient_id=str(row["patient_id"]),
        site=int(row["site"]),
        split=str(row["split"]),
        arterial=str(row.get("arterial", "")),
        portal=str(row.get("portal", "")),
        delayed=str(row.get("delayed", "")),
        tumor_mask=str(row.get("tumor_mask", "")),
        stomach_mask=str(row.get("stomach_mask", "")),
        clinical=read_json(clinical_path),
        label=label_from_mapping(row),
    )


def load_jsonl(path: str | Path) -> list[StudyRecord]:
    rows: list[StudyRecord] = []
    for line_number, line in enumerate(Path(path).read_text().splitlines(), start=1):
        if not line.strip():
            continue
        obj = json.loads(line)
        if not isinstance(obj, dict):
            raise ManifestError(f"line {line_number} is not an object")
        rows.append(record_from_mapping(obj))
    return rows


def split_records(records: Iterable[StudyRecord], split: str) -> list[StudyRecord]:
    return [record for record in records if record.split == split]


def site_histogram(records: Iterable[StudyRecord]) -> dict[int, int]:
    counts: dict[int, int] = {}
    for record in records:
        counts[record.site] = counts.get(record.site, 0) + 1
    return counts


def iter_batches(records: list[StudyRecord], batch_size: int) -> Iterator[list[StudyRecord]]:
    for start in range(0, len(records), batch_size):
        yield records[start : start + batch_size]
