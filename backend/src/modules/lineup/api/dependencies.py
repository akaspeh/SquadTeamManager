from shared.infrastructure.database import data_base_manager
from modules.lineup.infrastructure.unit_of_work import SqlAlchemyUnitOfWork
from typing import AsyncGenerator

async def get_uow() -> AsyncGenerator[SqlAlchemyUnitOfWork, None]:
    uow = SqlAlchemyUnitOfWork(data_base_manager.session_factory)
    async with uow:
        yield uow