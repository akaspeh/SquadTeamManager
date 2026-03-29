from pydantic import BaseModel

class LineUpListItemDTO(BaseModel):
    id: str
    name: str