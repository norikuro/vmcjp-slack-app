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
    response = params["actions"][0]["name"]
    
    if callback_id == "create_sddc":
        if response == "yes":
            data = {
                "callback_id": callback_id,
                "token": params["token"],
                "channel": params["channel"]["id"],
                "user_id": params["user"]["id"],
                "bot_token" :BOT_OAUTH_TOKEN,
                "response_url": url
            }
#            call_lambda("slack_session", data)
#            return {"text": "OK, starting create sddc wizard."}
            return {"statusCode": 200}
        elif response == "no":
            return {"text": "OK, create SDDC has cenceled."}
    elif callback_id == "restore_sddc":
        if response == "yes":
            data = {
                "user": params["user"]["name"],
                "user_id": params["user"]["id"],
                "response_url": params["response_url"],
                "channel_id": params["channel"]["id"]
            }
            call_lambda("check_resources", data)
            return {"text": "Checking current resoures..."}
        elif response == "no":
            return {"text": "OK, restoring sddc is canceled."}
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
#    body = event["body-json"]
#    params = json.loads(parse_qs(body)["payload"][0])
#    query = parse_qs(event.get["body"] or "")
#    logging.info(params)
    a = json.dumps(event)
    aa = json.loads(a)
    logging.info(aa.get["body"])
    
#    token = params["token"]
#    if not is_token_valid(params):
#        return
#    return command_handler(params)
