from pathlib import Path

from src.core.config_loader import ConfigLoader


def test_load_default_config(tmp_path: Path) -> None:
    cfg_file = tmp_path / "cfg.yaml"
    cfg_file.write_text(
        "target_process: test.exe\nfeatures:\n  - name: no_recoil\n    enabled: true\n",
        encoding="utf-8",
    )
    cfg = ConfigLoader.load(cfg_file)
    assert cfg.target_process == "test.exe"
    assert cfg.features[0].name == "no_recoil"
    assert cfg.features[0].enabled is True