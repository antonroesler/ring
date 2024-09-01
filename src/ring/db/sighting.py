from pydantic import BaseModel, Field
from ring.db.abstract import MongoBaseModel


class Sighting(BaseModel):
    place: str
    ring: str
    year: int = Field(..., ge=1900, le=2100)
    month: int = Field(..., ge=1, le=12)
    day: int = Field(..., ge=1, le=31)
    hour: int = Field(..., ge=0, le=23)
    minute: int = Field(..., ge=0, le=59)


class Sightings(MongoBaseModel):
    def __init__(self):
        self.Type = Sighting
        super().__init__()

    def insert(self, obj: BaseModel):
        assert isinstance(obj, self.Type)
        print(f"Inserting {obj}")
        if self.exists(obj):
            raise ValueError("Object already exists")
        self.collection.insert_one(obj.model_dump())

    def exists(self, obj: BaseModel):
        assert isinstance(obj, Sighting)
        return (
            self.collection.find_one({"ring": obj.ring, "place": obj.place}) is not None
        )

    def get(self, ring: str | None = None, place: str | None = None):
        assert ring is not None or place is not None
        if ring is not None:
            obj = self.collection.find_one({"ring": ring})
        else:
            obj = self.collection.find_one({"place": place})
        if obj is not None:
            return Sighting(**obj)

    def delete(self, ring, place):
        self.collection.delete_one({"ring": ring, "place": place})

    def update(self, ring: str, place: str, obj: Sighting):
        self.collection.update_one(
            {"ring": ring, "place": place}, {"$set": obj.model_dump()}
        )
