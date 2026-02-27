from typing import List
import uuid
from dataclasses import dataclass, field
from src.modules.lineup.domain.entities.SquadMember import SquadMember
from src.modules.lineup.domain.policies.SquadPolicy import SquadPolicy

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
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    name: str = "Squad"
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

