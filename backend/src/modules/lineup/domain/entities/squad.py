from dataclasses import dataclass, field
from datetime import datetime
from typing import List

from shared.domain.value_objects.id import ID
from modules.lineup.domain.entities.squad_member import SquadMember
from modules.lineup.domain.policies.squad_policy import SquadPolicy
from shared.domain.exceptions import ValidationError

import re

HEX_COLOR_RE = re.compile(r"^#[0-9A-Fa-f]{6}$")

@dataclass
class Squad:
    id: ID
    lineup_id: ID
    name: str
    color: str
    members: List[SquadMember] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.now)

    @staticmethod
    def create(lineup_id: ID, name: str = "default_squad") -> "Squad":
        return Squad(
            id=ID.new(),
            lineup_id=lineup_id,
            name=name,
            color="#FFFFFF"
        )

    def add_member(self, member: SquadMember):
        if member.squad_id != self.id:
            raise ValidationError("Member squad mismatch")

        SquadPolicy.validate_can_add_member(len(self.members))

        self.members.append(member)

    def get_member(self, member_id: ID) -> SquadMember:
        member = next((m for m in self.members if m.id == member_id), None)

        if not member:
            raise ValidationError("Member not found")

        return member

    def remove_member(self, member_id: ID):
        self.members = [m for m in self.members if m.id != member_id]

    def change_color(self, color: str):
        if not HEX_COLOR_RE.match(color):
            raise ValidationError("Invalid squad color")

        if color == self.color:
            return  # no-op

        self.color = color

    def change_name(self, name: str):
        if not name or len(name) < 2:
            raise ValidationError("Invalid squad name")

        self.name = name