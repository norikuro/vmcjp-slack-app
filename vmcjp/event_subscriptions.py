import json
import os
import logging

from vmcjp.utils.lambdautils import call_lambda

EXPECTED_TOKEN = os.environ["token"]
BOT_OAUTH_TOKEN = os.environ["bot_token"]
#BOT_USER = os.environ["bot_user"]

url = "https://slack.com/api/chat.postMessage"

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def is_token_valid(event):
    if "token" in event:
        if event["token"] == EXPECTED_TOKEN:
            return True
        logger.error("Request token (%s) does not match expected", event["token"])
        return False

def check_event(event):
    # We only support Direct Message to Slack App currently.
    if event["type"] == "event_callback":
        if event["event"]["type"] == "message" and event["event"]["channel_type"] == "im":
            return check_user(event)
    else:
        return False

def check_user(event):
    if event["event"].has_key("subtype"):
        if "bot_message" in event["event"]["subtype"]:
            return False
        elif "message_changed" in event["event"]["subtype"]:
            return False
        else:
            return True
    return True

def lambda_handler(event, context):
    logging.info(event)

    if not is_token_valid(event):
        return
    if "challenge" in event:
        return {"challenge": event["challenge"]}
    if check_event(event):
        logging.info(event)
        data = {
            "token": event["token"],
            "channel": event["event"]["channel"],
            "text": event["event"]["text"],
            "user_id": event["event"]["user"],
            "bot_token" :BOT_OAUTH_TOKEN,
            "response_url": url
        }
        call_lambda("slack_session", data)
        return {"statusCode": 200}
    return {"statusCode": 200}
