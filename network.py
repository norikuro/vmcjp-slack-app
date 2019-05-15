#!/usr/bin/env python

import json

from datetime import datetime
from collections import OrderedDict
from com.vmware.nsx_policy_client_for_vmc import create_nsx_policy_client_for_vmc
from vmcutils.S3 import write_json_to_s3, read_json_from_s3
from vmcutils.SecurityGroup import get_security_group

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

  def list_security_group(self):
    sg_list = []
    sg_list.append(get_security_group("mgw", self.nsx_client))
    sg_list.append(get_security_group("cgw", self.nsx_client))
    self.network_config["security_groups"] = sg_list
#    print(dict(self.network_config))
    
  def get_security_group(self, gateway_type):
    sg_system = ["/infra/domains/mgw/groups/hcx-ix-ips-public",
                 "ESXi",
                 "HCX",
                 "NSX Manager",
                 "vCenter"]
    group_list = []
    
    security_groups = self.nsx_client.infra.domains.Groups.list(gateway_type).results
#    print(security_groups[0].expression[0].__dict__.items())

    for sg in security_groups:
      dn = sg.display_name
      if dn not in sg_system and "HCX-IX-vm-" not in dn and "HCX-GRP-" not in dn and sg.expression != None:
        group_list.append(self.get_expressions(sg))
        
    return {"gateway_type": gateway_type, "groups": group_list}

  def get_expressions(self, sg):
    ex_list = []
    field_list = []    
#    dn = sg.display_name
    ex_dict = {"display_name": sg.display_name}
  
    for ex in sg.expression:
      sv = ex.get_struct_value()
      rt = sv.get_field("resource_type").value
      field_list.append({"resource_type": rt, "fields": self.get_fields(sv)})
      
    ex_dict["expressions"] = field_list
    ex_list.append(ex_dict)
    
    return ex_list

  def get_fields(self, struct_value):
    rt = struct_value.get_field("resource_type").value
    
    if rt == "IPAddressExpression":
      return [ip.value for ip in list(struct_value.get_field("ip_addresses"))]
    elif rt == "Condition":
      print("here----")
      print("member_type: ", struct_value.get_field("member_type").value)
      print("key: ", struct_value.get_field("key").value)
      print("operator: ", struct_value.get_field("operator").value)
      print("value: ", struct_value.get_field("value").value)
      print("resource_type: ", struct_value.get_field("resource_type").value)
      print("end----")
    elif rt == "ConjunctionOperator":
      print("ConjunctionOperator")
    elif rt == "NestedExpression":
      print("NestedExpression")
    else:
      print("aaa")
    
def lambda_handler(event, context):
  network_operations = NetworkConfig()
  network_operations.list_security_group()

def main():
  network_operations = NetworkConfig()
  network_operations.list_security_group()

if __name__ == '__main__':
  main()
