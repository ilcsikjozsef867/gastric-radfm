from __future__ import annotations

import argparse
import json
from pathlib import Path

from cais_core.learning.config import load_config
from cais_core.learning.trainer import train_local


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    args = parser.parse_args()
    config = load_config(args.config)
    result = train_local(config)
    out = Path(config.output_dir)
    out.mkdir(parents=True, exist_ok=True)
    (out / "metrics.json").write_text(json.dumps({"losses": result.losses, "metrics": result.metrics}, indent=2))


if __name__ == "__main__":
    main()
