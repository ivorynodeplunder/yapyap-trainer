# Contributing to YAPYAP Trainer

Thanks for your interest in improving YAPYAP Trainer.

## Ground rules
- YAPYAP Trainer is a hobbyist memory-patching trainer for single-player and private-server use only.
- Do **not** submit PRs that target anti-cheat bypasses for online competitive titles.
- Keep feature patches scoped to `src/features/` and register them through `FeatureRegistry`.

## Development setup
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python -m src.bootstrap.main --dry-run
```

## Style
- Type hints required on public functions.
- Log via `loguru.logger`, never `print`.
- Each new feature must ship a matching entry in `tests/features/`.

## Submitting
Open a PR against `main` with a short summary of the address signatures you targeted and the game build you verified against.