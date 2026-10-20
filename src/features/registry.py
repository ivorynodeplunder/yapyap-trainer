from __future__ import annotations

from src.core.config_loader import TrainerConfig
from src.features.base import BaseFeature
from src.features.infinite_stamina import InfiniteStamina
from src.features.no_recoil import NoRecoil

_FEATURES: dict[str, type[BaseFeature]] = {
    "infinite_stamina": InfiniteStamina,
    "no_recoil": NoRecoil,
}


class FeatureRegistry:
    def __init__(self, features: list[BaseFeature]) -> None:
        self._features = features

    @classmethod
    def from_config(cls, cfg: TrainerConfig) -> "FeatureRegistry":
        built: list[BaseFeature] = []
        for toggle in cfg.features:
            if not toggle.enabled:
                continue
            klass = _FEATURES.get(toggle.name)
            if klass is None:
                continue
            built.append(klass())
        return cls(built)

    def bind(self, memory) -> None:
        for f in self._features:
            f.bind(memory)

    def enabled(self) -> list[BaseFeature]:
        return self._features

    def __len__(self) -> int:
        return len(self._features)