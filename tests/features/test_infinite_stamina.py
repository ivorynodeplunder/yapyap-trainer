from src.features.infinite_stamina import InfiniteStamina


class _FakeMem:
    def __init__(self) -> None:
        self.writes: list[tuple[int, bytes]] = []

    def scan_aob(self, pattern: str, module: str = "game.exe") -> int:
        return 0x1000

    def write(self, address: int, payload: bytes) -> None:
        self.writes.append((address, payload))


def test_infinite_stamina_writes_on_tick() -> None:
    feat = InfiniteStamina()
    fake = _FakeMem()
    feat.bind(fake)  # type: ignore[arg-type]
    feat.tick()
    assert fake.writes, "expected at least one memory write"
    addr, payload = fake.writes[0]
    assert addr == 0x1020
    assert len(payload) == 4