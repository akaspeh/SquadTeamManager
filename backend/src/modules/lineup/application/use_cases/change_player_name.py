from modules.lineup.application.interfaces import LineupUnitOfWork
from shared.domain.exceptions import ValidationError
from shared.domain.value_objects import ID


class ChangePlayerName:
    def __init__(self, uow: LineupUnitOfWork):
        self.uow = uow

    async def execute(self, lineup_id: str, squad_id: str, member_id: str, name: str):
        lineup = await self.uow.lineups.get(ID(lineup_id))

        if not lineup:
            raise ValidationError("Lineup not found")

        squad = lineup.get_squad(ID(squad_id))
        if not squad:
            raise ValidationError("Squad not found")

        member = squad.get_member(ID(member_id))
        if not member:
            raise ValidationError("Player not found")

        member.change_name(name)

        await self.uow.lineups.save(lineup)
