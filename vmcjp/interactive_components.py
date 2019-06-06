import json
import ast
import os
import logging
import boto3
from urlparse import parse_qs

EXPECTED_TOKEN = os.environ["token"]

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
    callback_id = params["callback_id"]
    response = params["actions"][0]["name"]
    user = params["user"]["name"]
    response_url = params["response_url"]
    channel_id = params["channel"]["id"]

    if callback_id == "create_sddc":
        if response == "yes":
            return {"text": "creating sddc"}
        elif response == "no":
            return {"text": "how many hosts do you want to deploy?"}
    elif callback_id == "restore_sddc":
        if response == "yes":
            data = {
                "response_url": response_url,
                "channel_id": channel_id
            }
            call_lambda("check-resources", data)
#            call_lambda("restore_sddc", data)
            return {"text": "checking current resoures..."}
        elif response == "no":
            return {"text": "OK, canceled restoring sddc."}
    else:
        return {"text": "other response"}

def is_token_valid(params):
    if "token" in params:
        if params["token"] == EXPECTED_TOKEN:
            return True
    else:
        logger.error("Request token (%s) does not match expected", params["token"])
        return False

def lambda_handler(event, context):
    body = event["body-json"]
    params = json.loads(parse_qs(body)["payload"][0])
    
#    logging.info(params)
    
    token = params["token"]
    if not is_token_valid(params):
        return
    return command_handler(params)
