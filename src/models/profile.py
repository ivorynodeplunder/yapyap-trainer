from __future__ import annotations

from pydantic import BaseModel, Field


class Profile(BaseModel):
    name: str
    version: int = 1
    features: dict[str, dict] = Field(default_factory=dict)
    hotkeys: dict[str, str] = Field(default_factory=dict)