from datetime import datetime, timedelta
from azure.storage.blob import BlobServiceClient, generate_account_sas, ResourceTypes, AccountSasPermissions, ContainerClient, BlobClient
import asyncio
import os
import uuid

def is_exist_container(connectStr, containerName):
    container = ContainerClient.from_connection_string(connectStr, containerName)
    try:
        container_properties = container.get_container_properties()
        # Container foo exists. You can now use it.
        return True
    except Exception as e:
        # Container foo does not exist. You can now create it.
        print(e)
        return False

def make_container(connectStr, containerName):
    try:
        container_client = ContainerClient.from_connection_string(conn_str=connectStr, container_name=containerName)
        container_client.create_container()
        return True
    except Exception as e:
        # Container foo does not exist. You can now create it.
        print(e)
        return False

def make_container_retry(connectStr, containerName, maxRetryCount = 5):
    retryCount = 0
    while retryCount < maxRetryCount:
        retryCount += 1
        if not is_exist_container(connectStr, containerName):
            isSuccess = make_container(connectStr, containerName)
            if isSuccess:
                break

async def async_task_make_container(connectStr, containerName):
    container_client = ContainerClient.from_connection_string(conn_str=connectStr, container_name=containerName)
    await container_client.create_container()
    return True

async def async_make_container(loop, connectStr, containerName):
    await loop.create_task(async_task_make_container(connectStr, containerName))
    #await task_make_container(connection_string, container_name)
    return True

from utils.Config import Config

configFile = "app_config.yml"
config = Config(configFile).content
ACCOUNT_NAME = config['API_CONFIG']['AZURE_INFO']['ACCOUNT_NAME']
ACCOUNT_KEY = config['API_CONFIG']['AZURE_INFO']['ACCOUNT_KEY']
CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName={};AccountKey={};EndpointSuffix=core.windows.net".format(ACCOUNT_NAME, ACCOUNT_KEY)

if __name__ == "__main__":
    try:
        loop = asyncio.get_event_loop()
        containerName = "containertest"
        make_container_retry(CONNECTION_STRING, containerName)
        # Create a file in local data directory to upload and download
        local_path = "./upload"
        #local_file_name = "quickstart" + str(uuid.uuid4()) + ".txt"
        local_file_name = "quickstart.txt"
        upload_file_path = os.path.join(local_path, local_file_name)

        # Write text to the file
        file = open(upload_file_path, 'w')
        file.write("Hello, World!")
        file.close()

        # Create the BlobServiceClient object which will be used to create a container client
        blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)
        # Create a blob client using the local file name as the name for the blob
        blob_client = blob_service_client.get_blob_client(container=containerName, blob=local_file_name)

        print("\nUploading to Azure Storage as blob:\n\t" + local_file_name)

        # Upload the created file
        with open(upload_file_path, "rb") as data:
            blob_client.upload_blob(data)

    except Exception as e:
        print(e)
        
    finally:
        #loop.close()
        print("final")

