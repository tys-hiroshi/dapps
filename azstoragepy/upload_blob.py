from datetime import datetime, timedelta
from azure.storage.blob import BlobServiceClient, generate_account_sas, ResourceTypes, AccountSasPermissions, ContainerClient, BlobClient
import asyncio

sas_token = generate_account_sas(
    account_name="bnodestr",
    account_key="qeuflf0W18D9zSGCUIDoTJ1uK6V58ZlVbiozurnnqHe8088jDyqmLJtPTREWEB1/35bGRkT5S5VCok5nfTFPfg==",
    resource_types=ResourceTypes(service=True),
    permission=AccountSasPermissions(read=True),
    expiry=datetime.utcnow() + timedelta(hours=1)
)

blob_service_client = BlobServiceClient(account_url="https://bnodestr.blob.core.windows.net", credential=sas_token)

async def task_make_container(connection_string, container_name):
    container_client = ContainerClient.from_connection_string(conn_str=connection_string, container_name=container_name)
    await container_client.create_container()

async def make_container(loop, connection_string, container_name):
    task = loop.create_task(task_make_container(connection_string, container_name))
    await task

loop = asyncio.get_event_loop()
try:
    container_name = "containertest04"
    connection_string = "DefaultEndpointsProtocol=https;AccountName=bnodestr;AccountKey=qeuflf0W18D9zSGCUIDoTJ1uK6V58ZlVbiozurnnqHe8088jDyqmLJtPTREWEB1/35bGRkT5S5VCok5nfTFPfg==;EndpointSuffix=core.windows.net"
    loop.run_until_complete(make_container(loop, connection_string, container_name))
finally:
    loop.close()

#loop.create_task(make_container(connection_string, container_name))

# blob = BlobClient.from_connection_string(conn_str="<connection_string>", container_name="my_container", blob_name="my_blob")

# with open("./SampleSource.txt", "rb") as data:
#     await blob.upload_blob(data)


