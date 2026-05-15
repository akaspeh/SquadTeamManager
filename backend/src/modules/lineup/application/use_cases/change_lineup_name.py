from modules.lineup.application.interfaces import UnitOfWork
from shared.domain.exceptions import ValidationError
from shared.domain.value_objects import ID


class ChangeLineupName:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def execute(self, lineup_id: str, name: str):
        lineup = await self.uow.lineups.get(ID(lineup_id))

        if not lineup:
            raise ValidationError("Lineup not found")

        lineup.change_name(name)

        await self.uow.lineups.save(lineup)