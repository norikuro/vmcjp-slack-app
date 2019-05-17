#!/usr/bin/env python
import inspect

from security_groups import get_security_group_ids_and_names
from vmcutils.metadata import get_members
from vmcutils.listutils import compare_list_and_dict
from vmcutils.stringutils import replace_strings_in_list

def get_firewall_rules(gateway_type, nsx_client):
  admin_user = ["admin", "admin;admin"]
  rules_list = []
  
  security_groups = get_security_group_ids_and_names(gateway_type, nsx_client)
#  print(security_groups)

  policies = nsx_client.infra.domains.GatewayPolicies.get(gateway_type, "default")
# dict type
#  policies = nsx_client.infra.domains.GatewayPolicies.get(gateway_type, "default").to_dict()
  
#  print(policies.to_dict())

  gw_dn = policies.get_field("display_name")
  rules = policies.get_field("rules")
# dict type
#  gw_dn = policies["display_name"]
#  rules = policies["rules"]

  a = [get_rules(rule, gateway_type, security_groups) for rule in rules if rule.get_field("create_user") not in admin_user]
  print(a)
#  for rule in rules:
#    if rule.get_field("create_user") not in admin_user:
#      rules_list.insert(rule.get_field("sequence_number"), get_rules(rule, gateway_type, security_groups))
# dict type
#    if rule["_create_user"] not in admin_user:
#      rules_list.insert(rule["sequence_number"], get_rules(rule, gateway_type, security_groups))
  
#  print(rules_list)
#  get_members(rule)
#  return {"display_name": gw_dn, "rules": rules_list}
  return a

def get_rules(rule, gateway_type, security_groups):
  sn = rule.get_field("sequence_number")
#  sn = rule["sequence_number"]
  source_groups = rule.get_field("source_groups")
#  source_groups = rule["source_groups"]
  sg = replace_strings_in_list(source_groups, "/infra/domains/" + gateway_type + "/groups/")
  sg_names = compare_list_and_dict(sg, security_groups)
  dest_groups = rule.get_field("destination_groups")
#  dest_groups = rule["destination_groups"]
  dg = replace_strings_in_list(dest_groups, "/infra/domains/" + gateway_type + "/groups/")
  dg_names = compare_list_and_dict(dg, security_groups)

  return {"create_user": rule.get_field("create_user"),
          "display_name": rule.get_field("display_name"),
          "logged": rule.get_field("logged"),
          "destination_groups": dest_groups,
          "destination_groups_names": dg_names,
          "scope": rule.get_field("scope"),
          "services": rule.get_field("services"),
          "sequence_number": sn,
          "action": rule.get_field("action"),
          "source_groups": source_groups,
          "source_group_names": sg_names}

# dict type
#  return {"create_user": rule["_create_user"],
#          "display_name": rule["display_name"],
#          "logged": rule["logged"],
#          "destination_groups": dest_groups,
#          "destination_groups_names": dg_names,
#          "scope": rule["scope"],
#          "services": rule["services"],
#          "sequence_number": sn,
#          "action": rule["action"],
#          "source_groups": source_groups,
#          "source_group_names": sg_names}
