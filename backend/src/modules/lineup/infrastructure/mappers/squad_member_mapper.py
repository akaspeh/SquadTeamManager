# src/modules/lineup/infrastructure/mappers/squad_member_mapper.py

from src.modules.lineup.domain.entities.SquadMember import SquadMember
from src.modules.lineup.domain.value_objects.Kit import Kit
from src.modules.lineup.infrastructure.models.SquadMemberModel import SquadMemberModel

def domain_to_model(domain: SquadMember, squad_id: str) -> SquadMemberModel:
    return SquadMemberModel(
        id=domain.id,
        squad_id=squad_id,
        kit=domain.kit.name,
        player_name=domain.player_name
    )

def model_to_domain(model: SquadMemberModel) -> SquadMember:
    return SquadMember(
        id=model.id,
        kit=Kit(model.kit),
        player_name=model.player_name
    )