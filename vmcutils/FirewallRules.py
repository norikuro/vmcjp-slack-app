#!/usr/bin/env python
import inspect

def get_firewall_rules(nsx_client):
#  print(nsx_client.Infra.get())
#  print(nsx_client.infra.Tier1s.list())
#  print(nsx_client.infra.tier_1s.Segments.list('cgw'))
#  print(nsx_client.infra.Domains.list())
  obj = nsx_client.infra.domains.GatewayPolicies.get('mgw', 'default')
  struct_value = obj.get_struct_value()
  print(obj)
  for x in inspect.getmembers(obj, inspect.ismethod):
    print x[0]
