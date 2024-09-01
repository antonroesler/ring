from ring.db.client import get_client
from pydantic import BaseModel
from ring.db.abstract import MongoBaseModel


class Place(BaseModel):
    name: str
    lon: float | None = None
    lat: float | None = None
    desc: str | None = None


class Places(MongoBaseModel):
    def __init__(self):
        self.Type = Place
        self.key = "name"
        super().__init__()
