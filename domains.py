#!/usr/bin/env python
from vmcutils.metadata import get_members

def get_domains(nsx_client):
  print(get_members(nsx_client.infra.Tier0s.list()))
  print(nsx_client.infra.Tier0s.list().get_struct_value())
