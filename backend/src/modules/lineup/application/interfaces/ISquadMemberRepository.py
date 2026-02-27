from abc import ABC, abstractmethod
from src.modules.lineup.domain.entities.Squad import Squad

class ISquadMemberRepository(ABC):

    @abstractmethod
    async def save(self, squad: Squad) -> None:
        """Persist the squad member"""

    @abstractmethod
    async def get_by_id(self, squad_id: str) -> Squad:
        """Retrieve squad member by its ID"""

    @abstractmethod
    async def delete(self, squad_id: str) -> None:
        """Delete squad member by its ID"""