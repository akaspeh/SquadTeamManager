from dataclasses import dataclass, field
from datetime import datetime
from typing import List

from shared.domain.value_objects.id import ID
from modules.lineup.domain.entities.squad import Squad
from shared.domain.exceptions import ValidationError


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

        if any(s.id == squad.id for s in self.squads):
            raise ValidationError("Squad already exists in lineup")

        self.squads.append(squad)

    def get_squad(self, squad_id: ID) -> Squad | None:
        return next((s for s in self.squads if s.id == squad_id), None)

    def remove_squad(self, squad_id: ID):
        squad = self.get_squad(squad_id)

        if not squad:
            raise ValidationError("Squad not found")

        self.squads = [s for s in self.squads if s.id != squad_id]

    def change_name(self, name: str):
        if not name or len(name.strip()) < 2:
            raise ValidationError("Invalid lineup name")

        if name == self.name:
            return

        self.name = name