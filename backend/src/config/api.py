from pydantic import BaseSettings, Field

class ApiConfig(BaseSettings):
    prefix: str = "/api"

    version: str = "v1"

    allow_origins: list[str] = ["*"]
    allow_methods: list[str] = ["*"]
    allow_headers: list[str] = ["*"]

    request_timeout: int = 30
    connect_timeout: int = 5

    max_requests_per_minute: int = 1000

    docs_enabled: bool = True
    redoc_enabled: bool = True

    log_requests: bool = True

    class Config:
        env_prefix = "API_"
