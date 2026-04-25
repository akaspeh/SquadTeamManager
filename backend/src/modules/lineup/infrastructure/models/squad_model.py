import uuid
from sqlalchemy import String, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

from src.infrastructure.persistence import BaseModel


class SquadModel(BaseModel):
    __tablename__ = "squads"

    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    lineup_id: Mapped[str] = mapped_column(ForeignKey("lineups.id"))
    name: Mapped[str] = mapped_column(String, default="default_squad")
    created_at: Mapped[datetime] = mapped_column(DateTime)

    lineup: Mapped["LineupModel"] = relationship(back_populates="squads")

    members: Mapped[list["SquadMemberModel"]] = relationship(
        back_populates="squad",
        cascade="all, delete-orphan",
        lazy="selectin",
    )