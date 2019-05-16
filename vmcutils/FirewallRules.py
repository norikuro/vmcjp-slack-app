#!/usr/bin/env python
import inspect

from vmcutils.Metadata import get_members

def get_firewall_rules(nsx_client):
#  print(nsx_client.Infra.get())
#  print(nsx_client.infra.Tier1s.list())
#  print(nsx_client.infra.tier_1s.Segments.list('cgw'))
#  print(nsx_client.infra.Domains.list())
  obj = nsx_client.infra.domains.GatewayPolicies.get('mgw', 'default')
  rules = obj.get_field("rules")
  dn = obj.get_field("display_name")
  print(obj)
#  print(field[0])
  get_members(obj)
  
