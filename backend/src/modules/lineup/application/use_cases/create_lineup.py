from modules.lineup.application.interfaces import LineupUnitOfWork
from modules.lineup.domain.aggregate_root import Lineup


class CreateLineup:
    def __init__(self, uow: LineupUnitOfWork):
        self.uow = uow

    async def execute(self, name: str) -> str:
        lineup = Lineup.create(name)

        await self.uow.lineups.add(lineup)

        return str(lineup.id)
