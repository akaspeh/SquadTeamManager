from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, async_sessionmaker, AsyncSession
from backend.src.config import settings
from sqlalchemy import text
from infrastructure.persistence.base_model import BaseModel

async def init_dev_database(engine: AsyncEngine):
    async with engine.begin() as conn:
        await conn.execute(text('CREATE EXTENSION IF NOT EXISTS "pgcrypto";'))
        await conn.run_sync(BaseModel.metadata.drop_all)
        await conn.run_sync(BaseModel.metadata.create_all)

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

    async def get_session_for_dep(self):
        async with self.session_factory() as session:
            yield session

    async def bootstrap_dev(self):
        if settings.run_config.environment == "dev":
            await init_dev_database(self.engine)


data_base_manager = Database()