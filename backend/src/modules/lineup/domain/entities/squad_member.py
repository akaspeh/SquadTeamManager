from dataclasses import dataclass, field
from datetime import datetime

from shared.domain.value_objects.id import ID
from shared.domain.value_objects.kit import Kit
from shared.domain.value_objects.role import Role
from shared.domain.exceptions import ValidationError

@dataclass
class SquadMember:
    id: ID
    squad_id: ID
    name: str
    kit: Kit
    role: Role
    created_at: datetime = field(default_factory=datetime.now)

    @staticmethod
    def create(
        squad_id: ID,
        name: str = "some_member",
        kit: Kit = Kit.UNARMED,
        role: Role = Role.FLEX,
    ) -> "SquadMember":
        return SquadMember(
            id=ID.new(),
            squad_id=squad_id,
            name=name,
            kit=kit,
            role=role,
        )

    def change_role(self, role: Role):
        if not role:
            raise ValidationError("Role cannot be empty")

        self.role = role

    def change_kit(self, kit: Kit):
        if not kit:
            raise ValidationError("Kit cannot be empty")

        self.kit = kit

    def change_name(self, name: str):
        if not name or len(name) < 2:
            raise ValidationError("Invalid squad name")

        self.name = name