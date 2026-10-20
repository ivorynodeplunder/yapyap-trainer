from __future__ import annotations

import time

import pymem.process
from loguru import logger


class ProcessScanner:
    def __init__(self, target: str) -> None:
        self.target = target.lower()

    def wait_for_process(self, timeout_s: int = 30) -> int | None:
        deadline = time.time() + timeout_s
        while time.time() < deadline:
            for proc in pymem.process.list_processes():
                if proc.name.lower() == self.target:
                    return proc.pid
            time.sleep(0.5)
        return None