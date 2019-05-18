#!/usr/bin/env python

from com.vmware.vapi.std.errors_client import NotFound

from six.moves.urllib import parse
from vmware.vapi.vmc.client import create_vmc_client
from vmware.vapi.vsphere.client import create_vsphere_client
from vmcutils.fileutils import load_json
from vmcutils.s3 import read_json_from_s3
from vmcutils.metadata import get_members

def get_sddc(s3config):
  f = load_json(s3config)
  t = read_json_from_s3(f["bucket"], f["token"])
  j = read_json_from_s3(f["bucket"], f["config"])
  
  refresh_token = t["token"]
  org_id = j["org"]["id"]
  sddc_id = j["sddc"]["id"]
  
  # Login to VMware Cloud on AWS
  vmc_client = create_vmc_client(refresh_token)
  
  # Check if the organization exists
#  orgs = vmc_client.Orgs.list()
#  if org_id not in [org.id for org in orgs]:
#    raise ValueError("Org with ID {} doesn't exist".format(org_id))
  
#  org_id = "1c8787fb-d284-4cbd-92d2-860ad7a826b"
#  orgg = "1c8787fb-d284-4cbd-92d2-860ad7a826b0"
#  vmc_client.Orgs.get("1c8787fb-d284-4cbd-92d2-860ad7a826b")
  
  # Check if the sddc exists and return existing sddc
  try:
    return vmc_client.orgs.Sddcs.get(org_id, sddc_id)
  except NotFound:
    print("SDDC with ID {} doesn't exist".format(sddc_id))

def get_vsphere(sddc):
  vc_host = parse.urlparse(sddc.resource_config.vc_url).hostname
#  vc_host = sddc.resource_config.vc_management_ip

  # Login to vCenter Server
  return create_vsphere_client(
    vc_host, 
    username=sddc.resource_config.cloud_username, 
    password=sddc.resource_config.cloud_password
  )
