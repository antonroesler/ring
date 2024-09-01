from typing import Type
from pydantic import BaseModel
from ring.db.client import get_client
from ring.conf import settings


class MongoBaseModel:
    def __init__(self):
        self.Type: Type[BaseModel]
        self.key: str
        self.client = get_client()
        self.db = self.client[settings.db_name]
        self.collection_name = self.__class__.__name__.lower()
        self.collection = self.db[self.collection_name]
        print(f"Connected to {settings.db_name} database")
        print(f"Using collection {self.collection_name}")

    def insert(self, obj: BaseModel):
        assert isinstance(obj, self.Type)
        print(f"Inserting {obj}")
        if self.exists(obj):
            raise ValueError("Object already exists")
        self.collection.insert_one(obj.model_dump())

    def exists(self, obj: BaseModel):
        assert isinstance(obj, self.Type)
        return (
            self.collection.find_one({self.key: obj.model_dump()[self.key]}) is not None
        )

    def get(self, name: str):
        obj = self.collection.find_one({self.key: name})
        if obj is not None:
            return self.Type(**obj)
        return None

    def all(self):
        return [self.Type(**obj) for obj in self.collection.find()]

    def delete(self, name: str):
        self.collection.delete_one({self.key: name})

    def update(self, name: str, obj: BaseModel):
        assert isinstance(obj, self.Type)
        self.collection.update_one({self.key: name}, {"$set": obj.model_dump()})
