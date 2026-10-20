from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml
from pydantic import BaseModel, Field


class FeatureToggle(BaseModel):
    name: str
    enabled: bool = False
    hotkey: str | None = None
    options: dict[str, Any] = Field(default_factory=dict)


class TrainerConfig(BaseModel):
    target_process: str = "game.exe"
    poll_interval_ms: int = 250
    overlay_enabled: bool = True
    features: list[FeatureToggle] = Field(default_factory=list)


class ConfigLoader:
    @staticmethod
    def load(path: str | Path) -> TrainerConfig:
        raw = yaml.safe_load(Path(path).read_text(encoding="utf-8")) or {}
        return TrainerConfig.model_validate(raw)