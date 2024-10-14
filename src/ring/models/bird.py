from enum import Enum
from typing import Literal
import uuid
from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime


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


def make_id():
    return str(uuid.uuid4())

class Sighting(BaseModel):
    id: str = Field(default_factory=make_id)
    creation_timestamp: datetime = Field(default_factory=datetime.now)
    ring: str | None = Field(None, alias="Ringnummer")
    color_ring: str | None = Field(None, alias="Farbring")
    date: datetime | None  = Field(None, alias="Datum")
    reading: str | None = Field(None, alias="Ablesung")
    reading_color_ring: str | None = Field(None, alias="Ablesung (Farbring)")
    species: str | None = Field(None, alias="Art")
    place: str | None = Field(None, alias="Ort")
    gender: Literal["M", "W", None] = Field(None, alias="Geschlecht")
    age: str | None = Field(None, alias="Alter")
    partner: str | None = Field(None, alias="Partner")
    group: int = Field(None, alias="Kleingruppengröße")
    area_group: int = Field(None, alias="Gruppengröße")
    habitat: Habitat = Field(Habitat.UNKNOWN, alias="Habitat")
    living_type: LivingStatus = Field(LivingStatus.UNKNOWN, alias="Typ")
    comment: str | None = Field(None, alias="Kommentar")
    melder: str | None = Field(None, alias="Melder")
    melded: bool = Field(False, alias="Gemeldet")
    sighting_group_id: int | None = Field(None, alias="Gruppen ID")

    model_config = ConfigDict(
        populate_by_name=True,
    )
