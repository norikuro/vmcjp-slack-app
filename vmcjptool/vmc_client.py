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

class Nsx(object):
  def __init__(self):
    s3 = s3utils.S3()
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
