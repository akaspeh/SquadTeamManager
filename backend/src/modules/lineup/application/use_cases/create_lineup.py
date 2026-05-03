from modules.lineup.application.interfaces import UnitOfWork
from modules.lineup.domain.aggregate_root import Lineup


class CreateLineup:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def execute(self, name: str) -> str:
        lineup = Lineup.create(name)

        await self.uow.lineups.add(lineup)

        return str(lineup.id)
