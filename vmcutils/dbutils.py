#!/usr/bin/env python

import json
import pymongo
import sys
#import boto3

from vmcutils import s3utils

class db(object):
  def __init__(self):
    s3 = s3utils.s3()
    
    f = json.load(open("s3config.json", 'r'))
    url = s3.read_json_from_s3(f["bucket"], f["db"])["url"]
    s3.download_from_s3(f["bucket"], "rds-combined-ca-bundle.pem", "/tmp/rds-combined-ca-bundle.pem")
    
    self.client = pymongo.MongoClient(url + "?ssl=true&ssl_ca_certs=/tmp/rds-combined-ca-bundle.pem&replicaSet=rs0")
    self.db = self.client.sddc_db
    self.collection = self.db.sddc_collection
    
  def get_client(self):
    return self.client
  
  def get_db(self):
    return self.db
  
  def get_collection(self):
    return self.collection
  
  def upsert(query, update_data):
    self.collection.update(query, update_data, true)
