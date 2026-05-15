from modules.lineup.application.interfaces import LineupUnitOfWork
from shared.domain.value_objects import ID


class RemoveSquadFromLineup:
    def __init__(self, uow:  LineupUnitOfWork):
        self.uow = uow

    async def execute(self, lineup_id: str, squad_id: str):
        lineup = await self.uow.lineups.get(ID(lineup_id))

        if not lineup:
            raise ValueError("Lineup not found")

        lineup.remove_squad(ID(squad_id))

        await self.uow.lineups.save(lineup)
