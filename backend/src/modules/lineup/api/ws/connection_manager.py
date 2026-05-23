from collections import defaultdict
from fastapi import WebSocket


class ConnectionManager:
    def __init__(self):
        self.connections: dict[str, list[WebSocket]] = defaultdict(list)

    async def connect(self, lineup_id: str, ws: WebSocket):
        await ws.accept()
        self.connections[lineup_id].append(ws)

    def disconnect(self, lineup_id: str, ws: WebSocket):
        self.connections[lineup_id].remove(ws)

    async def broadcast(self, lineup_id: str, message: dict):
        for ws in self.connections[lineup_id]:
            await ws.send_json(message)


connection_manager = ConnectionManager()
