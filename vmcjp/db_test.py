#!/usr/bin/env python

import pymongo
import sys

from vmcjp.utils import dbutils

class Test(object):
  def db(self):
    db = dbutils.DocmentDb("vmcjp/s3config.json", "sddc_db", "sddc_collection")
#    collection = db.get_collection()
#    collection.remove()
#    col = db.find_all()
#    for data in col:
#      print(data)
    print(db.find_one({}, {"sddc": 1}))
  
def main():
  test = Test()
  test.db()

if __name__ == '__main__':
  main()
