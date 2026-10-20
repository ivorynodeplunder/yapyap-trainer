from __future__ import annotations

import threading
import time

from loguru import logger

from src.core.config_loader import TrainerConfig
from src.adapters.memory_adapter import MemoryAdapter
from src.adapters.process_scanner import ProcessScanner
from src.features.registry import FeatureRegistry


class TrainerRuntime:
    """Owns the attach loop and dispatches enabled features each tick."""

    def __init__(self, config: TrainerConfig) -> None:
        self.config = config
        self._stop = threading.Event()
        self._scanner = ProcessScanner(config.target_process)
        self._memory: MemoryAdapter | None = None
        self._registry = FeatureRegistry.from_config(config)

    def start(self, dry_run: bool = False) -> None:
        if dry_run:
            logger.info("dry-run: {} features staged", len(self._registry))
            return

        pid = self._scanner.wait_for_process(timeout_s=30)
        if pid is None:
            logger.error("target {} not found", self.config.target_process)
            return

        self._memory = MemoryAdapter.attach(pid)
        logger.success("attached to pid={}", pid)
        self._registry.bind(self._memory)
        self._tick_loop()

    def _tick_loop(self) -> None:
        delay = self.config.poll_interval_ms / 1000.0
        while not self._stop.is_set():
            for feature in self._registry.enabled():
                try:
                    feature.tick()
                except Exception as exc:  # noqa: BLE001
                    logger.exception("feature {} failed: {}", feature.name, exc)
            time.sleep(delay)

    def shutdown(self) -> None:
        self._stop.set()
        if self._memory is not None:
            self._memory.detach()
        logger.info("runtime shutdown complete")