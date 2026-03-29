import uuid
from dataclasses import dataclass, field
from typing import List
from src.modules.lineup.domain.entities.Squad import Squad


@dataclass
class LineUp:
    """
    Aggregate representing a full lineup (e.g., a team in a match).
    Contains references to Squad aggregates by their IDs.
    Responsible for coordination of squads but not their internal rules.
    """
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    name: str = "Default LineUp"
    squads: List[Squad] = field(default_factory=list)

    def _get_squad_or_raise(self, squad_id: str) -> Squad:
        for squad in self.squads:
            if squad.id == squad_id:
                return squad
        raise ValueError("Squad not found")

    def _sync_squads(self, incoming_squads):
        existing = {s.id: s for s in self.squads}
        new_squads = []

        for s in incoming_squads:
            if s.id in existing:
                squad = existing[s.id]
                squad.name = s.name
                new_squads.append(squad)
            else:
                new_squads.append(Squad(id=s.id, name=s.name))

        self.squads = new_squads

    def update_from_dto(self, dto):
        self.name = dto.name
        self._sync_squads(dto.squads)

    def add_squad(self, squad: Squad):
        """
        Add a squad to the lineup.
        Raises ValueError if a squad with the same ID is already present.
        """
        if any(s.id == squad.id for s in self.squads):
            raise ValueError(f"Squad {squad.id} is already in the lineup")
        self.squads.append(squad)

    def update_squad(self, squad_id: str, new_name: str | None = None):
        squad = self._get_squad_or_raise(squad_id)
        squad.update(name=new_name)

    def remove_squad(self, squad_id: str):
        """
        Remove a squad from the lineup by ID.
        """
        self.squads = [s for s in self.squads if s != squad_id]

    @property
    def total_squads(self) -> int:
        """
        Returns the number of squads in this lineup.
        """
        return len(self.squads)
