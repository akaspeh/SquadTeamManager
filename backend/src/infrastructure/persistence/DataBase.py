from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, async_sessionmaker
from backend.src.config import settings
from sqlalchemy import text
from src.infrastructure.persistence.BaseModel import BaseModel

async def init_dev_database(url: str):
    engine = create_async_engine(url)

    async with engine.begin() as conn:
        await conn.execute(text('CREATE EXTENSION IF NOT EXISTS "pgcrypto";'))
        await conn.run_sync(BaseModel.metadata.create_all)

    await engine.dispose()

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
        )

    async def dispose(self):
        await self.engine.dispose()

    async def get_session(self):
        async with self.session_factory() as session:
            yield session

    async def bootstrap_dev(self):
        if settings.run_config.environment == "dev":
            await init_dev_database(settings.db_config.url)


DataBaseManager = Database()