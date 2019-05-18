#!/usr/bin/env python

from vmcutils.fileutils import load_json

def get_vmc_client():
  f = load_json("s3config.json")
  t = read_json_from_s3(f["bucket"], f["token"])
  j = read_json_from_s3(f["bucket"], f["config"])
  
  refresh_token = t["token"]
#  org_id = j["org"]["id"]
#  sddc_id = j["sddc"]["id"]
  
  return create_vmc_client(refresh_token)
