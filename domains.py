#!/usr/bin/env python
from vmcutils.metadata import get_members

def get_domains(nsx_client):
  print(get_members(nsx_client.infra.services))
  print(nsx_client.infra.services)
