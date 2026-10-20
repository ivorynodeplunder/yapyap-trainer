from __future__ import annotations

from typing import Callable

import keyboard
from loguru import logger


class HotkeyManager:
    def __init__(self) -> None:
        self._registered: dict[str, Callable[[], None]] = {}

    def register(self, combo: str, callback: Callable[[], None]) -> None:
        if combo in self._registered:
            return
        keyboard.add_hotkey(combo, callback)
        self._registered[combo] = callback
        logger.debug("hotkey registered: {}", combo)

    def unregister_all(self) -> None:
        for combo in list(self._registered):
            try:
                keyboard.remove_hotkey(combo)
            except KeyError:
                pass
        self._registered.clear()