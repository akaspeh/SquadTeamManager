from src.config.database import *
from src.config.run import *
from src.config.api import *

class Settings(BaseSettings):
    run_config: RunConfig = RunConfig()
    api_config: ApiConfig = ApiConfig()
    db_config: DBconfig = DBconfig()

settings = Settings()
