import uuid
from sqlalchemy import String, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

from shared.infrastructure import BaseModel

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from modules.lineup.infrastructure.models.squad_model import SquadModel


class SquadMemberModel(BaseModel):
    __tablename__ = "squad_members"

    id: Mapped[str] = mapped_column(
        String, primary_key=True, default=lambda: str(uuid.uuid4())
    )
    squad_id: Mapped[str] = mapped_column(ForeignKey("squads.id"))

    name: Mapped[str] = mapped_column(String, default="some_member")
    kit: Mapped[str] = mapped_column(String, default="Unarmed")
    role: Mapped[str] = mapped_column(String, default="flex")

    created_at: Mapped[datetime] = mapped_column(DateTime)

    squad: Mapped["SquadModel"] = relationship(back_populates="members")
