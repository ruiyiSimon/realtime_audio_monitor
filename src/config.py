import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent


def load_config(path=None):
    if path is None:
        path = ROOT / "config.json"
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


if __name__ == "__main__":
    cfg = load_config()
    print(cfg)