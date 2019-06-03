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
    
#    s3 = boto3.resource('s3')
#    org = json.loads(s3.Object("vmc-env", "test_config.json").get()['Body'].read())
#    sddc = json.loads(s3.Object("vmc-env", "sddc.json").get()['Body'].read())
#    network = json.loads(s3.Object("vmc-env", "network.json").get()['Body'].read())
    
    config = {
        "updated": sddc["updated"],
        "org_id": org["org_id"],
        "region": sddc["sddc"]["region"],
#        "sddc_name": sddc["sddc"]["name"],
        "sddc_name": "nk_single_api_test", #for test
        "sddc_id": sddc["sddc"]["id"],
        "aws_account_id": network["customer_vpc"]["linked_account"],
#       "customer_subnet_id": network["customer_vpc"]["linked_vpc_subnets_id"],
        "customer_subnet_id": "subnet-4c80da05", #fortest
#       "provider": os.environ.get('VMC_PROVIDER', SddcConfig.PROVIDER_AWS),
        "provider": os.environ.get('VMC_PROVIDER', "ZEROCLOUD"), #for test
#       "num_hosts": sddc["sddc"]["num_hosts"]
        "num_hosts": 3 #for test
    }    

    return config
#    return "test data"

def create_button(config):
    button_set = json.load(open("button.json", 'r'))
    
    fields = []
    fields.append(
        {
            "title": "Updated date",
            "value": config["updated"],
            "short": "true"
        }
    )
    fields.append(
        {
            "title": "Org ID",
            "value": config["org_id"],
            "short": "true"
        }
    )
    fields.append(
        {
            "title": "SDDC name",
            "value": config["sddc_name"],
            "short": "true"
            }
        )
    fields.append(
        {
            "title": "Number of hosts",
            "value": config["num_hosts"],
            "short": "true"
        }
    )
    fields.append(
        {
            "title": "AWS account",
            "value": config["aws_account_id"],
            "short": "true"
        }
    )
    fields.append(
        {
            "title": "Region",
            "value": config["region"],
            "short": "true"
        }
    )

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
    
    logging.info(response.read())
  
#    return {
#        'statusCode': 200,
#        'body': json.dumps('Hello from Lambda!')
#    }
