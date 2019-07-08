import json
import os
import logging

from urlparse import parse_qs
from vmcjp.utils.lambdautils import call_lambda

EXPECTED_TOKEN = os.environ["token"]
BOT_OAUTH_TOKEN = os.environ["bot_token"]
#BOT_USER = os.environ["bot_user"]
POST_URL = "https://slack.com/api/chat.postMessage"

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def is_token_valid(event):
    if "token" in event:
        if event.get("token") == EXPECTED_TOKEN:
            return True
        logger.error("Request token (%s) does not match expected", event.get("token"))
        return False

def check_event(event):
    # We only support Direct Message to Slack App currently.
    if event.get("type") == "event_callback":
        if event.get("event").get("type") == "message" and event.get("event").get("channel_type") == "im":
            return check_user(event)
    else:
        return False

def check_user(event):
    if event["event"].has_key("subtype"):
        if "bot_message" in event.get("event").get("subtype"):
            return False
        elif "message_changed" in event.get("event").get("subtype"):
            return False
        else:
            return True
    return True

def lambda_handler(event, context):
    params = event.get("body")
    logging.info(params)

    if not is_token_valid(params):
        return
#    if "challenge" in event:
#        return {"challenge": event.get("challenge")}
#    if check_event(event):
##        logging.info(event)
#        data = {
#            "slack_token": event["token"],
#            "channel": event["event"]["channel"],
#            "text": event["event"]["text"],
#            "user_id": event["event"]["user"],
#            "bot_token" :BOT_OAUTH_TOKEN,
##            "response_url": POST_URL,
#            "post_url": POST_URL
#        }
#        call_lambda("slack_session", data)
#        return {"statusCode": 200}
    return {"statusCode": 200}
