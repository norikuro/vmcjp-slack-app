import json
import os
#import logging

from urlparse import parse_qs
from vmcjp.utils import constant
from vmcjp.utils.s3utils import read_json_from_s3
from vmcjp.utils.lambdautils import call_lambda_async

EXPECTED_TOKEN = os.environ["token"]

#logger = logging.getLogger()
#logger.setLevel(logging.INFO)

def set_data_and_call_lambda(params):
    f = json.load(open(constant.S3_CONFIG, 'r'))
    j = read_json_from_s3(f["bucket"], f["config"])
    
    data = {
        "slack_token": params["token"],
        "channel": params["channel"]["id"],
        "user_id": params["user"]["id"],
        "db_url": j.get("db_url"),
        "bot_token": j.get("bot_token"),
        "aws_internal_account": os.environ["aws_account"], #for internal use
        "aws_internal_id": os.environ["aws_id"], #for internal use
        "cloudwatch_account": j.get("cloudwatch_account"), #for internal use
        "callback_id": params["callback_id"],
        "response_url": params["response_url"],
        "response": params["actions"][0]["value"]
        if 
        params["actions"][0].has_key("value") 
        else 
        params["actions"][0]["selected_options"][0]["value"]
    }
#    call_lambda("slack_session", data)
    call_lambda_async("slack_interactive", data)
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

def is_retry_request(headers):
    if "X-Slack-Retry-Reason" in headers:
        return True
    else:
        return False

def lambda_handler(event, context):
#    logging.info(params)
    headers = event.get("headers")
    
    if is_retry_request(headers):
        return format_response(200, None)
    
    params = json.loads(
        parse_qs(event.get("body"))["payload"][0]
    )
    
    token = params.get("token")
    if not is_token_valid(params):
        return format_response(
            200, 
            "token is invalid"
        )
    
    return set_data_and_call_lambda(params)
