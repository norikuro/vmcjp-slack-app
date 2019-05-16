#!/usr/bin/env python

get_segments(gateway_type, nsx_client):
  print(nsx_client.infra.tier_1s.Segments.list(gateway_type))
