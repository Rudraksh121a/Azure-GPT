from dotenv import load_dotenv
import os

from resource_group import create_resource_group

load_dotenv()

subscription_id = os.environ["AZURE_SUBSCRIPTION_ID"]
RESOURCE_GROUP_NAME = os.environ["AZURE_RESOURCE_GROUP_NAME"]
LOCATION = os.environ["LOCATION"]


def main():
    print("Starting infrastructure setup...")

    rg = create_resource_group(subscription_id, RESOURCE_GROUP_NAME, LOCATION)
    print(f"Resource Group '{rg.name}' created in location '{rg.location}'")

if __name__ == "__main__":
    main()