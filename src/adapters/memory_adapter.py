from __future__ import annotations

from typing import Any

import pymem
from loguru import logger


class MemoryAdapter:
    """Thin wrapper around pymem for read/write/AOB scanning."""

    def __init__(self, pm: pymem.Pymem) -> None:
        self._pm = pm
        self._handle = pm.process_handle

    @classmethod
    def attach(cls, pid: int) -> "MemoryAdapter":
        pm = pymem.Pymem()
        pm.open_process_from_id(pid)
        return cls(pm)

    def read(self, address: int, size: int) -> bytes:
        return self._pm.read_bytes(address, size)

    def write(self, address: int, payload: bytes) -> None:
        self._pm.write_bytes(address, payload, len(payload))

    def read_int(self, address: int) -> int:
        return int.from_bytes(self.read(address, 4), "little")

    def write_int(self, address: int, value: int) -> None:
        self.write(address, value.to_bytes(4, "little"))

    def scan_aob(self, pattern: str, module: str = "game.exe") -> int | None:
        try:
            return self._pm.pattern_scan_module(pattern, module)
        except Exception as exc:  # noqa: BLE001
            logger.debug("aob miss {}: {}", pattern, exc)
            return None

    def detach(self) -> None:
        try:
            self._pm.close_process()
        except Exception:  # noqa: BLE001
            pass