from __future__ import annotations

import json
from pathlib import Path

from loguru import logger

PROFILES_DIR = Path("profiles")


class ProfileService:
    """Persist per-feature option sets to disk under profiles/*.json."""

    def __init__(self, root: Path = PROFILES_DIR) -> None:
        self.root = root
        self.root.mkdir(parents=True, exist_ok=True)

    def save(self, name: str, payload: dict) -> Path:
        path = self.root / f"{name}.json"
        path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
        logger.debug("profile saved: {}", path)
        return path

    def load(self, name: str) -> dict:
        path = self.root / f"{name}.json"
        if not path.exists():
            return {}
        return json.loads(path.read_text(encoding="utf-8"))

    def list_profiles(self) -> list[str]:
        return sorted(p.stem for p in self.root.glob("*.json"))