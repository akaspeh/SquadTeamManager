from pydantic import BaseModel

class SquadDTO(BaseModel):
    id: str
    name: str
