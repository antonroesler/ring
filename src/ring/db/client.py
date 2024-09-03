from azure.identity import DefaultAzureCredential
from azure.cosmos import CosmosClient
from uuid import uuid4
from ring.conf import settings

credential = DefaultAzureCredential()


def get_client():
    # Create a new client and connect to the server
    client = CosmosClient(url=settings.mongo_uri, credential=credential)
    return client


if __name__ == "__main__":
    # Send a ping to confirm a successful connection
    try:
        client = get_client()
        db = client.get_database_client("ring-db")
        container = db.get_container_client("brids")
        print(dir(container))
        x = container.read_all_items()
        print(x)
        for y in x:
            print(y)
        # query = "SELECT * FROM brids"
        # results = list(
        #     container.query_items(query=query, enable_cross_partition_query=True)
        # )
        # for item in results:
        #     print(item)
        #     print()

        print("Connected to the database")
    except Exception as e:
        print(e)
