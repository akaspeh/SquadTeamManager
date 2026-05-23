from typing import Protocol, List

from modules.lineup.domain.entities import SquadMember
from shared.domain.value_objects import ID


class SquadMemberRepository(Protocol):
    async def list_by_squad(self, squad_id: ID) -> List[SquadMember]: ...
