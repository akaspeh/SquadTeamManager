from dataclasses import dataclass

from shared.domain.value_objects import ID, Kit


@dataclass(frozen=True)
class Player:
    id: ID
    nickname: str
    kits: list[Kit]