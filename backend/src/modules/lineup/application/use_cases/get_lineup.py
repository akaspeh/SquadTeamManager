from modules.lineup.application.interfaces import UnitOfWork
from modules.lineup.domain.aggregate_root import Lineup
from shared.domain.value_objects import ID


class GetLineup:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def execute(self, lineup_id: str) -> Lineup:
        lineup = await self.uow.lineups.get(ID(lineup_id))

        if not lineup:
            raise ValueError("Lineup not found")

        return lineup
