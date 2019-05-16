#!/usr/bin/env python

get_segments(nsx_client):
  print(nsx_client.infra.tier_1s.Segments.list('cgw'))
