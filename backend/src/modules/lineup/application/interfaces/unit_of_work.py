from typing import Protocol

from modules.lineup.application.interfaces import LineupRepository


class UnitOfWork(Protocol):
    @property
    def lineups(self) -> LineupRepository:
        ...

    async def __aenter__(self) -> "UnitOfWork":
        ...

    async def __aexit__(self, exc_type, exc, tb):
        ...

    async def rollback(self):
        ...

    async def commit(self):
        ...