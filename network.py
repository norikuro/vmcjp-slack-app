#!/usr/bin/env python

import json

from com.vmware.nsx_policy_client_for_vmc import create_nsx_policy_client_for_vmc
from vmcutils.s3 import write_json_to_s3, read_json_from_s3

class NetworkConfig(object):
  def __init__(self):
    f = json.load(open('s3config.json', 'r'))
    t = read_json_from_s3(f["bucket"], f["token"])
    j = read_json_from_s3(f["bucket"], f["config"])

    refresh_token = t["token"]
    org_id = j["org"]["id"]
    sddc_id = j["sddc"]["id"]
    
    self.nsx_client = create_nsx_policy_client_for_vmc(
        refresh_token=refresh_token,
        org_id=org_id,
        sddc_id=sddc_id)


  def list_security_group(self, gateway_type):
    security_groups = self.nsx_client.infra.domains.Groups.list(gateway_type).results
    print(security_groups)

def lambda_handler(event, context):
  network_operations = NetworkConfig()
  network_operations.list_security_group()

def main():
  network_operations = NetworkConfig()
  network_operations.list_security_group("mgw")

if __name__ == '__main__':
  main()
