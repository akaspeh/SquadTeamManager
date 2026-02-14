from pydantic_settings import BaseSettings

class DBconfig(BaseSettings):
    url: str = "postgresql+asyncpg://postgres:some_password@localhost:5432/mydb"
    echo: bool = True
    pool_size: int = 5
    max_overflow: int = 10
    pool_timeout: int = 30
    pool_recycle: int = 1800
    pool_pre_ping: bool = True

    class Config:
        env_prefix = "DB_"