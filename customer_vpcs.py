#!/usr/bin/env python

def get_customer_vpc(nsx_app_client):
  vpc = nsx_app_client.infra.LinkedVpcs.list().results[0]
  print(vpc)
  return {
    "linked_vpc_address": vpc.linked_vpc_addresses[0],
    "linked_account": vpc.linked_account,
    "linked_vpc_subnets_cidr": vpc.linked_vpc_subnets[0].cidr,
    "linked_vpc_subnets_id": vpc.linked_vpc_subnets[0].id,
    "linked_vpc_subnets_availability_zone": vpc.linked_vpc_subnets[0].availability_zone,
    "linked_vpc_id": vpc.linked_vpc_id,
    "route_table_id": vpc.route_table_ids[0]
  }
