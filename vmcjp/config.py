#!/usr/bin/env python

import json

from datetime import datetime
from pytz import timezone
from vmcjp.utils import s3utils
from vmcjp.utils import dbutils

class Config(object):
    DB_NAME = "sddc_db"
    COLLECTION_NAME = "sddc_collection"
    
    def __init__(self, config):
      s3 = s3utils.S3()
      f = json.load(open(config, "r"))
      j = s3.read_json_from_s3(f["bucket"], f["config"])
      self.token = j["token"]
      self.org_id = j["org_id"]
      self.sddc_id = j["sddc_id"]
      
      now = datetime.now(timezone("Asia/Tokyo")).strftime("%Y/%m/%d")
      
      self.db = dbutils.DocmentDb(config, Config.DB_NAME, Config.COLLECTION_NAME)
 
