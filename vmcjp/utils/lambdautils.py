import json
import boto3

def call_lambda(function, data):
    clientLambda = boto3.client("lambda")
    clientLambda.invoke(
        FunctionName=function,
        InvocationType="Event",
        Payload=json.dumps(data)
    )
