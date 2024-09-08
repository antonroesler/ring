from ring.db.abstract import CosmosContainer, CosmosModel
from ring.db.sighting import Sighting
import datetime


class Ring(CosmosModel):
    species: str | None = None
    ring_age: int | None = None


class Rings(CosmosContainer):
    def __init__(self):
        self.Type = Ring
        super().__init__()


if __name__ == "__main__":
    rings = Rings()
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
            r = Ring(
                id=Nummer,
                species=Art,
                ring_age=int(float(strAge)) if strAge != "" else None,
            )
            try:
                date = datetime.datetime.strptime(
                    Datum.strip().split(" ")[0], "%Y-%m-%d"
                )
            except ValueError:
                continue
            print(Gruppe)
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
            s = Sighting(
                reading=Ablesung,
                place=Ort,
                species=Art,
                ring=r.id,
                year=None if not date else date.year,
                month=None if not date else date.month,
                day=None if not date else date.day,
                melded=True if gemeldet == "" else False,
                melder=Melder if Melder != "" else None,
                comment=Bemerkung if Bemerkung != "" else None,
                group=g,
                area_group=ag,
            )
            print(r)
            print(s)
