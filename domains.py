#!/usr/bin/env python

def get_domains(nsx_client):
  print(nsx_client.infra.Tier0s.list())
