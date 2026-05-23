from dataclasses import dataclass, field

from shared.domain.value_objects import ID
from modules.roster.domain.entities.membership import Membership
from modules.roster.domain.entities.static_squad import StaticSquad


@dataclass
class Roster:
    id: ID

    members: list[Membership] = field(default_factory=list)
    static_squads: list[StaticSquad] = field(default_factory=list)
