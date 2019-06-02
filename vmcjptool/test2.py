#!/usr/bin/env python

import pymongo
import sys

from vmcjptool.utils import dbutils

class Test(object):
  def db(self):
    db = dbutils.DocmentDb("vmcjptool/s3config.json", "sddc_db", "sddc_collection")
#    collection.remove()
    col = db.find_all()
    for data in col:
      print(data)
  
def main():
  test = Test()
  test.db()

if __name__ == '__main__':
  main()
