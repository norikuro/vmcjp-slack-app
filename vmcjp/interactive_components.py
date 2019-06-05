import json
import ast
import os
import logging
from urlparse import parse_qs
#from urllib import unquote

EXPECTED_TOKEN = os.environ["token"]

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def command_handler(params):
    callback_id = params["callback_id"]
    response = params["actions"][0]["name"]
    user = params["user"]["name"]

    if callback_id == "create_sddc":
        if response == "yes":
            return {"text": "creating sddc"}
        elif response == "no":
            return {"text": "how many hosts do you want to deploy?"}
    else:
        return {"callback_id": callback_id, "response": response, "user": user}

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
    token = params["token"]
    if not is_token_valid(params):
        return
    return command_handler(params)
#    return event["params"]