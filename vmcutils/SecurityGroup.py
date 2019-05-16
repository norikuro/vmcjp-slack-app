#!/usr/bin/env python

def get_security_groups(gateway_type, nsx_client):
    sg_system = ["/infra/domains/mgw/groups/hcx-ix-ips-public",
                 "ESXi",
                 "HCX",
                 "NSX Manager",
                 "vCenter"]
    group_list = []

    security_groups = nsx_client.infra.domains.Groups.list(gateway_type).results

    for sg in security_groups:
      dn = sg.display_name
      if dn not in sg_system and "HCX-IX-vm-" not in dn and "HCX-GRP-" not in dn and sg.expression != None:
        group_list.append(get_expressions(sg))

    return {"gateway_type": gateway_type, "groups": group_list}

def get_expressions(sg):
    field_list = []
    ex_dict = {"display_name": sg.display_name}

    for ex in sg.expression:
      print(i)
      sv = ex.get_struct_value()
      rt = sv.get_field("resource_type").value
      field_list.append(get_fields(sv))

    ex_dict["expressions"] = field_list
    return ex_dict

def get_fields(struct_value):
    rt = struct_value.get_field("resource_type").value

    if rt == "IPAddressExpression":
      return {"resource_type": rt, 
              "ip_addresses": [ip.value for ip in list(struct_value.get_field("ip_addresses"))]}
    elif rt == "Condition":
#      print("here----")
#      print(struct_value)
#      print("end----")
      return {"resource_type": rt,
              "member_type": struct_value.get_field("member_type").value,
              "key": struct_value.get_field("key").value,
              "operator": struct_value.get_field("operator").value,
              "value": struct_value.get_field("value").value}
    elif rt == "ConjunctionOperator":
#      print("here----")
#      print(struct_value)
#      print("end----")
      return {"resource_type": rt,
              "conjunction_operator": struct_value.get_field("conjunction_operator").value}
    elif rt == "NestedExpression":
      print("NestedExpression")
#      print("here----")
#      print(struct_value)
#      print("end----")
    else:
      print("else expression")
#      print("here----")
#      print(struct_value)
#      print("end----")
