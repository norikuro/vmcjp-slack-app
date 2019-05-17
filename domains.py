#!/usr/bin/env python
from vmcutils.metadata import get_members

def get_l3vpns(nsx_client):
#  obj = nsx_client.dns.forwarders.list
#  obj = nsx_client.infra.Tier0s.list()
  tier0_id = nsx_client.infra.Tier0s.list().results[0].get_field("id")
  tier1_id = nsx_client.infra.Tier1s.list().results[0].get_field("id")
  service_id = "default"
#  obj = nsx_client.infra.Services.list().results[0]
  obj = nsx_client.infra.tier_0s.locale_services.L3vpns.list(tier0_id, service_id)

#  print(type(obj))
  print(get_members(obj))
#  print(obj.__dict__.items())
  print(obj.to_dict())
