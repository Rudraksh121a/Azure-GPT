from dotenv import load_dotenv
import os
from azure.identity import DefaultAzureCredential
from resource_group import create_resource_group

from cosmodb import create_cosmos_db_account

load_dotenv()

subscription_id = os.environ["AZURE_SUBSCRIPTION_ID"]
RESOURCE_GROUP_NAME = os.environ["AZURE_RESOURCE_GROUP_NAME"]
LOCATION = os.environ["LOCATION"]
cosmos_db_account_name = os.environ.get("COSMOS_DB_ACCOUNT_NAME")  # default value if not set
COSMOS_DB_DATABASE_ID = os.environ.get("COSMOS_DB_DATABASE_ID")
COSMOS_DB_CONTAINER_ID = os.environ.get("COSMOS_DB_CONTAINER_ID")
COSMOS_DB_PARTITION_KEY_PATH = os.environ.get("COSMOS_DB_PARTITION_KEY_PATH")
credential = DefaultAzureCredential()

def main():
    print("Starting infrastructure setup...")

    rg = create_resource_group(subscription_id, RESOURCE_GROUP_NAME, LOCATION, credential=credential)
    print(f"Resource Group '{rg.name}' created in location '{rg.location}'")

    create_cosmos_db_account(
        subscription_id=subscription_id,
        resource_group_name=RESOURCE_GROUP_NAME,
        account_name=cosmos_db_account_name,
        location=LOCATION,
        credential=credential,
        cosmos_database_id=COSMOS_DB_DATABASE_ID,
        container_id=COSMOS_DB_CONTAINER_ID,
        partition_key_path=COSMOS_DB_PARTITION_KEY_PATH
    )


if __name__ == "__main__":
    main()