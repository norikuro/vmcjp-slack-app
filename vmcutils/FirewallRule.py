#!/usr/bin/env python

def get_firewall_rules(nsx_client):
  print(nsx_client.Infra.get())
