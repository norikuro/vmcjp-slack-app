#!/usr/bin/env python

import pymongo
import sys

class Test(object):
  def db(self):
    client = pymongo.MongoClient('mongodb://master:VMware1!@docdb-2019-05-30-00-09-16.cluster-cmtpcwnhqpq9.ap-northeast-1.docdb.amazonaws.com:27017/?ssl=true&ssl_ca_certs=/home/ec2-user/docdb-test/rds-combined-ca-bundle.pem&replicaSet=rs0')
    db = client.sddc_db
    collection = db.sddc_collection
#    print(collection.find_one({"sddc": {"$exists":True}}))
#    collection.remove()
    col = collection.find()
    for data in col:
      print(data)
  
def main():
  test = Test()
  test.db()

if __name__ == '__main__':
  main()
