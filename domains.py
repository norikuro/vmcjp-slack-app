#!/usr/bin/env python
from vmcutils.metadata import get_members

def get_domains(nsx_client):
  obj = nsx_client.infra.tier_0s.locale_services.L3vpnContext.get()
  print(get_members(obj))
  print(obj)
