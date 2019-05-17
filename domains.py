#!/usr/bin/env python
from vmcutils.metadata import get_members

def get_domains(nsx_client):
#  obj = nsx_client.dns.forwarders.list
  obj = nsx_client
  print(type(obj))
  print(get_members(obj))
  print(obj)
