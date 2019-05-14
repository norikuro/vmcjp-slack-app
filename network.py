#!/usr/bin/env python

class NetworkConfig(Object):
  def list_security_group(self):
    nsx_client = create_nsx_policy_client_for_vmc(
          refresh_token=args.refresh_token,
          org_id=args.org_id,
          sddc_id=args.sddc_id)

    security_groups = nsx_client.infra.domains.Groups.list(gateway_type).results
    print(security_groups)

def lambda_handler(event, context):
  network_operations = NetworkConfig()
  network_operations.list_security_group()

def main():
  network_operations = NetworkConfig()
  network_operations.list_security_group()

if __name__ == '__main__':
  main()
