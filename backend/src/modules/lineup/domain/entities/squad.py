from dataclasses import dataclass, field
from datetime import datetime
from typing import List

from modules.lineup.domain.value_objects.id import ID
from modules.lineup.domain.entities.squad_member import SquadMember
from modules.lineup.domain.policies.squad_policy import SquadPolicy
from modules.lineup.domain.exceptions import ValidationError


@dataclass
class Squad:
    id: ID
    lineup_id: ID
    name: str
    members: List[SquadMember] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.now)

    @staticmethod
    def create(lineup_id: ID, name: str = "default_squad") -> "Squad":
        return Squad(
            id=ID.new(),
            lineup_id=lineup_id,
            name=name,
        )

    def add_member(self, member: SquadMember):
        if member.squad_id != self.id:
            raise ValidationError("Member squad mismatch")

        SquadPolicy.validate_can_add_member(len(self.members))

        self.members.append(member)

    def remove_member(self, member_id: ID):
        self.members = [m for m in self.members if m.id != member_id]