from typing import Protocol

from modules.lineup.application.interfaces import LineupRepository
from shared.application.base_unit_of_work import BaseUnitOfWork


class LineupUnitOfWork(BaseUnitOfWork, Protocol):
    @property
    def lineups(self) -> LineupRepository:
        ...