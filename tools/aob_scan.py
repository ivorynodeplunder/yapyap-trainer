"""Standalone AOB scanner for finding feature signatures in a running game."""
from __future__ import annotations

import argparse

from src.adapters.memory_adapter import MemoryAdapter
from src.adapters.process_scanner import ProcessScanner


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--process", required=True)
    parser.add_argument("--pattern", required=True)
    parser.add_argument("--module", default="game.exe")
    args = parser.parse_args()

    pid = ProcessScanner(args.process).wait_for_process(timeout_s=10)
    if pid is None:
        print("process not found")
        return 1
    mem = MemoryAdapter.attach(pid)
    addr = mem.scan_aob(args.pattern, module=args.module)
    print(f"result: {hex(addr) if addr else 'not found'}")
    mem.detach()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())