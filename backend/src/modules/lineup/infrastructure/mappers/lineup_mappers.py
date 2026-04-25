from src.modules.lineup.domain.aggregate_root import Lineup
from src.modules.lineup.domain.value_objects import ID
from src.modules.lineup.infrastructure.mappers.squad_mappers import to_domain_squad, to_model_squad
from src.modules.lineup.infrastructure.models import LineupModel


def to_domain_lineup(model: LineupModel) -> Lineup:
    return Lineup(
        id=ID(model.id),
        name=model.name,
        created_at=model.created_at,
        squads=[
            to_domain_squad(squad_model)
            for squad_model in model.squads
        ],
    )



def to_model_lineup(entity: Lineup) -> LineupModel:
    model = LineupModel(
        id=str(entity.id),
        name=entity.name,
        created_at=entity.created_at,
    )

    model.squads = [
        to_model_squad(squad)
        for squad in entity.squads
    ]

    return model