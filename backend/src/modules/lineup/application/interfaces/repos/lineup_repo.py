from typing import Protocol, Optional, List

from src.modules.lineup.domain.aggregate_root import Lineup
from src.modules.lineup.domain.value_objects import ID


class LineupRepository(Protocol):
    async def get(self, id: ID) -> Optional[Lineup]:
        ...

    async def add(self, lineup: Lineup) -> None:
        ...

    async def remove(self, id: ID) -> None:
        ...

    async def list(self) -> List[Lineup]:
        ...