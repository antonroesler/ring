import datetime
from enum import Enum
from ring.db.abstract import CosmosContainer, CosmosModel
from pydantic import BaseModel
from ring.db.places import Place, Places
from ring.db.species import BirdSpecies, Species


class Habitat(str, Enum):
    WASSER = "Wasser"
    LAND = "Ackerland"
    AIR = "Flug"
    UNKNOWN = "-"


class LivingType(str, Enum):
    MAUSER = "Mausernd"
    BRUT = "Brütend"
    NOT_BRUT = "Nicht-brütend"
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
    living_type: LivingType = LivingType.UNKNOWN
    comment: str | None = None
    melder: str | None = None
    melded: bool = False


class Bird(CosmosModel):
    id: str
    species: str | None = None
    ring_age: str | None = None
    gender: str | None = None
    sightings: list[Sighting] = []


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


if __name__ == "__main__":
    added_places = set()
    added_species = set()
    species = Species()
    birds = Birds()
    places = Places()
    birds.upsert(Bird(id="unbekannt", species="unbekannt"))
    with open("/Users/RNS4ABT/mystuff/gaense/sightings.csv") as f:
        for line in f:
            (
                _,
                Art,
                Nummer,
                Ablesung,
                Datum,
                Ort,
                strAge,
                Gruppe,
                Bemerkung,
                Melder,
                gemeldet,
            ) = line.strip().split("|")
            try:
                date = datetime.datetime.strptime(
                    Datum.strip().split(" ")[0], "%Y-%m-%d"
                )
            except ValueError:
                print(f"Could not parse date {Datum}")
                continue
            g = None
            ag = None
            if str(Gruppe).isdigit():
                g = int(Gruppe)
            elif str(Gruppe).split(" ")[0].isdigit():
                g = int(str(Gruppe).split(" ")[0])
                if (
                    str(Gruppe)
                    .split(" ")[1]
                    .replace("(", "")
                    .replace(")", "")
                    .isdigit()
                ):
                    ag = int(
                        str(Gruppe).split(" ")[1].replace("(", "").replace(")", "")
                    )
            if Nummer is not None and Nummer != "":
                existing: Bird | None = birds.get(Nummer)
                if not existing:
                    print(f"Creating new bird {Nummer} of species {Art}")
                    bird = Bird(
                        id=Nummer,
                        species=Art,
                        ring_age=strAge if strAge != "" else None,
                    )
                    birds.upsert(bird)
                else:
                    print(f"Bird {Nummer} already exists ({Art}/{existing.species})")
                    assert existing.species == Art
            if Ort and Ort not in added_places:
                print(f"Adding place {Ort}")
                places.upsert(Place(name=Ort))
                added_places.add(Ort)
            if Art is None or Art == "":
                Art = "unbekannt"

            if Art and Art not in added_species:
                print(f"Adding species {Art}")
                species.upsert(BirdSpecies(name=Art))
                added_species.add(Art)

            s = Sighting(
                reading=Ablesung,
                place=Ort,
                year=None if not date else date.year,
                month=None if not date else date.month,
                day=None if not date else date.day,
                melded=True if gemeldet == "" else False,
                melder=Melder if Melder != "" else None,
                comment=Bemerkung if Bemerkung != "" else None,
                group=g,
                area_group=ag,
            )
            if Nummer is None or Nummer == "":
                Nummer = "unbekannt"

            birds.add_sighting(Nummer, s)
            print(f"Adding sighting to bird {Nummer} at {Ort}")
