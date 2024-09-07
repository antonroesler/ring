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
    ...
