#!/usr/bin/env python

from vmcutils.s3 import write_json_to_s3, read_json_from_s3

def get_config(filename):
  f = load_json(s3config_file)
  t = read_json_from_s3(f["bucket"], f["token"])
  j = read_json_from_s3(f["bucket"], f["config"])
  
  return {"token": f["token"], "org_id": j["org"]["id"], "sddc_id": j["sddc"]["id"]}
