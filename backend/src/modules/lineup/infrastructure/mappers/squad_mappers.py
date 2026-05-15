from modules.lineup.domain.entities import Squad
from shared.domain.value_objects import ID
from modules.lineup.infrastructure.mappers.squad_member_mappers import to_domain_squad_member, to_model_squad_member
from modules.lineup.infrastructure.models import SquadModel


def to_domain_squad(model: SquadModel) -> Squad:
    return Squad(
        id=ID(model.id),
        lineup_id=ID(model.lineup_id),
        name=model.name,
        color=model.color,
        created_at=model.created_at,
        members=[
            to_domain_squad_member(member_model)
            for member_model in model.members
        ],
    )

def to_model_squad(entity: Squad) -> SquadModel:
    model = SquadModel(
        id=str(entity.id),
        lineup_id=str(entity.lineup_id),
        name=entity.name,
        created_at=entity.created_at,
    )

    model.members = [
        to_model_squad_member(member)
        for member in entity.members
    ]

    return model