from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from ring.conf import settings


def get_client():
    # Create a new client and connect to the server
    client = MongoClient(
        settings.mongo_uri,
        server_api=ServerApi(version="1", strict=True, deprecation_errors=True),
    )
    print(client.admin.command("ping"))
    return client


if __name__ == "__main__":
    # Send a ping to confirm a successful connection
    try:
        client = get_client()
        client.admin.command("ping")
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)
