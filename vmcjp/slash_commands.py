import json
import os
import logging

from urlparse import parse_qs
from vmcjp.utils.lambdautils import call_lambda

EXPECTED_TOKEN = os.environ["token"]

command_massage = "'/vmcjp' is tool to manage SDDCs of VMC Japan. Please type '/vmcjp help' to see in detail"
help_message = "help message here.."

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def command_handler(params):
    user = params["user_name"][0]
    user_id = params["user_id"][0]
    response_url = params["response_url"][0]
    channel_id = params["channel_id"][0]
    
    if params.has_key("text"):
        command = params["text"][0]
    else:
        return command_massage
        
    if "help" in command:
        return {"text": help_message}
    elif "create sddc" in command:
        return {"text": "Creating sddc"}
    elif "restore sddc" in command:
        data = {
            "user": user,
            "user_id": user_id,
            "response_url": response_url,
            "channel_id": channel_id
        }
        call_lambda("restore_sddc", data)
        return {
        "text": "OK, restore from backed up configration."
        }
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
        return {"statusCode": 400}
    
    return command_handler(params)
