from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from src.modules.lineup.domain.entities.SquadMember import SquadMember
from src.modules.lineup.infrastructure.db.models.SquadMemberModel import SquadMemberModel
from src.modules.lineup.application.interfaces.ISquadMemberRepository import ISquadMemberRepository


class SquadMemberRepository(ISquadMemberRepository):

    def __init__(self, session: AsyncSession):
        self.session = session

    async def save(self, member: SquadMember) -> None:
        model = await self.session.get(SquadMemberModel, member.id)

        if model is None:
            model = SquadMemberModel(
                id=member.id,
                name=member.name,
                squad_id=member.squad_id
            )
            self.session.add(model)
        else:
            model.name = member.name

        await self.session.flush()

    async def get_by_id(self, member_id: str) -> SquadMember | None:
        stmt = select(SquadMemberModel).where(SquadMemberModel.id == member_id)
        result = await self.session.execute(stmt)
        model = result.scalar_one_or_none()

        if not model:
            return None

        return self._to_domain(model)

    async def delete(self, member_id: str) -> None:
        model = await self.session.get(SquadMemberModel, member_id)
        if model:
            await self.session.delete(model)
            await self.session.flush()

    def _to_domain(self, model: SquadMemberModel) -> SquadMember:
        return SquadMember(
            id=model.id,
            name=model.name,
            squad_id=model.squad_id
        )