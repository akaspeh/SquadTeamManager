from pydantic import BaseModel
from typing import List


class SquadMemberResponse(BaseModel):
    id: str
    name: str
    kit: str
    role: str


class SquadResponse(BaseModel):
    id: str
    name: str
    members: List[SquadMemberResponse]


class LineupResponse(BaseModel):
    id: str
    name: str
    squads: List[SquadResponse]

