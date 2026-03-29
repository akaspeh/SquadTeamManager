from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from src.modules.lineup.domain.aggregates.LineUp import LineUp
from src.modules.lineup.infrastructure.models.LineUpModel import LineUpModel
from src.modules.lineup.application.interfaces.ILineUpRepository import ILineUpRepository
from src.modules.lineup.application.DTO.LineUpListItemDTO import LineUpListItemDTO


class LineUpRepository(ILineUpRepository):

    def __init__(self, session: AsyncSession):
        self.session = session

    async def save(self, lineup: LineUp) -> None:
        model = await self.session.get(LineUpModel, lineup.id)

        if model is None:
            model = LineUpModel(id=lineup.id, name=lineup.name)
            self.session.add(model)
        else:
            model.name = lineup.name

        await self.session.flush()

    async def get_by_id(self, lineup_id: str) -> LineUp | None:
        stmt = select(LineUpModel).where(LineUpModel.id == lineup_id)
        result = await self.session.execute(stmt)
        model = result.scalar_one_or_none()

        if not model:
            return None

        return self._to_domain(model)

    async def get_all(self) -> list[LineUp]:
        stmt = select(LineUpModel)
        result = await self.session.execute(stmt)
        models = result.scalars().all()

        return [self._to_domain(m) for m in models]

    async def get_list_items(self) -> list[LineUpListItemDTO]:
        stmt = select(LineUpModel.id, LineUpModel.name)
        result = await self.session.execute(stmt)

        return [
            LineUpListItemDTO(id=row.id, name=row.name)
            for row in result.all()
        ]

    async def delete(self, lineup_id: str) -> None:
        model = await self.session.get(LineUpModel, lineup_id)
        if model:
            await self.session.delete(model)
            await self.session.flush()

    def _to_domain(self, model: LineUpModel) -> LineUp:
        return LineUp(
            id=model.id,
            name=model.name,
        )