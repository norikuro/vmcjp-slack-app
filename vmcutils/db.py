#!/usr/bin/env python

import pymongo
import sys
#import boto3
#import json

def get_collection():
  f = load_json(s3config)
  url = read_json_from_s3(f["bucket"], "db_config.json")["url"]
  download_from_s3("rds-combined-ca-bundle.pem", "/tmp")
  client = pymongo.MongoClient(url + "?ssl=true&ssl_ca_certs=/tmp/rds-combined-ca-bundle.pem&replicaSet=rs0")
  db = client.sddc_db
  return db.sddc_collection
  
#def insert(data):
