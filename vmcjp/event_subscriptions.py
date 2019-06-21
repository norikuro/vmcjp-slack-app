import json
import os
import logging

from vmcjp.utils.slack_post import post

EXPECTED_TOKEN = os.environ["token"]
BOT_OAUTH_TOKEN = os.environ["bot_token"]
BOT_USER = os.environ["bot_user"]

url = "https://slack.com/api/chat.postMessage"

logger = logging.getLogger()
logger.setLevel(logging.INFO)
    
def event_handler(event):
    text = event["event"]["text"]
    data = {
        "token": event["token"],
        "channel": event["event"]["channel"]
    }
    
    if "create sddc" in text:
        data["text"] = "OK, starting create sddc wizard."
    else:
        data["text"] = event
    response = post(url, data, BOT_OAUTH_TOKEN)
#    logging.info(response.read())
        
def is_token_valid(event):
    if "token" in event:
        if event["token"] == EXPECTED_TOKEN:
            return True
        logger.error("Request token (%s) does not match expected", event["token"])
        return False

def check_event(event):
    if event["event"]["type"] == "message":
        return check_user(event)
    elif event["event"]["type"] == "app_mention":
        return check_user(event)
    else:
        return False

def check_user(event):
    if "user" in event["event"]:
        if event["event"]["channel_type"] == "im":
            if not BOT_USER in event["event"]["user"]:
                return True
    return False


def lambda_handler(event, context):
#    logging.info(event)

    if not is_token_valid(event):
        return
    if "challenge" in event:
        return {"challenge": event["challenge"]}
    if check_event(event):
        event_handler(event)
        return "ok"
