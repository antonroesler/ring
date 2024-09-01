from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    app_name: str = "ring"
    db_name: str = "ring"
    mongo_uri: str = Field(env="MONGO_URI")  # "mongodb://root:example@localhost:27017/"


settings = Settings()
