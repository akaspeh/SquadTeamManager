from modules.lineup.application.interfaces import LineupUnitOfWork
from modules.lineup.domain.entities import Squad
from shared.domain.value_objects import ID


class AddSquadToLineup:
    def __init__(self, uow: LineupUnitOfWork):
        self.uow = uow

    async def execute(self, lineup_id: str, name: str) -> str:
        lineup = await self.uow.lineups.get(ID(lineup_id))

        if not lineup:
            raise ValueError("Lineup not found")

        squad = Squad.create(lineup.id, name)

        lineup.add_squad(squad)

        await self.uow.lineups.save(lineup)

        return str(squad.id)
