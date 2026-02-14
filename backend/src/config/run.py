from pydantic_settings import BaseSettings

class RunConfig(BaseSettings):
    # network
    host: str = "0.0.0.0"
    port: int = 8080

    # environment
    debug: bool = False
    environment: str = "dev"   # dev | staging | prod

    # workers (for uvicorn/gunicorn)
    workers: int = 1

    # timeouts
    keep_alive_timeout: int = 5
    graceful_shutdown_timeout: int = 15

    # security toggles
    auth_enabled: bool = False
    https_only: bool = False

    # performance
    reload: bool = False  # hot reload for dev

    # observability
    access_log: bool = True

    class Config:
        env_prefix = "RUN_"
