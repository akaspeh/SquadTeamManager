from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from modules.lineup.api.ws.connection_manager import connection_manager
from modules.lineup.application.use_cases.add_player_to_squad import AddPlayerToSquad
from modules.lineup.application.use_cases.change_player_kit import ChangePlayerKit
from modules.lineup.application.use_cases.change_player_name import ChangePlayerName
from modules.lineup.application.use_cases.change_squad_name import ChangeSquadName
from modules.lineup.application.use_cases.remove_player_from_squad import RemovePlayerFromSquad
from modules.lineup.application.use_cases.add_squad_to_lineup import AddSquadToLineup
from modules.lineup.application.use_cases.remove_squad_from_lineup import RemoveSquadFromLineup
from modules.lineup.application.use_cases.change_squad_color import ChangeSquadColor
from modules.lineup.infrastructure.unit_of_work import SqlAlchemyLineupUnitOfWork
from shared.infrastructure.database import data_base_manager

router = APIRouter(prefix="/lineups", tags=["lineups"])


@router.websocket("/{lineup_id}/ws")
async def lineup_ws(websocket: WebSocket, lineup_id: str):
    await connection_manager.connect(lineup_id, websocket)

    try:
        while True:
            message = await websocket.receive_json()
            action = message.get("action")
            data = message.get("data", {})

            async with SqlAlchemyLineupUnitOfWork(data_base_manager.session_factory) as uow:
                event = None
                # --- SQUAD ---
                if action == "add_squad":
                    use_case = AddSquadToLineup(uow)
                    squad_id = await use_case.execute(
                        lineup_id=lineup_id,
                        name=data["name"],
                    )
                    event = {
                        "type": "squad_added",
                        "data": {
                            "squad_id": squad_id,
                            "name": data["name"]
                        }
                    }

                elif action == "remove_squad":
                    use_case = RemoveSquadFromLineup(uow)
                    await use_case.execute(
                        lineup_id=lineup_id,
                        squad_id=data["squad_id"],
                    )
                    event = {
                        "type": "squad_removed",
                        "data": data
                    }


                elif action == "add_player":
                    use_case = AddPlayerToSquad(uow)
                    player_id = await use_case.execute(
                        lineup_id=lineup_id,
                        squad_id=data["squad_id"],
                        name=data["name"],
                        kit=data["kit"],
                        role=data["role"],
                    )
                    event = {
                        "type": "player_added",
                        "data": {
                            "player_id": player_id,
                            **data
                        }
                    }

                elif action == "remove_player":
                    use_case = RemovePlayerFromSquad(uow)
                    await use_case.execute(
                        lineup_id=lineup_id,
                        squad_id=data["squad_id"],
                        member_id=data["member_id"],
                    )
                    event = {
                        "type": "player_removed",
                        "data": data
                    }

                elif action == "change_squad_color":
                    use_case = ChangeSquadColor(uow)
                    await use_case.execute(
                        lineup_id=lineup_id,
                        squad_id=data["squad_id"],
                        color=data["color"],
                    )
                    event = {
                        "type": "squad_color_changed",
                        "data": {
                            "squad_id": data["squad_id"],
                            "color": data["color"],
                        }
                    }

                elif action == "change_squad_name":
                    use_case = ChangeSquadName(uow)
                    await use_case.execute(
                        lineup_id=lineup_id,
                        squad_id=data["squad_id"],
                        name=data["name"],
                    )
                    event = {
                        "type": "squad_name_changed",
                        "data": {
                            "squad_id": data["squad_id"],
                            "name": data["name"],
                        }
                    }

                elif action == "change_player_kit":
                    use_case = ChangePlayerKit(uow)
                    await use_case.execute(
                        lineup_id=lineup_id,
                        squad_id=data["squad_id"],
                        member_id=data["member_id"],
                        kit=data["kit"],
                    )
                    event = {
                        "type": "player_kit_changed",
                        "data": data
                    }

                elif action == "change_player_name":
                    use_case = ChangePlayerName(uow)
                    await use_case.execute(
                        lineup_id=lineup_id,
                        squad_id=data["squad_id"],
                        member_id=data["member_id"],
                        name=data["name"],
                    )
                    event = {
                        "type": "player_name_changed",
                        "data": data
                    }

                else:
                    await websocket.send_json({
                        "type": "error",
                        "message": f"Unknown action: {action}"
                    })
                    continue


            # broadcast ONLY after successful commit
            await connection_manager.broadcast(lineup_id, event)

    except WebSocketDisconnect:
        connection_manager.disconnect(lineup_id, websocket)

    except Exception as e:
        await websocket.send_json({
            "type": "error",
            "message": str(e)
        })