from config.database import *
from config.run import *
from config.api import *

class Settings(BaseSettings):
    run_config: RunConfig = RunConfig()
    api_config: ApiConfig = ApiConfig()
    db_config: DBconfig = DBconfig()

settings = Settings()
