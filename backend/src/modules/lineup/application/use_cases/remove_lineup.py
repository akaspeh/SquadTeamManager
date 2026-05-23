from modules.lineup.application.interfaces import LineupUnitOfWork
from shared.domain.value_objects.id import ID
from shared.domain.exceptions import ValidationError


class RemoveLineup:
    def __init__(self, uow: LineupUnitOfWork):
        self.uow = uow

    async def execute(self, lineup_id: str) -> None:
        lineup = await self.uow.lineups.get(ID(lineup_id))

        if not lineup:
            raise ValidationError("Lineup not found")

        await self.uow.lineups.remove(ID(lineup_id))
