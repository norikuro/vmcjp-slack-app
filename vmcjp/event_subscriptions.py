import json
import os
#import logging

from vmcjp.utils.lambdautils import call_lambda

EXPECTED_TOKEN = os.environ["token"]

#logger = logging.getLogger()
#logger.setLevel(logging.INFO)

def is_token_valid(event):
    if "token" in event:
        if EXPECTED_TOKEN in event.get("token"):
            return True
    logger.error("Request token (%s) does not match expected", event.get("token"))
    return False

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

def check_event(event):
    # We only support Direct Message to Slack App currently.
    if "event_callback" in event.get("type"):
        if "message" in event.get("event").get("type") and "im" in event.get("event").get("channel_type"):
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

def is_retry_request(headers):
    if "X-Slack-Retry-Reason" in headers:
        return True
    else:
        return False

def lambda_handler(event, context):
#    logging.info(event)
    headers = event.get("headers")
    if is_retry_request(headers):
        return format_response(200, None)
    
    params = json.loads(event.get("body"))
    
    if not is_token_valid(params):
        return format_response(
            200, 
            "token is invalid"
        )
    
    if "challenge" in params:
        return {"challenge": params.get("challenge")}
    
    if check_event(params):
#        logging.info(params)
        data = {
            "slack_token": params["token"],
            "channel": params["event"]["channel"],
            "text": params["event"]["text"],
            "user_id": params["event"]["user"]
        }
        call_lambda("slack_session", data)
        return format_response(200, None)
    
    return format_response(200, None)
