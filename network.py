#!/usr/bin/env python

import json

from datetime import datetime
from collections import OrderedDict
from com.vmware.nsx_policy_client_for_vmc import create_nsx_policy_client_for_vmc
from vmcutils.S3 import write_json_to_s3, read_json_from_s3
from vmcutils.SecurityGroup import get_security_groups
from vmcutils.FirewallRule import get_firewall_rules

class NetworkConfig(object):
    def __init__(self):
        f = json.load(open('s3config.json', 'r'))
        t = read_json_from_s3(f["bucket"], f["token"])
        j = read_json_from_s3(f["bucket"], f["config"])

        refresh_token = t["token"]
        org_id = j["org"]["id"]
        sddc_id = j["sddc"]["id"]
        
        self.network_config = OrderedDict()
        self.network_config["updated"] = datetime.now().strftime("%Y/%m/%d")
        
        self.nsx_client = create_nsx_policy_client_for_vmc(
          refresh_token=refresh_token,
          org_id=org_id,
          sddc_id=sddc_id)

    def list_security_groups(self):
        sg_list = []
        sg_list.append(get_security_groups("mgw", self.nsx_client))
        sg_list.append(get_security_groups("cgw", self.nsx_client))
        self.network_config["security_groups"] = sg_list
#        print(dict(self.network_config))

    def list_firewall_rules(self):
        get_firewall_rules(self.nsx_client)
    
    def output_to_s3(self):
        write_json_to_s3("vmc-env", "network.json", self.network_config)

def lambda_handler(event, context):
    network_operations = NetworkConfig()
    network_operations.list_security_groups()
    network_operations.output_to_s3()

def main():
    network_operations = NetworkConfig()
    network_operations.list_security_groups()
    network_operations.output_to_s3()


if __name__ == '__main__':
    main()
