from modules.lineup.domain.aggregate_root import Lineup
from modules.lineup.api.schemas import LineupResponse, SquadResponse, SquadMemberResponse


def to_response(lineup: Lineup) -> LineupResponse:
    return LineupResponse(
        id=str(lineup.id),
        name=lineup.name,
        squads=[
            SquadResponse(
                id=str(s.id),
                name=s.name,
                members=[
                    SquadMemberResponse(
                        id=str(m.id),
                        name=m.name,
                        kit=m.kit.value,
                        role=m.role.value,
                    )
                    for m in s.members
                ],
                color=s.color,
            )
            for s in lineup.squads
        ],
    )