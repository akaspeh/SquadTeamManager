from abc import ABC, abstractmethod
from src.modules.lineup.application.DTO.LineUpListItem import LineUpListItem
from src.modules.lineup.domain.aggregates.LineUp import LineUp


class ILineUpRepository(ABC):

    @abstractmethod
    async def save(self, lineup: LineUp) -> None:
        """Persist the lineup"""

    @abstractmethod
    async def get_by_id(self, lineup_id: str) -> LineUp:
        """Retrieve lineup by its ID"""

    @abstractmethod
    async def get_all(self) -> list[LineUp]:
        """Retrieve all lineups"""

    @abstractmethod
    async def get_list_items(self) -> list[LineUpListItem]: #can be moved to another repo for query requests
        """Lightweight list for frontend"""

    @abstractmethod
    async def delete(self, lineup_id: str) -> None:
        """Delete lineup by its ID"""


