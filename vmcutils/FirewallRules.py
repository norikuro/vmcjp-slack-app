#!/usr/bin/env python
import inspect

from vmcutils.Metadata import get_members

def get_firewall_rules(nsx_client):
#  print(nsx_client.Infra.get())
#  print(nsx_client.infra.Tier1s.list())
#  print(nsx_client.infra.tier_1s.Segments.list('cgw'))
#  print(nsx_client.infra.Domains.list())

  policies = nsx_client.infra.domains.GatewayPolicies.get('mgw', 'default')
  gw_dn = policies.get_field("display_name")
  rules = policies.get_field("rules")
  for rule in rules:
    get_members(rule)    
#  print(rules)
