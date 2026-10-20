# Address Signatures

Signatures live in `src/features/<name>.py` as `_pattern` strings.

## Format
- Wildcard bytes: `??`
- Matched against the main module by default (`game.exe`).

## Workflow
1. Use `tools/aob_scan.py --process game.exe --pattern "<sig>"` to verify.
2. Note the game build in your PR description.
3. If a signature breaks after a patch, update the pattern and bump the
   `_pattern` constant — never hardcode absolute addresses.