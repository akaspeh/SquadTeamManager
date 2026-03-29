from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from src.modules.lineup.domain.entities.Squad import Squad
from src.modules.lineup.infrastructure.models.SquadModel import SquadModel
from src.modules.lineup.application.interfaces.ISquadRepository import ISquadRepository


class SquadRepository(ISquadRepository):

    def __init__(self, session: AsyncSession):
        self.session = session

    async def save(self, squad: Squad) -> None:
        model = await self.session.get(SquadModel, squad.id)

        if model is None:
            model = SquadModel(
                id=squad.id,
                name=squad.name,
            )
            self.session.add(model)
        else:
            model.name = squad.name

        await self.session.flush()

    async def get_by_id(self, squad_id: str) -> Squad | None:
        stmt = select(SquadModel).where(SquadModel.id == squad_id)
        result = await self.session.execute(stmt)
        model = result.scalar_one_or_none()

        if not model:
            return None

        return self._to_domain(model)

    async def delete(self, squad_id: str) -> None:
        model = await self.session.get(SquadModel, squad_id)
        if model:
            await self.session.delete(model)
            await self.session.flush()

    def _to_domain(self, model: SquadModel) -> Squad:
        return Squad(
            id=model.id,
            name=model.name,
        )