from typing import Protocol, List, Optional

from modules.lineup.domain.entities import Squad
from shared.domain.value_objects import ID


class SquadRepository(Protocol):
    async def get(self, id: ID) -> Optional[Squad]: ...

    async def list_by_lineup(self, lineup_id: ID) -> List[Squad]: ...
