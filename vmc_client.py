#!/usr/bin/env python
import json

from com.vmware.vapi.std.errors_client import NotFound
from six.moves.urllib import parse
from vmware.vapi.vmc.client import create_vmc_client
from vmware.vapi.vsphere.client import create_vsphere_client
from com.vmware.nsx_policy_client_for_vmc import create_nsx_policy_client_for_vmc
from com.vmware.nsx_vmc_app_client_for_vmc import create_nsx_vmc_app_client_for_vmc
from vmcutils import s3utils
from vmcutils.metadata import get_members

class vmc(object):
  org_id = ""
  sddc_id = ""
  vmc_client = ""
  sddc = ""
  vsphere = ""
  
  def __init__(self):
    self.s3 = s3utils.s3()
    f = json.load(open("s3config.json", 'r'))
    t = s3.read_json_from_s3(f["bucket"], f["token"])
    j = s3.read_json_from_s3(f["bucket"], f["config"])
    self.token = t["token"]
    org_id = j["org_id"]
    sddc_id = j["sddc_id"]
    vmc_client = create_vmc_client(self.token)
    
    # Check if the organization exists
    orgs = vmc_client.Orgs.list()
    if org_id not in [org.id for org in orgs]:
      raise ValueError("Org with ID {} doesn't exist".format(org_id))
    
    # Check if the sddc exists and return existing sddc
    try:
      sddc = vmc_client.orgs.Sddcs.get(org_id, sddc_id)
    except NotFound:
      raise ValueError("SDDC with ID {} doesn't exist".format(sddc_id))
    
    vc_host = parse.urlparse(sddc.resource_config.vc_url).hostname
  #  vc_host = sddc.resource_config.vc_management_ip
  
    # Login to vCenter Server
    vsphere = create_vsphere_client(
      vc_host, 
      username=sddc.resource_config.cloud_username, 
      password=sddc.resource_config.cloud_password
    )
  
  def get_org_id(self):
    return org_id
  
  def get_vmc_client(self):
    return vmc_client
    
  def get_sddc(self):
    return sddc

  def get_vsphere(self):
    return vsphere

class nsx(object):
  nsx_policy = ""
  nsx_app = ""
  
  def __init__(self):
    self.s3 = s3utils.s3()
    f = json.load(open("s3config.json", 'r'))
    t = s3.read_json_from_s3(f["bucket"], f["token"])
    j = s3.read_json_from_s3(f["bucket"], f["config"])
    token = t["token"]
    org_id = j["org_id"]
    sddc_id = j["sddc_id"]
#    vmc_client = create_vmc_client(token)
    
    nsx_policy = create_nsx_policy_client_for_vmc(
      refresh_token=token,
      org_id=org_id,
      sddc_id=sddc_id
    )
    nsx_app = create_nsx_vmc_app_client_for_vmc(
      refresh_token=token,
      org_id=org_id,
      sddc_id=sddc_id
    )
    
  def get_nsx_policy(self):
    return nsx_policy

  def get_nsx_app(self):
    return nsx_app
