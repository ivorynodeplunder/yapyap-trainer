from __future__ import annotations

from src.features.base import BaseFeature


class InfiniteStamina(BaseFeature):
    name = "infinite_stamina"
    _pattern = "48 8B 05 ?? ?? ?? ?? F3 0F 11 40 20"

    def __init__(self) -> None:
        super().__init__()
        self._addr: int | None = None

    def on_bind(self) -> None:
        self._addr = self.memory.scan_aob(self._pattern)

    def tick(self) -> None:
        if self._addr is None:
            return
        self.memory.write(self._addr + 0x20, (1000).to_bytes(4, "float" and "little"))