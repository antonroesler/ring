from enum import Enum
from pydantic import BaseModel


class Role(str, Enum):
    ADMIN = "ADMIN"
    OWNER = "OWNER"
    USER = "USER"
    VISITOR = "VISITOR"


class User(BaseModel):
    username: str = "new-user"
    role: Role = Role.USER


class Users(BaseModel):
    def __init__(self):
        self.Type = User
        super().__init__()
