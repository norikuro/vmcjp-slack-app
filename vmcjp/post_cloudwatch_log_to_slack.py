import json
import os
import logging
import urllib
import gzip
import base64

logger = logging.getLogger()
logger.setLevel(logging.INFO)

WEBHOOK_URL = os.environ["webhook_url"]

def post_log(text):
    url = WEBHOOK_URL

    headers = {
        "Content-Type": "application/json"
    }
    data = {
            "text": text
    }
    request = urllib.request.Request(
        url, 
        data=json.dumps(data).encode("utf-8"), 
        method="POST",
        headers=headers
    )
    
    response = urllib.request.urlopen(request)
#    response = post(url, data)
#    logging.info(response.read())

# Python 3.6 runtime is needed.
def lambda_handler(event, context):
    logdata = json.dumps(event["awslogs"]["data"])
    f = base64.b64decode(logdata)
    payload=json.loads(gzip.decompress(f))
    for logevent in payload["logEvents"]:
        if "INFO" in logevent["message"]:
            str = logevent["message"]
            logging.info("!!!: " + str)
            if "RuntimeWarning: Parent module" not in str and "Found credentials in environment variables" not in str:
                logging.info("!! aaaaa")
                i = logevent["message"].find("{")
                text = "logGroup: "+ payload["logGroup"] + ",  " + "message: " + str[:i] + ",  " + str[i:]
                post_log(text)
        elif "error" in logevent["message"]:
            str = logevent["message"]
            post_log(str)
#    logging.info(event)
#    post_log(payload)
