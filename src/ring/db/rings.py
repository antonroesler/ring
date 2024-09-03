from ring.db.client import get_client
from pydantic import BaseModel
from ring.db.abstract import CosmosContainer, CosmosModel


class Ring(CosmosModel):
    num: str
    species: str | None = None
    color: str | None = None
    desc: str | None = None


class Rings(CosmosContainer):
    def __init__(self):
        self.Type = Ring
        super().__init__()


if __name__ == "__main__":
    rings = Rings()

    a = [
        Ring(num="DEWAG 1234", species="69d0eda0-e9c2-46fb-abd3-cfb104f89055"),
        Ring(num="DEWAG 1235", species="69d0eda0-e9c2-46fb-abd3-cfb104f89055"),
        Ring(num="DEWAG 1236", species="69d0eda0-e9c2-46fb-abd3-cfb104f89055"),
        Ring(num="DEWAG 1237", species="69d0eda0-e9c2-46fb-abd3-cfb104f89055"),
        Ring(num="DEWAG 1238", species="69d0eda0-e9c2-46fb-abd3-cfb104f89055"),
        Ring(num="DEWAG 1239", species="69d0eda0-e9c2-46fb-abd3-cfb104f89055"),
        Ring(num="DEWAG 1240", species="69d0eda0-e9c2-46fb-abd3-cfb104f89055"),
        Ring(num="DEWAG 1241", species="69d0eda0-e9c2-46fb-abd3-cfb104f89055"),
        Ring(num="DEWAG 1242", species="69d0eda0-e9c2-46fb-abd3-cfb104f89055"),
        Ring(num="CY0032", species="320dca25-45f5-496e-a967-066faa264f60"),
        Ring(num="CY0033", species="320dca25-45f5-496e-a967-066faa264f60"),
        Ring(num="A1234", species="d70807a1-7f9e-4282-85bc-456376a47994"),
        Ring(num="A1235", species="d70807a1-7f9e-4282-85bc-456376a47994"),
        Ring(num="A1236", species="d70807a1-7f9e-4282-85bc-456376a47994"),
        Ring(num="A1237", species="d70807a1-7f9e-4282-85bc-456376a47994"),
        Ring(num="A1238", species="d70807a1-7f9e-4282-85bc-456376a47994"),
        Ring(num="A1239", species="d70807a1-7f9e-4282-85bc-456376a47994"),
        Ring(num="DEX000947362", species="320dca25-45f5-496e-a967-066faa264f60"),
        Ring(num="DEX000947363", species="320dca25-45f5-496e-a967-066faa264f60"),
        Ring(num="DEX000947364", species="320dca25-45f5-496e-a967-066faa264f60"),
        Ring(num="DEX000947365", species="320dca25-45f5-496e-a967-066faa264f60"),
        Ring(num="DEX000947366", species="320dca25-45f5-496e-a967-066faa264f60"),
        Ring(num="DEX000947367", species="320dca25-45f5-496e-a967-066faa264f60"),
        Ring(num="DEX000947368", species="320dca25-45f5-496e-a967-066faa264f60"),
        Ring(num="DEX000947369", species="320dca25-45f5-496e-a967-066faa264f60"),
        Ring(num="DEX000947370", species="320dca25-45f5-496e-a967-066faa264f60"),
        Ring(num="DEX000947371", species="320dca25-45f5-496e-a967-066faa264f60"),
        Ring(num="DEX000947372", species="320dca25-45f5-496e-a967-066faa264f60"),
        Ring(num="DEX000947373", species="320dca25-45f5-496e-a967-066faa264f60"),
        Ring(num="DEX000947374", species="320dca25-45f5-496e-a967-066faa264f60"),
        Ring(num="DEX000947375", species="320dca25-45f5-496e-a967-066faa264f60"),
        Ring(num="DEX000947376", species="320dca25-45f5-496e-a967-066faa264f60"),
    ]
    for ring in a:
        rings.upsert(ring)
