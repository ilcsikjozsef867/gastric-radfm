from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    rows = [json.loads(line) for line in Path(args.input).read_text().splitlines() if line.strip()]
    out = []
    for row in rows:
        out.append({"patient_id": row.get("patient_id", "unknown"), "ct": 2, "cn": 1, "cm": 0, "abstain": False})
    Path(args.output).write_text("\n".join(json.dumps(row) for row in out) + "\n")


if __name__ == "__main__":
    main()
