#!/usr/bin/env python
from vmcutils.metadata import get_members

def get_segments(gateway_type, nsx_client):
  segments = nsx_client.infra.tier_1s.Segments.list(gateway_type).results
#  b = []
#  for segment in segments:
#    if segment.get_field("create_user") != "admin":
#      b.append({"create_user": segment.get_field("create_user"),
#           "display_name": segment.get_field("display_name"),
#           "domain_name": segment.get_field("domain_name"),
#           "l2_extension": segment.get_field("l2_extension"),
#           "subnet": segment.get_field("subnets")[0].to_dict(),
#           "type": segment.get_field("type")})
#  print(b)
  b = [
    {"create_user": segment.get_field("create_user"),
     "display_name": segment.get_field("display_name"),
     "domain_name": segment.get_field("domain_name"),
     "l2_extension": segment.get_field("l2_extension"),
     "subnet": segment.get_field("subnets")[0].to_dict(),
     "type": segment.get_field("type")}
    for segment in segments 
    if segment.get_field("create_user") != "admin"
  ]
  return b
