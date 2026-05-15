from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.modules.lineup.application.interfaces import LineupRepository
from src.modules.lineup.domain.aggregate_root import Lineup
from src.modules.lineup.domain.value_objects import ID
from src.modules.lineup.infrastructure.mappers.lineup_mappers import to_domain_lineup, to_model_lineup
from src.modules.lineup.infrastructure.mappers.squad_mappers import to_model_squad

from src.modules.lineup.infrastructure.models import LineupModel


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

    async def save(self, lineup: Lineup) -> None:
        stmt = select(LineupModel).where(LineupModel.id == str(lineup.id))
        result = await self.session.execute(stmt)
        model = result.scalar_one_or_none()

        if not model:
            raise ValueError("Lineup not found")

        model.name = lineup.name

        model.squads = [
            to_model_squad(squad)
            for squad in lineup.squads
        ]

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