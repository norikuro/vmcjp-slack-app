#!/usr/bin/env python

import pymongo
import sys
#import boto3
#import json

from vmcutils import s3

class db(object):
  def __init__(self):
    s3 = s3()
    
    f = load_json("s3config")
    url = s3.read_json_from_s3(f["bucket"], f["db"])["url"])
    s3.download_from_s3(f["bucket"], "rds-combined-ca-bundle.pem", "/tmp")
    
    self.client = pymongo.MongoClient(url + "?ssl=true&ssl_ca_certs=/tmp/rds-combined-ca-bundle.pem&replicaSet=rs0")
    self.db = self.client.sddc_db
    self.collection = self.db.sddc_collection
    
  def get_client(self):
    return self.client
  
  def get_db(self):
    return self.db
  
  def get_collection(self):
    return self.collection
  
#def insert(data):
