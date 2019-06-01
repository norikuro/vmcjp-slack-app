#!/usr/bin/env python

import json

from com.vmware.vapi.std.errors_client import NotFound
from six.moves.urllib import parse
from vmware.vapi.vmc.client import create_vmc_client
from vmware.vapi.vsphere.client import create_vsphere_client
from com.vmware.nsx_policy_client_for_vmc import create_nsx_policy_client_for_vmc
from com.vmware.nsx_vmc_app_client_for_vmc import create_nsx_vmc_app_client_for_vmc
from vmcjptool.utils import s3utils
from vmcjptool.utils.metadata import get_members

class vmc(object):
  def __init__(self):
    s3 = s3utils.s3()
    f = json.load(open("s3config.json", 'r'))
    t = s3.read_json_from_s3(f["bucket"], f["token"])
    j = s3.read_json_from_s3(f["bucket"], f["config"])
    token = t["token"]
    
    self.org_id = j["org_id"]
    self.sddc_id = j["sddc_id"]
    self.vmc_client = create_vmc_client(token)
    self.orgs = self.vmc_client.orgs
    self.org = self.vmc_client.Orgs.get(self.org_id)
    self.sddc = self.vmc_client.orgs.Sddcs.get(self.org_id, self.sddc_id)
    self.vsphere = create_vsphere_client(
      parse.urlparse(self.sddc.resource_config.vc_url).hostname, 
      username=self.sddc.resource_config.cloud_username, 
      password=self.sddc.resource_config.cloud_password
    )
    self.vcenter = self.vsphere.vcenter

class nsx(object):
  def __init__(self):
    s3 = s3utils.s3()
    f = json.load(open("s3config.json", 'r'))
    t = s3.read_json_from_s3(f["bucket"], f["token"])
    j = s3.read_json_from_s3(f["bucket"], f["config"])
    token = t["token"]
    org_id = j["org_id"]
    sddc_id = j["sddc_id"]
#    vmc_client = create_vmc_client(token)
    
    self.nsx_policy = create_nsx_policy_client_for_vmc(
      refresh_token=token,
      org_id=org_id,
      sddc_id=sddc_id
    )
    self.nsx_app = create_nsx_vmc_app_client_for_vmc(
      refresh_token=token,
      org_id=org_id,
      sddc_id=sddc_id
    )
    
  def get_nsx_policy(self):
    return self.nsx_policy

  def get_nsx_app(self):
    return self.nsx_app
