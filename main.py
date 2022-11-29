# copy this code to setup the at pub/sub main.py code


import base64
import json
import urllib3

http = urllib3.PoolManager()
dest_url = "https://cloud.community.humio.com/api/v1/ingest/hec/raw"
dest_token1 = <xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx>
header1 = {"Content-Type": "application/json", "Authorization": f"Bearer {dest_token1}"}

def send_data(event, context):
    """Send the event to LogScale."""

    print(f"This function was triggered by messageId {context.event_id} "
          f"published at {context.timestamp} to {context.resource['name']}"
          )
    
    if 'data' in event:

        newevent = base64.b64decode(event['data']).decode('utf-8')
        http.request('POST', dest_url, body=newevent, headers=header1)


