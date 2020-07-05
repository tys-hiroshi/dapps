from datetime import datetime, timedelta
from azure.storage.blob import BlobServiceClient, generate_account_sas, ResourceTypes, AccountSasPermissions, ContainerClient, BlobClient
import asyncio
import os
import uuid

async def task_make_container(connection_string, container_name):
    container_client = ContainerClient.from_connection_string(conn_str=connection_string, container_name=container_name)
    await container_client.create_container()
    return True

async def make_container(loop, connection_string, container_name):
    await loop.create_task(task_make_container(connection_string, container_name))
    #await task_make_container(connection_string, container_name)
    return True


if __name__ == "__main__":
    try:
        loop = asyncio.get_event_loop()
        container_name = "containertest04"
        connection_string = "DefaultEndpointsProtocol=https;AccountName=bnodestr;AccountKey=qeuflf0W18D9zSGCUIDoTJ1uK6V58ZlVbiozurnnqHe8088jDyqmLJtPTREWEB1/35bGRkT5S5VCok5nfTFPfg==;EndpointSuffix=core.windows.net"
        #loop.run_until_complete(make_container(loop, connection_string, container_name))
        # Create a file in local data directory to upload and download
        local_path = "./upload"
        local_file_name = "quickstart" + str(uuid.uuid4()) + ".txt"
        upload_file_path = os.path.join(local_path, local_file_name)

        # Write text to the file
        file = open(upload_file_path, 'w')
        file.write("Hello, World!")
        file.close()

        # # sas_token = generate_account_sas(
        # #     account_name="bnodestr",
        # #     account_key="qeuflf0W18D9zSGCUIDoTJ1uK6V58ZlVbiozurnnqHe8088jDyqmLJtPTREWEB1/35bGRkT5S5VCok5nfTFPfg==",
        # #     resource_types=ResourceTypes(service=True),
        # #     permission=AccountSasPermissions(read=True),
        # #     expiry=datetime.utcnow() + timedelta(hours=1)
        # # )

        # # blob_service_client = BlobServiceClient(account_url="https://bnodestr.blob.core.windows.net", credential=sas_token)

        # Create the BlobServiceClient object which will be used to create a container client
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        # Create a blob client using the local file name as the name for the blob
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file_name)

        print("\nUploading to Azure Storage as blob:\n\t" + local_file_name)

        # Upload the created file
        with open(upload_file_path, "rb") as data:
            blob_client.upload_blob(data)

        
    finally:
        #loop.close()
        print("aaaa")


#loop.create_task(make_container(connection_string, container_name))

# blob = BlobClient.from_connection_string(conn_str="<connection_string>", container_name="my_container", blob_name="my_blob")

# with open("./SampleSource.txt", "rb") as data:
#     await blob.upload_blob(data)


