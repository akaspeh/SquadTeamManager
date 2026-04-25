from src.modules.lineup.application.interfaces import UnitOfWork
from src.modules.lineup.domain.aggregate_root import Lineup


class GetAllLineups:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def execute(self) -> list[Lineup]:
        lineups = await self.uow.lineups.list()
        return lineups