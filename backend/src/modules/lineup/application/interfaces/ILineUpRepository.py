from abc import ABC, abstractmethod
from backend.src.modules.lineup.domain.aggregates.LineUp import LineUp

class ILineUpRepository(ABC):

    @abstractmethod
    def save(self, lineup: LineUp) -> None:
        """Persist the lineup"""

    @abstractmethod
    def get_by_id(self, lineup_id: str) -> LineUp:
        """Retrieve lineup by its ID"""

    @abstractmethod
    def delete(self, lineup_id: str) -> None:
        """Delete lineup by its ID"""
