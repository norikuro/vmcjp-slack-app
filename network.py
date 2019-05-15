#!/usr/bin/env python

import json

from datetime import datetime
from collections import OrderedDict
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

    self.network_config = OrderedDict()
    self.network_config["updated"] = datetime.now().strftime("%Y/%m/%d")

    
    self.nsx_client = create_nsx_policy_client_for_vmc(
        refresh_token=refresh_token,
        org_id=org_id,
        sddc_id=sddc_id)

  def list_security_group(self, gateway_type):
    sg_system = ["/infra/domains/mgw/groups/hcx-ix-ips-public",
                 "ESXi",
                 "HCX",
                 "NSX Manager",
                 "vCenter"]
    security_groups = self.nsx_client.infra.domains.Groups.list(gateway_type).results
    c = []
    for sg in security_groups:
      dn = sg.display_name
#      a = {}
      if dn not in sg_system and "HCX-IX-vm-" not in dn and "HCX-GRP-" not in dn and sg.expression != None:
#        a["display_name"] = dn
#        for ex in sg.expression:
#          a.update(self.get_expressions(ex))
        print(self.get_expressions(sg))
#        c.append([self.get_expressions(ex, dn) for ex in sg.expression])
#        print(c)
#    self.network_config["security_groups"] = c
#    print(dict(self.network_config))

#  def get_expressions(self, expression):
  def get_expressions(self, sg):
    b = []
    for ex in sg.expression:
      sv = ex.get_struct_value()
      rt = sv.get_field("resource_type").value
      a = {}
      a["display_name"] = sg.display_name
      a["resource_type"] = rt
      a["expressions"] = self.get_fields(sv, rt)
      b.append(a)
    print(b[0])
    return b

  def get_fields(self, struct_value, resource_type):
    if resource_type == "IPAddressExpression":
      return [ip.value for ip in list(struct_value.get_field("ip_addresses"))]
    return None
    
def lambda_handler(event, context):
  network_operations = NetworkConfig()
  network_operations.list_security_group()

def main():
  network_operations = NetworkConfig()
  network_operations.list_security_group("mgw")

if __name__ == '__main__':
  main()
