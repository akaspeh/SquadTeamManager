from dataclasses import dataclass

@dataclass(frozen=True)
class LineUpListItem:
    id: str
    name: str