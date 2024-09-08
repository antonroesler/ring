from ring.db.abstract import CosmosContainer, CosmosModel


class Place(CosmosModel):
    name: str
    lon: float | None = None
    lat: float | None = None
    desc: str | None = None


class Places(CosmosContainer):
    def __init__(self):
        self.Type = Place
        super().__init__()


if __name__ == "__main__":
    line_counter = 0
    _Places = Places()

    with open("/Users/RNS4ABT/mystuff/gaense/orte.csv") as f:
        for line in f:
            _, Ort, lat, lon = line.split("|")
            places = _Places.query(f"WHERE c.name = '{Ort}'")
            if len(places) == 0:
                ...
            if len(places) == 1:
                place: Place = places[0]
                assert place.name == Ort
                if not place.lon is None or not place.lat is None:
                    print(place)
                    print(lon)
                    print(lat)
                    print("Already has coordinates")
                    continue
                place.lon = float(lon)
                place.lat = float(lat)
                _Places.upsert(place)
