from pydantic import BaseModel
from typing import List
from src.modules.lineup.application.DTO.SquadDTO import SquadDTO

class UpdateLineUpDTO(BaseModel):
    id: str
    name: str
    squads: List[SquadDTO]