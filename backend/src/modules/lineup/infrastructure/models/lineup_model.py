import uuid
from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

from infrastructure.persistence import BaseModel


class LineupModel(BaseModel):
    __tablename__ = "lineups"

    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name: Mapped[str] = mapped_column(String, default="default_lineup")
    created_at: Mapped[datetime] = mapped_column(DateTime)

    squads: Mapped[list["SquadModel"]] = relationship(
        back_populates="lineup",
        cascade="all, delete-orphan",
        lazy="selectin",
    )





