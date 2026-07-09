from __future__ import annotations

import argparse
import json
from pathlib import Path


def load_jsonl(path: str) -> list[dict[str, object]]:
    return [json.loads(line) for line in Path(path).read_text().splitlines() if line.strip()]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    parser.add_argument("--predictions", required=True)
    args = parser.parse_args()
    rows = load_jsonl(args.predictions)
    total = len(rows)
    correct = sum(1 for row in rows if row.get("ct") == row.get("ct_label"))
    value = correct / max(total, 1)
    Path("outputs").mkdir(exist_ok=True)
    Path("outputs/evaluation.json").write_text(json.dumps({"ct_accuracy": value, "n": total}, indent=2))


if __name__ == "__main__":
    main()
