#!/usr/bin/env python

from com.vmware.vapi.std.errors_client import NotFound

from six.moves.urllib import parse
from vmware.vapi.vmc.client import create_vmc_client
from vmware.vapi.vsphere.client import create_vsphere_client
from com.vmware.nsx_policy_client_for_vmc import create_nsx_policy_client_for_vmc
from com.vmware.nsx_vmc_app_client_for_vmc import create_nsx_vmc_app_client_for_vmc
from vmcutils.fileutils import load_json
from vmcutils import s3
from vmcutils.metadata import get_members

s3 = s3()

def get_sddc(s3config):
  f = load_json(s3config)
  t = s3.read_json_from_s3(f["bucket"], f["token"])
  j = s3.read_json_from_s3(f["bucket"], f["config"])
  
  # Login to VMware Cloud on AWS
  vmc_client = create_vmc_client(t["token"])
  
  # Check if the organization exists
  orgs = vmc_client.Orgs.list()
  if j["org_id"] not in [org.id for org in orgs]:
    raise ValueError("Org with ID {} doesn't exist".format(j["org_id"]))
    
  # Check if the sddc exists and return existing sddc
  try:
    return vmc_client.orgs.Sddcs.get(j["org_id"], j["sddc_id"])
  except NotFound:
    raise ValueError("SDDC with ID {} doesn't exist".format(j["sddc_id"]))

def get_vsphere(sddc):
  vc_host = parse.urlparse(sddc.resource_config.vc_url).hostname
#  vc_host = sddc.resource_config.vc_management_ip

  # Login to vCenter Server
  return create_vsphere_client(
    vc_host, 
    username=sddc.resource_config.cloud_username, 
    password=sddc.resource_config.cloud_password
  )

def get_nsx_policy(s3config):
  f = load_json(s3config)
  t = s3.read_json_from_s3(f["bucket"], f["token"])
  j = s3.read_json_from_s3(f["bucket"], f["config"])
  
  return create_nsx_policy_client_for_vmc(
    refresh_token=t["token"],
    org_id=j["org_id"],
    sddc_id=j["sddc_id"]
  )

def get_nsx_app(s3config):
  f = load_json(s3config)
  t = s3.read_json_from_s3(f["bucket"], f["token"])
  j = s3.read_json_from_s3(f["bucket"], f["config"])
  
  return create_nsx_vmc_app_client_for_vmc(
    refresh_token=t["token"],
    org_id=j["org_id"],
    sddc_id=j["sddc_id"]
  )
