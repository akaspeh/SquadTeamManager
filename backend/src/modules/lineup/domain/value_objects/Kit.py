from dataclasses import dataclass
from ..enums.KitEnum import KitEnum
@dataclass(frozen=True, slots=True)
class Kit:
    """
    Value Object representing a player's kit.
    """
    name: str

    def __post_init__(self):
        if self.name not in KitEnum._value2member_map_:
            raise ValueError(f"Invalid kit name: {self.name}")