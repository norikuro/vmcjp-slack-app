#!/usr/bin/env python
from vmcutils.metadata import get_members

def get_l3vpns(nsx_client):
  tier0_id = nsx_client.infra.Tier0s.list().results[0].get_field("id")
  tier1_id = nsx_client.infra.Tier1s.list().results[0].get_field("id")
  print(tier0_id)
  print(tier1_id)
  vpns = nsx_client.infra.tier_0s.locale_services.L3vpns.list("vmc", "default").results

  for vpn in vpns:
    vpn.get_field("enable_perfect_forward_secrecy")


#  print(type(obj))
#  print(get_members(obj))
#  print(obj.__dict__.items())
  print(obj.to_dict())
