#!/usr/bin/env python
from vmcutils.metadata import get_members

def get_segments(gateway_type, nsx_client):
  result = nsx_client.infra.tier_1s.Segments.list(gateway_type).results[0]
#  print(get_members(result))
  print(result.get_field("display_name"))
  print(result.get_field("domain_name"))
  print(result.get_field("id"))
  print(result.get_field("l2_extension"))
  print(result.get_field("links"))
  print(result.get_field("ls_id"))
  print(result.get_field("overlay_id"))
  print(result.get_field("parent_path"))
  print(result.get_field("path"))
  print(result.get_field("relative_path"))
  print(result.get_field("resource_type"))
  print(result.get_field("schema"))
  print(result.get_field("self_"))
  print(result.get_field("subnets"))
  print(result.get_field("system_owned"))
  print(result.get_field("tags"))
  print(result.get_field("type"))
