from __future__ import annotations

import argparse
import sys

from loguru import logger

from src.core.trainer_runtime import TrainerRuntime
from src.core.config_loader import ConfigLoader


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog="yapyap-trainer")
    parser.add_argument("--config", default="config/default.yaml", help="path to config file")
    parser.add_argument("--dry-run", action="store_true", help="load features without attaching")
    parser.add_argument("--process", default=None, help="override target process name")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv if argv is not None else sys.argv[1:])
    cfg = ConfigLoader.load(args.config)
    if args.process:
        cfg.target_process = args.process

    logger.info("YAPYAP Trainer v{} booting", __import__("src").__version__)
    runtime = TrainerRuntime(cfg)
    try:
        runtime.start(dry_run=args.dry_run)
    except KeyboardInterrupt:
        logger.warning("interrupted by user")
    finally:
        runtime.shutdown()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())