from dataclasses import dataclass, field
from datetime import datetime
from typing import List

from src.modules.lineup.domain.value_objects.id import ID
from src.modules.lineup.domain.entities.squad import Squad
from src.modules.lineup.domain.exceptions import ValidationError


@dataclass
class Lineup:
    id: ID
    name: str
    squads: List[Squad] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.now)

    @staticmethod
    def create(name: str = "default_lineup") -> "Lineup":
        return Lineup(
            id=ID.new(),
            name=name,
        )

    def add_squad(self, squad: Squad):
        if squad.lineup_id != self.id:
            raise ValidationError("Squad lineup mismatch")

        self.squads.append(squad)

    def remove_squad(self, squad_id: ID):
        self.squads = [s for s in self.squads if s.id != squad_id]