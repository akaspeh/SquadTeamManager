from dataclasses import dataclass, field
from datetime import datetime

from src.modules.lineup.domain.value_objects.id import ID
from src.modules.lineup.domain.value_objects.kit import Kit
from src.modules.lineup.domain.value_objects.role import Role


@dataclass
class SquadMember:
    id: ID
    squad_id: ID
    name: str
    kit: Kit
    role: Role
    created_at: datetime = field(default_factory=datetime.utcnow)

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