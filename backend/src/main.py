from fastapi import FastAPI
import uvicorn
from contextlib import asynccontextmanager
from shared.infrastructure.database import data_base_manager
from modules.lineup.api.routes.lineup import router as lineup_router
from modules.lineup.api.ws.lineup_ws import router as lineup_router_ws


@asynccontextmanager
async def lifespan(app: FastAPI):
    await data_base_manager.bootstrap_dev()
    print("Database initialized successfully.")
    yield
    await data_base_manager.dispose()

app = FastAPI(title="Lineup Service API", lifespan=lifespan)
app.include_router(lineup_router)
app.include_router(lineup_router_ws)

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
