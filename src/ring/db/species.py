from ring.db.client import get_client
from pydantic import BaseModel
from ring.db.abstract import MongoBaseModel


class BirdSpecies(BaseModel):
    name: str
    name_latin: str


class Species(MongoBaseModel):
    def __init__(self):
        self.Type = BirdSpecies
        self.key = "name"
        super().__init__()


if __name__ == "__main__":
    species = Species()
    ...
