#!/usr/bin/env python
from vmcutils.metadata import get_members

def get_domains(nsx_client):
  obj = nsx_client
  print(get_members(obj))
  print(obj)
