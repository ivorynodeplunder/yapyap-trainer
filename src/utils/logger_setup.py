from __future__ import annotations

import sys
from pathlib import Path

from loguru import logger


def configure(log_dir: str = "logs") -> None:
    Path(log_dir).mkdir(parents=True, exist_ok=True)
    logger.remove()
    logger.add(sys.stderr, level="INFO")
    logger.add(
        f"{log_dir}/yapyap_{{time:YYYY-MM-DD}}.log",
        rotation="10 MB",
        retention="7 days",
        level="DEBUG",
        enqueue=True,
    )