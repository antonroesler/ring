from ring.db.client import get_client
from pydantic import BaseModel
from ring.db.abstract import MongoBaseModel


class Ring(BaseModel):
    num: str
    species: str | None = None
    color: str | None = None
    desc: str | None = None


class Rings(MongoBaseModel):
    def __init__(self):
        self.Type = Ring
        self.key = "num"
        super().__init__()
