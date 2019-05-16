#!/usr/bin/env python
import inspect

from vmcutils.Metadata import get_members

def get_firewall_rules(gateway_type, nsx_client):
  rule_system = ["vCenter Outbound Rule", "ESXi Outbound Rule"]
  rules_list = []
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
      a = {"create_user": rule.get_field("create_user"),
           "display_name": rule.get_field("display_name"),
           "destination_groups": rule.get_field("destination_groups"),
           "services": rule.get_field("services"),
           "sequence_number": sn,
           "action": rule.get_field("action"),
           "source_groups": rule.get_field("source_groups"),
           "logged": rule.get_field("logged")}
      print(rule)
      rules_list.insert(sn, a)
#  print(rules)
#  get_members(rule)
  return {"display_name": gw_dn, "rules": rules_list}
