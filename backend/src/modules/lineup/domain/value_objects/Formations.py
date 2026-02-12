from dataclasses import dataclass

@dataclass(frozen=True)
class Formation:
    name: str
    slot_count: int
    MAX_SLOTS: int = 9

    def __post_init__(self):
        if self.slot_count < 1:
            raise ValueError(f"Formation '{self.name}' must have at least one slot")
        if self.slot_count > self.MAX_SLOTS:
            raise ValueError(f"Formation '{self.name}' cannot have more than {self.MAX_SLOTS} slots")