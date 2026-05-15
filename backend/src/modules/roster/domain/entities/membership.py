from dataclasses import dataclass

from modules.roster.domain.value_objects.membership_type import MembershipType
from shared.domain.value_objects import ID


@dataclass
class Membership:
    id: ID
    player_id: ID
    nickname: str
    membership_type: MembershipType