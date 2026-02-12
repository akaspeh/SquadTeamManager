import uuid
from dataclasses import dataclass, field

from typing import Optional
from ..value_objects.Kit import Kit

@dataclass
class SquadMember:
    """
    Entity representing a squad member (player assigned to a kit).
    """
    kit: Kit
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    player_name: Optional[str] = None
