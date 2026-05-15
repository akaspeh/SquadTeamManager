from shared.infrastructure.database import data_base_manager
from modules.lineup.infrastructure.unit_of_work import SqlAlchemyLineupUnitOfWork
from typing import AsyncGenerator

async def get_uow() -> AsyncGenerator[SqlAlchemyLineupUnitOfWork, None]:
    uow = SqlAlchemyLineupUnitOfWork(data_base_manager.session_factory)
    async with uow:
        yield uow