from config.database import DBconfig
from config.run import RunConfig
from config.api import ApiConfig
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    run_config: RunConfig = RunConfig()
    api_config: ApiConfig = ApiConfig()
    db_config: DBconfig = DBconfig()


settings = Settings()
