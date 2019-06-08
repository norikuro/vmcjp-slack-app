#!/usr/bin/env python

import json
import pymongo
#import sys
#import boto3

from vmcjp.utils import s3utils

class DocmentDb(object):
  CA_BUMDLE = "rds-combined-ca-bundle.pem"
  DOWNLOAD_TARGET = "/tmp/" + CA_BUMDLE
  
  def __init__(self, s3config, db_name, collection_name):
    s3 = s3utils.S3()
    
    f = json.load(open(s3config, 'r'))
    url = s3.read_json_from_s3(f["bucket"], f["config"])["db_url"]
    s3.download_from_s3(f["bucket"], DocmentDb.CA_BUMDLE, DocmentDb.DOWNLOAD_TARGET)
    
    self.client = pymongo.MongoClient(url + "?ssl=true&ssl_ca_certs=" + DocmentDb.DOWNLOAD_TARGET + "&replicaSet=rs0")
    self.db = self.client[db_name]
    self.collection = self.db[collection_name]
    
  def get_client(self):
    return self.client
  
  def get_db(self):
    return self.db
  
  def get_collection(self):
    return self.collection
  
  def upsert(self, query, update_data):
    self.collection.update(query, update_data, upsert=True)

  def find_with_fields(self, query, fields):
    return self.collection.find(query, fields)[0]
