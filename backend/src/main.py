import asyncio
from src.infrastructure.persistence.DataBase import DataBaseManager

async def init_db():
    await DataBaseManager.bootstrap_dev()

    print("Database initialized successfully.")


if __name__ == "__main__":
    asyncio.run(init_db())
