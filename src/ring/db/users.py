from ring.db.client import get_client
from ring.conf import settings
import hashlib

client = get_client()

users_container = client.get_database_client(settings.db_name).get_container_client(
    "users"
)


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


def validate_user(username: str, password: str) -> bool:
    hashed_password = hash_password(password)
    query = f"SELECT * FROM c WHERE c.username = '{username}' AND c.password = '{hashed_password}'"
    results = list(
        users_container.query_items(query=query, enable_cross_partition_query=True)
    )
    return len(results) > 0


def create_user(username: str, password: str) -> bool:
    hashed_password = hash_password(password)
    user = {"username": username, "password": hashed_password, "id": username}
    try:
        users_container.create_item(user)
        return True
    except Exception as e:
        print(e)
        return False


if __name__ == "__main__":
    ...
