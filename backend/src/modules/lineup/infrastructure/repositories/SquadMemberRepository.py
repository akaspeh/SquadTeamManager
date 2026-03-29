from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from src.modules.lineup.domain.entities.SquadMember import SquadMember
from src.modules.lineup.domain.value_objects.Kit import Kit
from src.modules.lineup.infrastructure.models.SquadMemberModel import SquadMemberModel
from src.modules.lineup.application.interfaces.ISquadMemberRepository import ISquadMemberRepository
from src.modules.lineup.infrastructure.mappers.squad_member_mapper import domain_to_model, model_to_domain


class SquadMemberRepository(ISquadMemberRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def save(self, member: SquadMember, squad_id: str) -> None:
        """
        Save or update SquadMember in the database.
        squad_id is required to link member to a SquadModel.
        """
        model = await self.session.get(SquadMemberModel, member.id)

        if model is None:
            model = domain_to_model(member, squad_id)
            self.session.add(model)
        else:
            # Обновляем существующую модель
            model.player_name = member.player_name
            model.kit = member.kit.name
            model.squad_id = squad_id  # на случай перемещения в другой сквад

        await self.session.flush()

    async def get_by_id(self, member_id: str) -> SquadMember | None:
        stmt = select(SquadMemberModel).where(SquadMemberModel.id == member_id)
        result = await self.session.execute(stmt)
        model = result.scalar_one_or_none()

        if not model:
            return None

        return model_to_domain(model)

    async def delete(self, member_id: str) -> None:
        model = await self.session.get(SquadMemberModel, member_id)
        if model:
            await self.session.delete(model)
            await self.session.flush()