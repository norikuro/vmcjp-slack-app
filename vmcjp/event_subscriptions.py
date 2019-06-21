import json
import os
import logging
#import urllib2
#from urlparse import parse_qs
from vmcjp.utils.slack_post import post

EXPECTED_TOKEN = os.environ["token"]
#BOT_OAUTH_TOKEN = os.environ["bot_token"]
BOT_USER = os.environ["bot_user"]

url = "https://slack.com/api/chat.postMessage"

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def do_something(event):
    return "hello!"
#    return event

    
def event_handler(event):
    data = {
        "token": event["token"],
        "channel": event["event"]["channel"]
    }
    
#    if not "thread_ts" in event["event"] and "ts" in event["event"]:
#        data["thread_ts"] = event["event"]["ts"]
#    elif "thread_ts" in event["event"]:
#        data["thread_ts"] = event["event"]["thread_ts"]
    
#    data["text"] = do_something(event)
    data["text"] = event
    response = post(url, data)
    logging.info(response.read())
        
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
        if event["event"]["type"] == "app_mention":
            if BOT_USER in event["event"]["text"] and not BOT_USER in event["event"]["user"]:
                return True
        elif event["event"]["type"] == "message":
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
    return
