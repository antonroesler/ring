from typing import Any, Type
from uuid import uuid4
from pydantic import BaseModel
from ring.db.client import get_client
from ring.conf import settings


class CosmosModel(BaseModel):
    id: str | None = None

    def model_post_init(self, __context: Any) -> None:
        if self.id is None:
            self.id = str(uuid4())
        return super().model_post_init(__context)


class CosmosContainer:
    def __init__(self):
        self.Type: Type[CosmosModel]
        self.key: str = "id"
        self.client = get_client()
        self.db = self.client.get_database_client(settings.db_name)
        self.container_name = self.__class__.__name__.lower()
        self.container = self.db.get_container_client(self.container_name)
        print(f"Connected to {settings.db_name} database")
        print(f"Using container {self.container_name}")
        self.full_cache = {}

    def upsert(self, obj: CosmosModel):
        assert isinstance(obj, self.Type)
        self.container.upsert_item(obj.model_dump())

    def get(self, id: str):
        try:
            obj = self.container.read_item(
                item=id,
                partition_key=id,
            )
            return self.Type(**obj)
        except Exception:
            return None

    def all(self):
        if self.full_cache:
            return list(self.full_cache.values())
        print(f"Reading all items {self.container_name}")
        self.full_cache = {
            obj.get("id"): self.Type(**obj) for obj in self.container.read_all_items()
        }
        return list(self.full_cache.values())

    def delete(self, id):
        self.container.delete_item(item=id, partition_key=id)

    def query(self, filter: str):
        query = f"SELECT * FROM c {filter}"
        return [
            self.Type(**obj)
            for obj in self.container.query_items(
                query=query,
                enable_cross_partition_query=True,
            )
        ]
