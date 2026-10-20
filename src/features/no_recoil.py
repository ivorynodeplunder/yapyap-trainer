from __future__ import annotations

from src.features.base import BaseFeature


class NoRecoil(BaseFeature):
    name = "no_recoil"
    _pattern = "F3 0F 10 87 ?? ?? ?? ?? 0F 57 C9"

    def __init__(self) -> None:
        super().__init__()
        self._addr: int | None = None

    def on_bind(self) -> None:
        self._addr = self.memory.scan_aob(self._pattern)

    def tick(self) -> None:
        if self._addr is None:
            return
        # zero out recoil accumulator
        self.memory.write(self._addr + 0x10, b"\x00\x00\x00\x00")