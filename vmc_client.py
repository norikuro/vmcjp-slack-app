#!/usr/bin/env python

from vmware.vapi.vmc.client import create_vmc_client
from vmcutils.fileutils import load_json
from vmcutils.s3 import read_json_from_s3

def get_sddc(s3config_file):
  f = load_json(s3config_file)
  t = read_json_from_s3(f["bucket"], f["token"])
  j = read_json_from_s3(f["bucket"], f["config"])
  
  refresh_token = t["token"]
#  org_id = j["org"]["id"]
#  sddc_id = j["sddc"]["id"]
  
  return create_vmc_client(refresh_token)
