import json
import os
import logging
import ipaddress

from vmcjp.utils.slack_post import post
from vmcjp.utils.lambdautils import call_lambda

EXPECTED_TOKEN = os.environ["token"]
BOT_OAUTH_TOKEN = os.environ["bot_token"]
#BOT_USER = os.environ["bot_user"]

url = "https://slack.com/api/chat.postMessage"

logger = logging.getLogger()
logger.setLevel(logging.INFO)
    
def event_handler(event):
    text = event["event"]["text"]
    data = {
        "token": event["token"],
        "channel": event["event"]["channel"]
    }
    le = {"user": event["event"]["user"]}
    le.update(data)
    
    if "create sddc" in text:
        data["text"] = "OK, starting create sddc wizard."
        response = post(url, data, BOT_OAUTH_TOKEN)
        data["text"] = "This conversation will end with typing `cancel` or doing nothing within 5 minutes"
        response = post(url, data, BOT_OAUTH_TOKEN)
        data["text"] = "Please enter SDDC name"
        response = post(url, data, BOT_OAUTH_TOKEN)
        le.update({"event_type": "sddc_name"})
        call_lambda("slack_session", le)
    elif "cancel" in text:
        data["text"] = "OK, create SDDC has cenceled."
        response = post(url, data, BOT_OAUTH_TOKEN)
        le.update({"event_type": "cancel"})
        call_lambda("slack_session", le)
    elif text.find(" ") != -1:
        data["text"] = event
        response = post(url, data, BOT_OAUTH_TOKEN)
    elif is_valid_network(text):
        data["text"] = text
        response = post(url, data, BOT_OAUTH_TOKEN)
    else:
        data["text"] = "Single host or Multi host?"
        response = post(url, data, BOT_OAUTH_TOKEN)
        call_lambda("slack_session", le)
#    logging.info(response.read())

def is_valid_network(address):
    try:
        ipaddress.ip_network(address)
        return True
    except ValueError:
        return False

def is_token_valid(event):
    if "token" in event:
        if event["token"] == EXPECTED_TOKEN:
            return True
        logger.error("Request token (%s) does not match expected", event["token"])
        return False

def check_event(event):
    if event["event"]["type"] == "message" and event["event"]["channel_type"] == "im":
        return check_user(event)
    else:
        return False

def check_user(event):
    if event["event"].has_key("subtype"):
        if "bot_message" in event["event"]["subtype"]:
            return False
    return True


def lambda_handler(event, context):
#    logging.info(event)

    if not is_token_valid(event):
        return
    if "challenge" in event:
        return {"challenge": event["challenge"]}
    if check_event(event) == True:
        event_handler(event)
        return "ok"
    return "ok"
