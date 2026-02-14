from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, async_sessionmaker
from backend.src.config import settings

class Database:
    def __init__(self):
        self.engine: AsyncEngine = create_async_engine(
            settings.db_config.url,
            pool_size=settings.db_config.pool_size,
            max_overflow=settings.db_config.max_overflow,
            pool_timeout=settings.db_config.pool_timeout,
            pool_recycle=settings.db_config.pool_recycle,
            echo=settings.db_config.echo,
            pool_pre_ping=True,
        )
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            expire_on_commit=False,
            autocommit=False
        )

    async def dispose(self):
        await self.engine.dispose()

    async def get_session(self):
        async with self.session_factory() as session:
            yield session


DataBaseManager = Database()