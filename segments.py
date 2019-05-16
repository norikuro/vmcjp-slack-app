#!/usr/bin/env python
from vmcutils.metadata import get_members

def get_segments(gateway_type, nsx_client):
  get_members(nsx_client.infra.tier_1s.Segments.list(gateway_type)[0])
  print(nsx_client.infra.tier_1s.Segments.list(gateway_type)[0])
