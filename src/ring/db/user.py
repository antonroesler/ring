from enum import Enum
from ring.db.abstract import CosmosContainer, CosmosModel


class Role(str, Enum):
    ADMIN = "ADMIN"
    OWNER = "OWNER"
    USER = "USER"
    VISITOR = "VISITOR"


class User(CosmosModel):
    username: str = "new-user"
    role: Role = Role.USER


class Users(CosmosContainer):
    def __init__(self):
        self.Type = User
        super().__init__()
