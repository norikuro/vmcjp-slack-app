#!/usr/bin/env python
import inspect

def get_firewall_rules(nsx_client):
#  print(nsx_client.Infra.get())
#  print(nsx_client.infra.Tier1s.list())
#  print(nsx_client.infra.tier_1s.Segments.list('cgw'))
#  print(nsx_client.infra.Domains.list())
  obj = nsx_client.infra.domains.GatewayPolicies.get('mgw', 'default')
  field = obj.get_field("rules")
  print(field[0])
  for x in inspect.getmembers(field[0], inspect.ismethod):
    print x[0]
