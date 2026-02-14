from typing import List
from dataclasses import dataclass, field
from ..value_objects.Formations import Formation
from ..entities.SquadMember import SquadMember
from ..policies.SquadPolicy import SquadPolicy

# that class can be
# optimized by storing void squadmembers
# to not modify list as its hard operation
# but right now im tired

@dataclass
class Squad:
    """
    Aggregate representing a squad lineup.
    Delegates hard rules to SquadPolicy.
    """
    name: str
    formation: Formation
    members: List[SquadMember] = field(default_factory=list)

    def add_member(self, member: SquadMember):
        # Hard rules validated via policy
        SquadPolicy.validate_max_players(self)
        SquadPolicy.validate_unique_kit(self, member)

        self.members.append(member)

    def remove_member(self, member_id: str):
        self.members = [m for m in self.members if m.id != member_id]

    @property
    def current_size(self) -> int:
        return len(self.members)

