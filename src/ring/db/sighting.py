from pydantic import BaseModel, Field
from ring.db.abstract import CosmosContainer, CosmosModel

from enum import Enum


class Habitat(str, Enum):
    WASSER = "wasser"
    LAND = "land"
    AIR = "air"
    UNKNOWN = "-"


class LivingType(str, Enum):
    MAUSER = "mausernd"
    BRUT = "brütend"
    NOT_BRUT = "nicht-brütend"
    UNKNOWN = "-"


class Sighting(CosmosModel):
    place: str
    reading: str
    ring: str | None = None
    year: int = Field(..., ge=1900, le=2100)
    month: int = Field(..., ge=1, le=12)
    day: int = Field(..., ge=1, le=31)
    group: int | None = None
    area_group: int | None = None
    habitat: Habitat = Habitat.UNKNOWN
    living_type: LivingType = LivingType.UNKNOWN
    comment: str | None = None
    melder: str | None = None
    melded: bool = False


class Sightings(CosmosContainer):
    def __init__(self):
        self.Type = Sighting
        super().__init__()


if __name__ == "__main__":
    sightings = Sightings()

    from ring.db.rings import Ring, Rings
    from ring.db.places import Place, Places
    import random

    all_rings = Rings().all()
    all_places = Places().all()

    x = [
        Sighting(
            place=random.choice(all_places).id,
            ring=random.choice(all_rings).id,
            year=2021,
            month=random.randint(1, 12),
            day=random.randint(1, 28),
            hour=random.randint(5, 21),
            minute=random.randint(0, 59),
        )
        for x in range(100)
    ]

    for sighting in x:
        sightings.upsert(sighting)
