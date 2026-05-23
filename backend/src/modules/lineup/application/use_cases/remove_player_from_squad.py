from modules.lineup.application.interfaces import LineupUnitOfWork
from shared.domain.value_objects.id import ID
from shared.domain.exceptions import ValidationError


class RemovePlayerFromSquad:
    def __init__(self, uow: LineupUnitOfWork):
        self.uow = uow

    async def execute(
        self,
        lineup_id: str,
        squad_id: str,
        member_id: str,
    ):
        lineup = await self.uow.lineups.get(ID(lineup_id))

        if not lineup:
            raise ValidationError("Lineup not found")

        squad = lineup.get_squad(ID(squad_id))

        if not squad:
            raise ValidationError("Squad not found")

        squad.remove_member(ID(member_id))

        await self.uow.lineups.save(lineup)
