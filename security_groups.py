#!/usr/bin/env python

from vmcutils.metadata import get_members

def get_security_groups(gateway_type, nsx_client):
    sys_usr = ["admin", "admin;admin"]
    group_list = []

    security_groups = nsx_client.infra.domains.Groups.list(gateway_type).results

    for sg in security_groups:
      usr = sg.get_field("_create_user")
#      print(usr)
      if usr not in sys_usr:
        group_list.append(get_expressions(sg))

    return {"gateway_type": gateway_type, "groups": group_list}

def get_expressions(sg):
    ex_dict = {"display_name": sg.get_field("display_name"),
               "id": sg.get_field("id")}
    
    ex_dict["expressions"] = [get_fields(ex.get_struct_value()) for ex in sg.get_field("expression")]

    return ex_dict

def get_fields(struct_value):
    rt = struct_value.get_field("resource_type").value

    if rt == "IPAddressExpression":
      return {"resource_type": rt, 
              "ip_addresses": [ip.value for ip in list(struct_value.get_field("ip_addresses"))]}
    elif rt == "Condition":
      return {"resource_type": rt,
              "member_type": struct_value.get_field("member_type").value,
              "key": struct_value.get_field("key").value,
              "operator": struct_value.get_field("operator").value,
              "value": struct_value.get_field("value").value}
    elif rt == "ConjunctionOperator":
      return {"resource_type": rt,
              "conjunction_operator": struct_value.get_field("conjunction_operator").value}
    elif rt == "NestedExpression":
      print("NestedExpression")
    else:
      print("else expression")

def get_security_group_ids_and_names(gateway_type, nsx_client):
  security_groups = nsx_client.infra.domains.Groups.list(gateway_type).results
#  security_groups = nsx_client.infra.domains.Groups.list(gateway_type).to_dict()["results"]
  return {sg.get_field("id"):sg.get_field("display_name") for sg in security_groups}
#  return {sg["id"]:sg["display_name"] for sg in security_groups}
