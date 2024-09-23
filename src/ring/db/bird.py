from enum import Enum
from typing import Literal
from ring.db.abstract import CosmosContainer, CosmosModel


class Habitat(str, Enum):
    ACKER_BRACHE = "Ackerbrache"
    ACKER_UMGEBROCHEN = "Acker umgebrochen"
    GETREIDESTOPPEL = "Getreidestoppel"
    GRUENANALGE = "Grünanlage"
    KARTOFFELN = "Kartoffeln"
    MAISSTOPPEL = "Maisstoppel"
    STOPPELACKER_U = "Stoppelacker unbestimmt"
    PARK = "Park"
    RAPSSTOPPEL = "Rapsstoppel"
    RUEBEN = "Rüben"
    SAAT = "Saat (jung)"
    UNKNOWN = "-"


class LivingStatus(str, Enum):
    BRUTVOGEL = "Brutvogel"
    EINZELTIER = "Einzeltier"
    FAMILIENVERBAND = "Familienverband"
    MAUSERGRUPPE = "Mausergruppe"
    SCHLAFPLATZ = "Schlafplatz"
    SCHULE = "Schule"
    VERPAART = "Verpaart"
    UNKNOWN = "-"


class Sighting(CosmosModel):
    place: str
    reading: str
    year: int | None = None
    month: int | None = None
    day: int | None = None
    group: int | None = None
    area_group: int | None = None
    habitat: Habitat = Habitat.UNKNOWN
    living_type: LivingStatus = LivingStatus.UNKNOWN
    comment: str | None = None
    melder: str | None = None
    melded: bool = False


class Bird(CosmosModel):
    id: str
    species: str | None = None
    ring_age: str | None = None
    gender: Literal["M", "W", None] = None
    sightings: list[Sighting] = []
    partner: str | None = None


class Birds(CosmosContainer):
    def __init__(self):
        self.Type = Bird
        super().__init__()

    def add_sighting(self, bird_id: str, species: str, sighting: Sighting):
        bird: Bird | None = self.get(bird_id)
        if bird is None:
            bird = Bird(id=bird_id, species=species)
            self.upsert(bird)
        bird.sightings.append(sighting)
        self.upsert(bird)

    def delete_sightings(self, bird_id: str, sighting_ids: list[str]):
        print(f"Deleting {sighting_ids} from {bird_id}")
        bird: Bird | None = self.get(bird_id)
        if bird is None:
            print(f"Bird {bird_id} not found")
            return
        print(f"Found bird {bird_id}")
        print(f"Before deletion: {bird.sightings}")
        bird.sightings = [s for s in bird.sightings if s.id not in sighting_ids]
        print(f"After deletion: {bird.sightings}")
        self.upsert(bird)

    def ring_query(self, contains: str) -> list[Bird] | None:
        contains = contains.strip().replace("…", "...")
        if contains.startswith("..."):
            return self.query(f"WHERE c.id LIKE '%{contains[3:]}'")
        if contains.endswith("..."):
            return self.query(f"WHERE c.id LIKE '{contains[:-3]}%'")
        return self.query(f"WHERE c.id LIKE '%{contains}%'")


if __name__ == "__main__":
    birds = Birds()
    for b in birds.container.read_all_items():
        try:
            Bird(**b)
        except Exception as e:
            print(b.get("id"))
