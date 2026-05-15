from modules.lineup.application.interfaces import UnitOfWork
from shared.domain.value_objects.id import ID
from modules.lineup.domain.entities.squad_member import SquadMember
from shared.domain.value_objects import Kit
from shared.domain.value_objects import Role
from shared.domain.exceptions import ValidationError


class AddPlayerToSquad:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def execute(
        self, lineup_id: str, squad_id: str, name: str, kit: Kit, role: Role) -> str:
        lineup = await self.uow.lineups.get(ID(lineup_id))

        if not lineup:
            raise ValidationError("Lineup not found")

        squad = next((s for s in lineup.squads if s.id == ID(squad_id)), None)

        if not squad:
            raise ValidationError("Squad not found")

        member = SquadMember.create(
            squad_id=squad.id,
            name=name,
            kit=kit,
            role=role,
        )

        squad.add_member(member)

        await self.uow.lineups.save(lineup)

        return str(member.id)
