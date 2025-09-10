import os
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
import sys
import os




project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)
from logging_setup.setup import setup_logger

# Create a logger that writes to logs/resource_group.log
logger = setup_logger(__name__, "resource_group.log")


def create_resource_group(subscription_id: str, resource_group_name: str, location: str):
    try:
        logger.info("Authenticating with Azure...")
        credential = DefaultAzureCredential()

        resource_client = ResourceManagementClient(credential, subscription_id)
        logger.info(f"Using subscription ID: {subscription_id}")

        logger.info(f"Creating or updating resource group '{resource_group_name}' in '{location}'...")
        rg = resource_client.resource_groups.create_or_update(
            resource_group_name,
            {"location": location}
        )
        logger.info(f"Resource group '{rg.name}' created in location '{rg.location}'")
        return rg

    except Exception:
        logger.error("Failed to create resource group", exc_info=True)
        raise
