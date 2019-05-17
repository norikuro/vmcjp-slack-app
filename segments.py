#!/usr/bin/env python
from vmcutils.metadata import get_members

def get_segments(gateway_type, nsx_client):
  segments = nsx_client.infra.tier_1s.Segments.list(gateway_type).results
#  result = nsx_client.infra.tier_1s.Segments.list(gateway_type).results[11]
#  print(result.to_dict())
  b = []
  for segment in segments:
    if segment.get_field("type") != "DIS":
      b.append({"create_user": segment.get_field("create_user"),
           "display_name": segment.get_field("display_name"),
           "domain_name": segment.get_field("domain_name"),
           "l2_extension": segment.get_field("l2_extension"),
           "subnets": segment.get_field("subnets")[0].to_dict(),
           "type": segment.get_field("type")})
  print(b)
#  print("create_user ", result.get_field("create_user"))
#  print("display_name ", result.get_field("display_name"))
#  print("domain_name ", result.get_field("domain_name"))
#  print("id ", result.get_field("id"))
#  print("l2_extension ", result.get_field("l2_extension"))
#  print("links ", result.get_field("links"))
#  print("ls_id ", result.get_field("ls_id"))
#  print("overlay_id ", result.get_field("overlay_id"))
#  print("parent_path ", result.get_field("parent_path"))
#  print("path ", result.get_field("path"))
#  print("relative_path ", result.get_field("relative_path"))
#  print("resource_type ", result.get_field("resource_type"))
#  print("schema ", result.get_field("schema"))
#  print("self_ ", result.get_field("self_"))
#  print("subnets ", result.get_field("subnets"))
#  print("system_owned ", result.get_field("system_owned"))
#  print("tags ", result.get_field("tags"))
#  print("type ", result.get_field("type"))
#  subnet = result.get_field("subnets")[0]
#  print("subnet-----")
#  print("dhcp_ranges ", subnet.get_field("dhcp_ranges"))
#  print("gateway_address ", subnet.get_field("gateway_address"))
#  print("network ", subnet.get_field("network"))
