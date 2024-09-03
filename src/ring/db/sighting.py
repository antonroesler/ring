from pydantic import BaseModel, Field
from ring.db.abstract import CosmosContainer, CosmosModel


class Sighting(CosmosModel):
    place: str
    ring: str
    year: int = Field(..., ge=1900, le=2100)
    month: int = Field(..., ge=1, le=12)
    day: int = Field(..., ge=1, le=31)
    hour: int = Field(..., ge=0, le=23)
    minute: int = Field(..., ge=0, le=59)


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
