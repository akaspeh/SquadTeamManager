import uuid
from dataclasses import dataclass, field
from typing import List

@dataclass
class LineUp:
    """
    Aggregate representing a full lineup (e.g., a team in a match).
    Contains references to Squad aggregates by their IDs.
    Responsible for coordination of squads but not their internal rules.
    """
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    name: str = "Default LineUp"
    squad_ids: List[str] = field(default_factory=list)

    def add_squad(self, squad_id: str):
        """
        Add a squad to the lineup by ID.
        Raises ValueError if the squad is already present.
        """
        if squad_id in self.squad_ids:
            raise ValueError(f"Squad {squad_id} is already in the lineup")
        self.squad_ids.append(squad_id)

    def remove_squad(self, squad_id: str):
        """
        Remove a squad from the lineup by ID.
        """
        self.squad_ids = [s for s in self.squad_ids if s != squad_id]

    def has_squad(self, squad_id: str) -> bool:
        """
        Check if a squad is part of this lineup.
        """
        return squad_id in self.squad_ids

    @property
    def total_squads(self) -> int:
        """
        Returns the number of squads in this lineup.
        """
        return len(self.squad_ids)
