#!/usr/bin/env python

from vmware.vapi.vmc.client import create_vmc_client
from vmcutils.fileutils import load_json
from vmcutils.s3 import read_json_from_s3

def get_sddc(s3config_file):
  j = get_config("s3config.json")
  refresh_token = j["token"]
  org_id = j["org_id"]
  sddc_id = j["sddc_id"]
  
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
    
    if sddc_id in [sddc.id for sddc in sddcs]:
      return sddc
