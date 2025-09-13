from dotenv import load_dotenv
import os
import sys
from azure.identity import DefaultAzureCredential
from azure.cosmos import CosmosClient

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)
from logging_setup.setup import setup_logger
logger = setup_logger(__name__, "database.log")

load_dotenv()
COSMOS_DB_DATABASE_ID = os.environ.get("COSMOS_DB_DATABASE_ID")
COSMOS_DB_CONTAINER_ID = os.environ.get("COSMOS_DB_CONTAINER_ID")
COSMOS_ENDPOINT = os.environ.get("COSMOS_ENDPOINT")
COSMOS_KEY = os.environ.get("COSMOS_KEY")


def datainsert(data):
    # Connect client
    logger.info("Connecting to Cosmos DB...")
    client = CosmosClient(COSMOS_ENDPOINT, credential=COSMOS_KEY)

    # Get database & container (already created earlier)
    logger.info("Accessing database and container...")
    database = client.get_database_client(COSMOS_DB_DATABASE_ID)

    container = database.get_container_client(COSMOS_DB_CONTAINER_ID)
    logger.info("Inserting data into container...")
    container.upsert_item(data)
    logger.info("Inserted: %s", data)
    return data

def fatch_data():
    # Connect client
    logger.info("Connecting to Cosmos DB...")
    client = CosmosClient(COSMOS_ENDPOINT, credential=COSMOS_KEY)

    # Get database & container (already created earlier)
    logger.info("Accessing database and container...")
    database = client.get_database_client(COSMOS_DB_DATABASE_ID)

    container = database.get_container_client(COSMOS_DB_CONTAINER_ID)
    logger.info("Fetching data from container...")
    items = list(container.read_all_items())
    logger.info("Fetched %d items", len(items))
    roles = [item.get("role") for item in items if "role" in item]
    return roles

if __name__ == "__main__":
    print(fatch_data())