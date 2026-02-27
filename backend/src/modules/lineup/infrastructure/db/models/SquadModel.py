from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from typing import List
from src.infrastructure.persistence.BaseModel import BaseModel
from sqlalchemy import text

class SquadModel(BaseModel):
    __tablename__ = "squads"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    name: Mapped[str] = mapped_column(String, default="Default LineUp", server_default=text("gen_random_uuid()"))
    lineup_id: Mapped[str] = mapped_column(String, ForeignKey("lineups.id"))

    lineup: Mapped["LineUpModel"] = relationship(back_populates="squads")

    members: Mapped[List["SquadMemberModel"]] = relationship(
        back_populates="squad",
        cascade="all, delete-orphan",
        lazy="selectin"
    )