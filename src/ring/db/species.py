from ring.db.client import get_client
from pydantic import BaseModel
from ring.db.abstract import CosmosContainer, CosmosModel


class BirdSpecies(CosmosModel):
    name: str
    name_latin: str | None = None


class Species(CosmosContainer):
    def __init__(self):
        self.Type = BirdSpecies
        super().__init__()


if __name__ == "__main__":
    species = Species()

    x = species.query("WHERE c.name LIKE '%gans%'")
    print(x)
