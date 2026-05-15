from dataclasses import dataclass, field

from shared.domain.value_objects import ID
from modules.roster.domain.entities.membership import Membership


@dataclass
class StaticSquad:
    id: ID
    name: str
    description: str | None = None

    members: list[Membership] = field(default_factory=list)