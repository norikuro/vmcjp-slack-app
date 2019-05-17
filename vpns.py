#!/usr/bin/env python
from vmcutils.metadata import get_members

def get_l3vpns(nsx_client):
  tier0_id = nsx_client.infra.Tier0s.list().results[0].get_field("id")
  tier1_id = nsx_client.infra.Tier1s.list().results[0].get_field("id")
  print(tier0_id)
  print(tier1_id)
  vpns = nsx_client.infra.tier_0s.locale_services.L3vpns.list("vmc", "default").results

  for vpn in vpns:
    {
      "enable_perfect_forward_secrecy": vpn.get_field("enable_perfect_forward_secrecy"),
      "ike_digest_algorithms": vpn.get_field("ike_digest_algorithms"),
      "dh_groups": vpn.get_field("dh_groups"),
      "tunnel_encryption_algorithms": vpn.get_field("tunnel_encryption_algorithms"),
      "id": vpn.get_field("id"),
      "ike_version": vpn.get_field("ike_version"),
      "display_name": vpn.get_field("display_name"),
      "remote_public_address": vpn.get_field("remote_public_address"),
      "local_address": vpn.get_field("local_address"),
      "ike_encryption_algorithms": vpn.get_field("ike_encryption_algorithms"),
      "l3vpn_session": get_vpn_session(vpn.get_field("l3vpn_session")),
      "remote_private_address": vpn.get_field("remote_private_address"),
      "tunnel_digest_algorithms": vpn.get_field("tunnel_digest_algorithms"),
      "enabled": vpn.get_field("enabled"),
      "resource_type": vpn.get_field("resource_type")
    }

#  print(type(obj))
#  print(get_members(obj))
#  print(obj.__dict__.items())
  print(obj.to_dict())
  
def get_vpn_session(session):
  a = []
  rules = session.get_field("rules")
  for rule in rules:
    a.append(
      {
        "sources": rules.get_field("sources"),
        "resource_type": rules.get_field("resource_type"),
        "id": rules.get_field("id"),
        "sequence_number": rules.get_field("sequence_number"),
        "destinations": rules.get_field("destinations"),
      }
    )
  return {"rules": a}
