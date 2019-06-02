#!/usr/bin/env python

import pymongo
import sys

import vmcjptool.vmcutils.dbutils

class Test(object):
  def db(self):
    db = DocmentDb("vmcjptool/s3config.json")
#    collection.remove()
    col = db.find_all()
    for data in col:
      print(data)
  
def main():
  test = Test()
  test.db()

if __name__ == '__main__':
  main()
