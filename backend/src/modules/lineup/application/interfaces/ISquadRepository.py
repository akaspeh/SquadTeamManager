from abc import ABC, abstractmethod
from backend.src.modules.lineup.domain.aggregates.Squad import Squad

class ISquadRepository(ABC):

    @abstractmethod
    def save(self, squad: Squad) -> None:
        """Persist the squad"""

    @abstractmethod
    def get_by_id(self, squad_id: str) -> Squad:
        """Retrieve squad by its ID"""

    @abstractmethod
    def delete(self, squad_id: str) -> None:
        """Delete squad by its ID"""