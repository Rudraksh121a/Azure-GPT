from azure.mgmt.cosmosdb import CosmosDBManagementClient
from azure.cosmos import CosmosClient, PartitionKey
import os
from azure.identity import DefaultAzureCredential
import sys
from logging_setup.setup import setup_logger

# Create a logger that writes to logs/cosmosdb.log
logger = setup_logger(__name__, "cosmosdb.log")

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

def create_cosmos_db_account(
    subscription_id: str,
    resource_group_name: str,
    account_name: str,
    location: str,
    credential: DefaultAzureCredential,
    cosmos_database_id: str,
    container_id: str,
    partition_key_path: str
) -> tuple:
    try:
        cosmos_mgmt = CosmosDBManagementClient(credential, subscription_id)

        params = {
            "location": location,
            "locations": [{"location_name": location}],
            "kind": "GlobalDocumentDB",
            "properties": {
                "database_account_offer_type": "Standard"
            }
        }

        logger.info(f"Starting creation of Cosmos DB account: {account_name} in resource group: {resource_group_name}")
        poller = cosmos_mgmt.database_accounts.begin_create_or_update(
            resource_group_name,
            account_name,
            params
        )
        account = poller.result()
        logger.info(f"Cosmos DB account created: {account.name}")

        keys = cosmos_mgmt.database_accounts.list_keys(resource_group_name, account_name)
        primary_key = keys.primary_master_key
        endpoint = account.document_endpoint

        logger.info(f"Connecting to Cosmos DB endpoint: {endpoint}")
        cosmos_client = CosmosClient(endpoint, credential=primary_key)
        db = cosmos_client.create_database_if_not_exists(id=cosmos_database_id)
        logger.info(f"Database '{cosmos_database_id}' ensured/created.")

        container = db.create_container_if_not_exists(
            id=container_id,
            partition_key=PartitionKey(path=partition_key_path),
            offer_throughput=400
        )
        logger.info(f"database is created.")

        return endpoint, primary_key, container, True
    except Exception as e:
        logger.error(f"Error creating Cosmos DB account or resources: {e}")
        return None, False
