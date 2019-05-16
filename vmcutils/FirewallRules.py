#!/usr/bin/env python
import inspect

from vmcutils.Metadata import get_members
from vmcutils.SecurityGroups import get_security_group_ids_and_names

def get_firewall_rules(gateway_type, nsx_client):
  rule_system = ["vCenter Outbound Rule", "ESXi Outbound Rule", "Default VTI Rule"]
  rules_list = []
  
  sg_dict = get_security_group_ids_and_names(gateway_type, nsx_client)
#  print(sg_dict)
  
#  print(nsx_client.Infra.get())
#  print(nsx_client.infra.Tier1s.list())
#  print(nsx_client.infra.tier_1s.Segments.list('cgw'))
#  print(nsx_client.infra.Domains.list())

  policies = nsx_client.infra.domains.GatewayPolicies.get(gateway_type, "default")
  gw_dn = policies.get_field("display_name")
  rules = policies.get_field("rules")
  for rule in rules:
    a = {}
    dn = rule.get_field("display_name")
    if dn not in rule_system:
      sn = rule.get_field("sequence_number")
      sg = rule.get_field("source_groups")
      dg = rule.get_field("destination_groups")
      print(sg)
#      sg_names = compare_list_dict(sg, sg_dict)
      a = {"create_user": rule.get_field("create_user"),
           "display_name": rule.get_field("display_name"),
           "logged": rule.get_field("logged"),
           "destination_groups": dg,
           "scope": rule.get_field("scope"),
           "services": rule.get_field("services"),
           "sequence_number": sn,
           "action": rule.get_field("action"),
           "source_groups": sg}
#      print(rule)
      rules_list.insert(sn, a)
#  print(rules)
#  get_members(rule)
  return {"display_name": gw_dn, "rules": rules_list}

def compare_list_dict(ls, dic):
  value_list = []
  key_list = dic.keys()
  and_list = set(key_list) & set(ls)
  for id in and_list:
    value_list.append(dic[id])
#  print(value_list)
    
