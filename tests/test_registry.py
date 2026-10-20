from src.core.config_loader import FeatureToggle, TrainerConfig
from src.features.registry import FeatureRegistry


def test_registry_filters_disabled_features() -> None:
    cfg = TrainerConfig(
        features=[
            FeatureToggle(name="no_recoil", enabled=True),
            FeatureToggle(name="infinite_stamina", enabled=False),
        ]
    )
    registry = FeatureRegistry.from_config(cfg)
    names = [f.name for f in registry.enabled()]
    assert names == ["no_recoil"]