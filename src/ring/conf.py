from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    app_name: str = "ring"
    db_name: str = "ring-db"
    mongo_uri: str = Field(env="MONGO_URI")
    local_mode: bool = Field(env="LOCAL_MODE", default=False)


settings = Settings()
