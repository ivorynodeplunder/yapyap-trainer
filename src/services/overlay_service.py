from __future__ import annotations

import tkinter as tk
from threading import Thread

from loguru import logger


class OverlayService:
    """Minimal always-on-top HUD showing active feature list."""

    def __init__(self, title: str = "YAPYAP Trainer") -> None:
        self._title = title
        self._root: tk.Tk | None = None
        self._lines: list[str] = []

    def set_lines(self, lines: list[str]) -> None:
        self._lines = lines
        if self._root is not None:
            self._redraw()

    def _redraw(self) -> None:
        assert self._root is not None
        for child in self._root.winfo_children():
            child.destroy()
        tk.Label(self._root, text=self._title, fg="#0f0", bg="#111").pack()
        for line in self._lines:
            tk.Label(self._root, text=line, fg="#0f0", bg="#111").pack()

    def start(self) -> None:
        self._root = tk.Tk()
        self._root.title(self._title)
        self._root.configure(bg="#111")
        self._root.attributes("-topmost", True)
        self._redraw()
        Thread(target=self._root.mainloop, daemon=True).start()
        logger.info("overlay started")