
import asyncio
from fastapi import FastAPI
import uvicorn
from contextlib import asynccontextmanager
from src.infrastructure.persistence.database import data_base_manager
from src.modules.lineup.api.routes.lineup import router as lineup_router  # твои endpoints
from src.modules.lineup.api.ws.lineup_ws import router as lineup_router_ws  # твои endpoints


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
    uvicorn.run("src.main:app", host="localhost", port=8000, reload=True)
