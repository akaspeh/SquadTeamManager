from src.modules.lineup.domain.entities import SquadMember
from src.modules.lineup.domain.value_objects import ID, Kit, Role
from src.modules.lineup.infrastructure.models import SquadMemberModel


def to_domain_squad_member(model: SquadMemberModel) -> SquadMember:
    return SquadMember(
        id=ID(model.id),
        squad_id=ID(model.squad_id),
        name=model.name,
        kit=Kit(model.kit),
        role=Role(model.role),
        created_at=model.created_at,
    )

def to_model_squad_member(entity: SquadMember) -> SquadMemberModel:
    return SquadMemberModel(
        id=str(entity.id),
        squad_id=str(entity.squad_id),
        name=entity.name,
        kit=entity.kit.value,
        role=entity.role.value,
        created_at=entity.created_at,
    )