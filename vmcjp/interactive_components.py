import json
import os
import logging

from urlparse import parse_qs
from vmcjp.utils.lambdautils import call_lambda

#EXPECTED_TOKEN = os.environ["token"]
EXPECTED_TOKEN = os.environ["token2"] #for test
BOT_OAUTH_TOKEN = os.environ["bot_token"]

url = "https://slack.com/api/chat.postMessage"

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def command_handler(params):
    callback_id = params["callback_id"]
    
    if callback_id == "restore_sddc":
        if response == "yes":
            data = {
                "user": params["user"]["name"],
                "user_id": params["user"]["id"],
                "response_url": params["response_url"],
                "channel_id": params["channel"]["id"]
            }
            call_lambda("check_resources", data)
            return format_response(
                200,
                "Checking current resoures..."
            )
        elif response == "no":
            return format_response(
                200,
                "OK, restoring sddc is canceled."
            )
    else:
        data = {
            "callback_id": params["callback_id"],
            "token": params["token"],
            "channel": params["channel"]["id"],
            "user_id": params["user"]["id"],
            "bot_token" :BOT_OAUTH_TOKEN,
            "response_url": params["response_url"],
            "response": params["actions"][0]["value"] 
            if 
            params["actions"][0].has_key("value") 
            else 
            params["actions"][0]["selected_options"][0]["value"]
        }
        call_lambda("slack_session", data)
        return format_response(200, None)

def format_response(status, text):
    if text is None:
        return {
        "statusCode": status,
        "body": ""
        }
    else:
        return {
            "statusCode": status,
            "body": json.dumps(
                {"text": text}
            )
        }

def is_token_valid(params):
    if "token" in params:
        if params["token"] == EXPECTED_TOKEN:
            return True
    else:
        logger.error("Request token (%s) does not match expected", params["token"])
        return False

def lambda_handler(event, context):
#    body = event["body-json"]
    params = json.loads(
        parse_qs(event.get("body"))["payload"][0]
    )
#    logging.info(params)
    
    token = params.get("token")
    if not is_token_valid(params):
        return format_response(
            200, 
            "token is invalid"
        )
    
    return command_handler(params)
