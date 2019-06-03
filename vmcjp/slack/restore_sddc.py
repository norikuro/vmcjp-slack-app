import json
import os
import logging
import boto3

from vmcjp.utils.slack_post import post_to_response_url
from vmcjp.utils import dbutils

logger = logging.getLogger()
logger.setLevel(logging.INFO)

DB_NAME = "sddc_db"
COLLECTION_NAME = "sddc_collection"
S3_CONFIG = "vmcjp/s3config.json"

def restore_sddc():
    db = dbutils.DocmentDb(S3_CONFIG, DB_NAME, COLLECTION_NAME)
    return db.find_with_fields(
      {}, 
      {
        "sddc_updated": 1,
        "sddc.name": 1, 
        "sddc.region": 1, 
        "sddc.num_hosts": 1, 
        "org.display_name": 1,
        "customer_vpc.linked_account": 1,
        "customer_vpc.linked_vpc_subnets_id": 1,
        "_id": 0
      }
    )

def create_button(config):
    button_set = json.load(open("vmcjp/slack/button.json", 'r'))
    
    fields = [
        {
            "title": "Backed up date",
            "value": config["sddc_updated"],
            "short": "true"
        },
        {
            "title": "Org Name",
#            "value": config["org"]["display_name"],
            "value": "APJ SME Zero Cloud Org",
            "short": "true"
        },
        {
            "title": "SDDC name",
#            "value": config["sddc"]["name"],
            "value": "nk_single_api_test", #for test
            "short": "true"
        },
        {
            "title": "Number of hosts",
#            "value": config["sddc"]["num_hosts"],
            "value": 3, #for test
            "short": "true"
        },
        {
            "title": "AWS account",
            "value": config["customer_vpc"]["linked_account"],
            "short": "true"
        },
        {
            "title": "AWS linked subnet",
#            "value": config["customer_vpc"]["linked_vpc_subnets_id"],
            "value": "subnet-4c80da05", #fortest,
            "short": "true"
        },
        {
            "title": "Region",
            "value": config["sddc"]["region"],
            "short": "true"
        }
    ]

    button_set["attachments"][0]["fields"] = fields
    logging.info(button_set)
    return button_set
    

def lambda_handler(event, context):
#    logging.info(event)
    
    url = event["response_url"]
    config = restore_sddc()
    button = create_button(config)
    
    response = post_to_response_url(url, button)

#    data = {
#        "channel": event["channel_id"],
#        "text": config
#    }
    
#    response = post_to_response_url(url, data)
    
#    logging.info(response.read())
  
#    return {
#        'statusCode': 200,
#        'body': json.dumps('Hello from Lambda!')
#    }
