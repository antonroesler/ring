from azure.identity import DefaultAzureCredential
from azure.cosmos import CosmosClient
from ring.conf import settings
import streamlit as st

credential = DefaultAzureCredential()


@st.cache_resource(ttl=600)
def get_client():
    # Create a new client and connect to the server
    client = CosmosClient(url=settings.mongo_uri, credential=credential)
    return client


if __name__ == "__main__":
    # Send a ping to confirm a successful connection
    try:
        client = get_client()
        db = client.get_database_client(settings.db_name)
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
