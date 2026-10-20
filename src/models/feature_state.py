from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass
class FeatureState:
    name: str
    enabled: bool = False
    last_tick: datetime | None = None
    error_count: int = 0
    metadata: dict = field(default_factory=dict)

    def mark_tick(self) -> None:
        self.last_tick = datetime.now(timezone.utc)