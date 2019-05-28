#!/usr/bin/env python

import json
import time

from datetime import datetime
from collections import OrderedDict
from vmcutils.s3 import write_json_to_s3
from vmcutils.metadata import get_members
from security_groups import get_security_groups
from firewall_rules import get_firewall_rules
from segments import get_segments
from vpns import get_l3vpns
from customer_vpcs import get_customer_vpc
from vmc_client import get_nsx_policy, get_nsx_app

class NetworkConfig(object):
    def __init__(self):
        self.network_config = OrderedDict()
        self.network_config["updated"] = datetime.now().strftime("%Y/%m/%d")

        start = time.time()
        self.nsx_client = get_nsx_policy("s3config.json")
        self.nsx_app_client = get_nsx_app("s3config.json")
        elapsed_time = time.time() - start
        print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")

    def list_customer_vpcs(self):
        start = time.time()
        self.network_config["customer_vpc"] = get_customer_vpc(self.nsx_app_client)
        elapsed_time = time.time() - start
        print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")
#        print(dict(self.network_config))
        
    def list_security_groups(self):
        start = time.time()
        self.network_config["security_groups"] = [
            get_security_groups("mgw", self.nsx_client),
            get_security_groups("cgw", self.nsx_client)
        ]
        elapsed_time = time.time() - start
        print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")
#        print(dict(self.network_config))

    def list_firewall_rules(self):
        start = time.time()
        self.network_config["firewall_rules"] = [
            get_firewall_rules("mgw", self.nsx_client),
            get_firewall_rules("cgw", self.nsx_client)
        ]
        elapsed_time = time.time() - start
        print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")
#        print(dict(self.network_config))
    
    def list_segments(self):
        start = time.time()
        self.network_config["segments"] = get_segments("cgw", self.nsx_client)
        elapsed_time = time.time() - start
        print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")
#        print(dict(self.network_config))

    def list_l3vpns(self):
        start = time.time()
        self.network_config["l3vpn"] = get_l3vpns(self.nsx_client)
        elapsed_time = time.time() - start
        print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")
#        print(dict(self.network_config))
        
    def output_to_s3(self):
        write_json_to_s3("vmc-env", "network.json", self.network_config)

def lambda_handler(event, context):
    network_operations = NetworkConfig()
    network_operations.list_customer_vpcs()
    network_operations.list_security_groups()
    network_operations.list_firewall_rules()
    network_operations.list_segments()
    network_operations.list_l3vpns()
    network_operations.output_to_s3()

def main():
    network_operations = NetworkConfig()
    network_operations.list_customer_vpcs()
#    network_operations.list_security_groups()
#    network_operations.list_firewall_rules()
#    network_operations.list_segments()
#    network_operations.list_l3vpns()
#    network_operations.output_to_s3()

if __name__ == '__main__':
    main()
