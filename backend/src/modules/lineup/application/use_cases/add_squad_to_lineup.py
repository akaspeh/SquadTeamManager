from src.modules.lineup.application.interfaces import UnitOfWork
from src.modules.lineup.domain.entities import Squad
from src.modules.lineup.domain.value_objects import ID


class AddSquadToLineup:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def execute(self, lineup_id: str, name: str) -> str:
        lineup = await self.uow.lineups.get(ID(lineup_id))

        if not lineup:
            raise ValueError("Lineup not found")

        squad = Squad.create(lineup.id, name)

        lineup.add_squad(squad)

        return str(squad.id)
