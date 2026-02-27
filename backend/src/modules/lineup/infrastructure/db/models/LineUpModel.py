from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from typing import List
from src.infrastructure.persistence.BaseModel import BaseModel
from sqlalchemy import text

class LineUpModel(BaseModel):
    __tablename__ = "lineups"

    id: Mapped[str] = mapped_column(String, primary_key=True, server_default=text("gen_random_uuid()"))
    name: Mapped[str] = mapped_column(String)

    squads: Mapped[List["SquadModel"]] = relationship(
        back_populates="lineup",
        cascade="all, delete-orphan",
        lazy="selectin"
    )
