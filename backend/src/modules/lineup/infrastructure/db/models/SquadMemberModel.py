from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from src.infrastructure.persistence.BaseModel import BaseModel
from sqlalchemy import text

class SquadMemberModel(BaseModel):
    __tablename__ = "squad_members"

    id: Mapped[str] = mapped_column(String, primary_key=True, server_default=text("gen_random_uuid()"))
    squad_id: Mapped[str] = mapped_column(String, ForeignKey("squads.id"))
    kit_name: Mapped[str] = mapped_column(String)
    player_name: Mapped[str | None] = mapped_column(String, nullable=True)

    squad: Mapped["SquadModel"] = relationship(back_populates="members")