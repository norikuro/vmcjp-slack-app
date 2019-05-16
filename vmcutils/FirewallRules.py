#!/usr/bin/env python
import inspect

from vmcutils.Metadata import get_members

def get_firewall_rules(nsx_client):
  rule_system = ["vCenter Outbound Rule", "ESXi Outbound Rule"]
#  print(nsx_client.Infra.get())
#  print(nsx_client.infra.Tier1s.list())
#  print(nsx_client.infra.tier_1s.Segments.list('cgw'))
#  print(nsx_client.infra.Domains.list())

  policies = nsx_client.infra.domains.GatewayPolicies.get('mgw', 'default')
  gw_dn = policies.get_field("display_name")
  rules = policies.get_field("rules")
  for rule in rules:
    dn = rule.get_field("display_name")
    if dn not in rule_system:
#      get_members(rule)
      print("here----")
      print(rule.get_field("create_user"))
      print(rule.get_field("display_name"))
      print(rule.get_field("destination_groups"))
      print(rule.get_field("services"))
      print(rule.get_field("sequence_number"))
      print(rule.get_field("action"))
      print(rule.get_field("source_groups"))
      print("end----")
#  print(rules)
