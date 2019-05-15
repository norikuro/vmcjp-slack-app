import json
import boto3

def write_json_to_s3(bucket, key, dictionary):
  s3obj = boto3.resource('s3').Object(bucket, key)
  s3obj.put(Body=json.dumps(dictionary, indent=2))

def read_json_from_s3(bucket, key):
  return json.loads(boto3.resource('s3').Object(bucket, key).get()['Body'].read())
