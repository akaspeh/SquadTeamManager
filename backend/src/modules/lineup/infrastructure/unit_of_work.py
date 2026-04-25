from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from src.modules.lineup.application.interfaces import UnitOfWork, LineupRepository
from src.modules.lineup.infrastructure.repos.lineup_repo import SqlAlchemyLineupRepository


class SqlAlchemyUnitOfWork(UnitOfWork):
    def __init__(self, session_factory: async_sessionmaker[AsyncSession]):
        self._session_factory = session_factory
        self.session: AsyncSession | None = None

    async def __aenter__(self) -> "SqlAlchemyUnitOfWork":
        self.session = self._session_factory()
        return self

    async def __aexit__(self, exc_type, exc, tb):
        if not self.session:
            return

        try:
            if exc_type:
                await self.session.rollback()
            else:
                await self.session.commit()
        finally:
            await self.session.close()
            self.session = None

    async def commit(self):
        if not self.session:
            raise RuntimeError("Session not initialized")
        await self.session.commit()

    async def rollback(self):
        if not self.session:
            raise RuntimeError("Session not initialized")

        await self.session.rollback()

    @property
    def lineups(self) -> LineupRepository:
        if not self.session:
            raise RuntimeError("UoW not initialized")

        return SqlAlchemyLineupRepository(self.session)