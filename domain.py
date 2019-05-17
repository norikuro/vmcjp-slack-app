#!/usr/bin/env python

def get_domain(nsx_client):
  print(nsx_client.infra.Domains.list())
