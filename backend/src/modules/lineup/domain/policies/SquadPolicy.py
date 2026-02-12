from typing import List

from ..entities.SquadMember import SquadMember


class SquadPolicy:
    """
    Policy class for SquadLineUp domain rules.
    """

    MAX_PLAYERS = 9
    UNIQUE_KITS = ["Squad Leader"]  # можно заменить на List[KitEnum]

    @classmethod
    def validate_max_players(cls, lineup) -> None:
        if len(lineup.members) > cls.MAX_PLAYERS:
            raise ValueError(f"Squad cannot exceed {cls.MAX_PLAYERS} players")

    @classmethod
    def validate_unique_kit(cls, lineup, member: SquadMember) -> None:
        for m in lineup.members:
            if m.kit.name == member.kit.name and member.kit.name in cls.UNIQUE_KITS:
                raise ValueError(f"Unique kit {member.kit.name} already assigned")
