from modules.lineup.application.interfaces import LineupUnitOfWork
from modules.lineup.domain.aggregate_root import Lineup


class GetAllLineups:
    def __init__(self, uow: LineupUnitOfWork):
        self.uow = uow

    async def execute(self) -> list[Lineup]:
        lineups = await self.uow.lineups.list()
        return lineups