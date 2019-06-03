#!/usr/bin/env python

import pymongo
import sys

from vmcjp.utils import dbutils

class Test(object):
  def db(self):
    db = dbutils.DocmentDb("vmcjp/s3config.json", "sddc_db", "sddc_collection")
    collection = db.get_collection()
#    col = collection.aggregate([{"$project": {"sddc.name": 1}}])
#    collection.remove()
    col = db.find({}, {"sddc.name": 1, "sddc.region": 1, "_id" :0})
#    col = db.find_one({"sddc.name": {"$exists": True}})
#    print(col)
#    col = db.find_all()
    for data in col:
      print(data)
  
def main():
  test = Test()
  test.db()

if __name__ == '__main__':
  main()
