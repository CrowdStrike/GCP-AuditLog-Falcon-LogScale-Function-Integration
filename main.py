"""CrowdStrike LogScale GCP integration.

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |                         |::.. . | LogScale GCP integration
`-------'                         `-------'

This code is an example for pub / sub setup.

11.28.22 - @@ihaque55
"""
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


