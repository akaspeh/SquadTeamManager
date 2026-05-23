from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from modules.lineup.application.use_cases.create_lineup import CreateLineup
from modules.lineup.application.use_cases.get_all_lineups import GetAllLineups
from modules.lineup.application.use_cases.get_lineup import GetLineup
from modules.lineup.api.mappers import to_response
from modules.lineup.api.dependencies import get_uow
from modules.lineup.application.use_cases.remove_lineup import RemoveLineup
from shared.domain.exceptions import ValidationError
from modules.lineup.infrastructure.unit_of_work import SqlAlchemyLineupUnitOfWork

router = APIRouter(prefix="/lineups", tags=["lineups"])


# --- GET LIST ---
@router.get("/")
async def get_lineups(uow: SqlAlchemyLineupUnitOfWork = Depends(get_uow)):
    async with uow:
        use_case = GetAllLineups(uow)
        lineups = await use_case.execute()

        return [to_response(lineup) for lineup in lineups]


# --- GET ONE ---
@router.get("/{lineup_id}")
async def get_lineup(
    lineup_id: str, uow: SqlAlchemyLineupUnitOfWork = Depends(get_uow)
):
    async with uow:
        use_case = GetLineup(uow)
        return await use_case.execute(lineup_id)


@router.post("/")
async def create_lineup(name: str, uow: SqlAlchemyLineupUnitOfWork = Depends(get_uow)):
    async with uow:
        use_case = CreateLineup(uow)
        lineup_id = await use_case.execute(name)

        return {"id": lineup_id}


@router.delete("/{lineup_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_lineup(
    lineup_id: str, uow: SqlAlchemyLineupUnitOfWork = Depends(get_uow)
):
    async with uow:
        use_case = RemoveLineup(uow)

        try:
            await use_case.execute(lineup_id)
        except ValidationError as e:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
