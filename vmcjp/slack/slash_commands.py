import json
import os
import logging
import boto3

from urlparse import parse_qs

EXPECTED_TOKEN = os.environ["token"]

success = {
    "statusCode": 200,
    "body": "OK"
}

command_massage = "'/vmcjp' is tool to manage SDDCs of VMC Japan. Please type '/vmcjp help' to see in detail"
help_message = "help message here.."

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def call_lambda(function, data):
    clientLambda = boto3.client("lambda")
    clientLambda.invoke(
        FunctionName=function,
        InvocationType="Event",
        Payload=json.dumps(data)
    )

def command_handler(params):

    if params.has_key("text"):
        command = params["text"][0]
    else:
        return command_massage
        
    if "help" in command:
        return {"text": help_message}
    elif "create sddc" in command:
        return "creating sddc"
    elif "restore sddc" in command:
        data = {
            "response_url": params["response_url"][0],
            "channel_id": params["channel_id"][0]
        }
        call_lambda("restore_sddc", data)
        return {
        'text': "OK, restore from backed up configration."
        }
#        return
    else:
        return command_massage

def is_token_valid(params):
    if params.has_key("token") and params["token"][0] == EXPECTED_TOKEN:
        return True
    else:
        logger.error("Request token (%s) does not match expected", params["token"][0])
        return False

def lambda_handler(event, context):
#    logging.info(event)

    body = event["body-json"]
    params = parse_qs(body)

#    logging.info(params)

    if not is_token_valid(params):
        return {'statusCode': 400}
    
    return command_handler(params)
    
#    return {
#        'statusCode': 200,
#        'body': json.dumps('Hello from Lambda!')
#    }
