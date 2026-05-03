from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from modules.lineup.application.interfaces import LineupRepository
from modules.lineup.domain.aggregate_root import Lineup
from modules.lineup.domain.value_objects import ID
from modules.lineup.infrastructure.mappers.lineup_mappers import to_domain_lineup, to_model_lineup

from modules.lineup.infrastructure.models import LineupModel


class SqlAlchemyLineupRepository(LineupRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get(self, id: ID) -> Lineup | None:
        stmt = select(LineupModel).where(LineupModel.id == str(id))

        result = await self.session.execute(stmt)
        model = result.scalar_one_or_none()

        if not model:
            return None

        return to_domain_lineup(model)

    async def add(self, lineup: Lineup) -> None:
        model = to_model_lineup(lineup)
        self.session.add(model)

    async def remove(self, id: ID) -> None:
        stmt = select(LineupModel).where(LineupModel.id == str(id))
        result = await self.session.execute(stmt)

        model = result.scalar_one_or_none()

        if model:
            await self.session.delete(model)

    async def list(self) -> list[Lineup]:
        stmt = select(LineupModel)

        result = await self.session.execute(stmt)
        models = result.scalars().all()

        return [to_domain_lineup(m) for m in models]