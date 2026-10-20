from __future__ import annotations

from abc import ABC, abstractmethod

from src.adapters.memory_adapter import MemoryAdapter


class BaseFeature(ABC):
    name: str = "base"

    def __init__(self) -> None:
        self._mem: MemoryAdapter | None = None

    def bind(self, memory: MemoryAdapter) -> None:
        self._mem = memory
        self.on_bind()

    def on_bind(self) -> None:
        """Resolve addresses once memory is available."""

    @abstractmethod
    def tick(self) -> None:
        """Called each runtime poll while the feature is enabled."""

    @property
    def memory(self) -> MemoryAdapter:
        if self._mem is None:
            raise RuntimeError(f"feature {self.name} not bound to memory")
        return self._mem