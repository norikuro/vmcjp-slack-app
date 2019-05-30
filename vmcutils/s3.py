#!/usr/bin/env python

import json
import boto3

class s3utils(object):
    def __init__(self):
        self.s3 = boto3.resource('s3')
    
    def get_s3(self):
        return self.s3
    
    def write_json_to_s3(self, bucket, key, dictionary):
        s3obj = self.s3.Object(bucket, key)
        s3obj.put(Body=json.dumps(dictionary, indent=2))
        
    def read_json_from_s3(self, bucket, key):
        return json.loads(self.s3.Object(bucket, key).get()['Body'].read())
    
    def download_from_s3(self, bucket, key, target):
        bucket = self.s3.Bucket(bucket)
        bucket.download_file(key, target)
