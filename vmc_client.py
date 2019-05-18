#!/usr/bin/env python

from vmware.vapi.vmc.client import create_vmc_client
from vmcutils.fileutils import load_json
from vmcutils.s3 import read_json_from_s3

def get_sddc(s3config):
  f = load_json(s3config)
  t = read_json_from_s3(f["bucket"], f["token"])
  j = read_json_from_s3(f["bucket"], f["config"])
  
  refresh_token = t["token"]
  org_id = j["org"]["id"]
  sddc_id = j["sddc"]["id"]
  
#  print(refresh_token)
#  print(org_id)
#  print(sddc_id)
  
  # Login to VMware Cloud on AWS
  vmc_client = create_vmc_client(refresh_token)
  
  # Check if the organization exists
  orgs = vmc_client.Orgs.list()
  if org_id not in [org.id for org in orgs]:
    raise ValueError("Org with ID {} doesn't exist".format(org_id))
  
  # Check if the sddc exists
  sddcs = vmc_client.orgs.Sddcs.list(org_id)
  if not sddcs:
    raise ValueError("require at least one SDDC associated"
                     "with the calling user")
  for sddc in sddcs:
    if sddc_id == sddc.id:
      return sddc
