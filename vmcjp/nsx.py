#!/usr/bin/env python

import json
import time

from datetime import datetime
from pytz import timezone
from vmcjp.utils import s3utils
from vmcjp.utils import dbutils
from vmcjp.utils.metadata import get_members
from vmcjp.network.security_groups import get_security_groups
from vmcjp.network.firewall_rules import get_firewall_rules
from vmcjp.network.segments import get_segments
from vmcjp.network.vpns import get_l3vpns
#from vmcjp.network.customer_vpcs import get_customer_vpc
from com.vmware.nsx_policy_client_for_vmc import create_nsx_policy_client_for_vmc
from com.vmware.nsx_vmc_app_client_for_vmc import create_nsx_vmc_app_client_for_vmc

S3_CONFIG = "vmcjp/s3config.json"

class NetworkConfig(object):
    DB_NAME = "sddc_db"
    COLLECTION_NAME = "sddc_collection"

    def __init__(self, config):
        s3 = s3utils.S3()
        f = json.load(open(config, "r"))
        j = s3.read_json_from_s3(f["bucket"], f["config"])
        token = j["token"]
        org_id = j["org_id"]
        sddc_id = j["sddc_id"]
        
        now = datetime.now(timezone("Asia/Tokyo")).strftime("%Y/%m/%d")
        
        self.db = dbutils.DocmentDb(config, NetworkConfig.DB_NAME, NetworkConfig.COLLECTION_NAME)
        self.db.upsert(
            {"sddc_updated": {"$exists":True}}, 
            {"$set": 
              {"network_updated": now}
            }
        )
        
        start = time.time()
        self.nsx_policy_client = create_nsx_policy_client_for_vmc(
            refresh_token=token,
            org_id=org_id,
            sddc_id=sddc_id
        )
        self.nsx_app_client = create_nsx_vmc_app_client_for_vmc(
            refresh_token=token,
            org_id=org_id,
            sddc_id=sddc_id
        )
        elapsed_time = time.time() - start
        print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")

    def list_customer_vpcs(self):
        start = time.time()
        vpc = nsx_app_client.infra.LinkedVpcs.list().results[0]
#        network_config = get_customer_vpc(self.nsx_app_client)
        network_config = {
            "linked_vpc_address": vpc.linked_vpc_addresses[0],
            "linked_account": vpc.linked_account,
            "linked_vpc_subnets_cidr": vpc.linked_vpc_subnets[0].cidr,
            "linked_vpc_subnets_id": vpc.linked_vpc_subnets[0].id,
            "linked_vpc_subnets_availability_zone": vpc.linked_vpc_subnets[0].availability_zone,
            "linked_vpc_id": vpc.linked_vpc_id,
            "route_table_id": vpc.route_table_ids[0]
        }
        self.db.upsert(
            {"network_updated": {"$exists":True}},
            {"$set": 
              {"customer_vpc": network_config}
            }
        )
        elapsed_time = time.time() - start
        print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")
        
    def list_security_groups(self):
        start = time.time()
        network_config = [
            get_security_groups("mgw", self.nsx_policy_client),
            get_security_groups("cgw", self.nsx_policy_client)
        ]
        self.db.upsert(
            {"network_updated": {"$exists":True}},
            {"$set": 
              {"security_groups": network_config}
            }
        )
        elapsed_time = time.time() - start
        print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")

    def list_firewall_rules(self):
        start = time.time()
        network_config = [
            get_firewall_rules("mgw", self.nsx_policy_client),
            get_firewall_rules("cgw", self.nsx_policy_client)
        ]
        self.db.upsert(
            {"network_updated": {"$exists":True}},
            {"$set": 
              {"firewall_rules": network_config}
            }
        )
        elapsed_time = time.time() - start
        print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")
    
    def list_segments(self):
        start = time.time()
        network_config = get_segments("cgw", self.nsx_policy_client)
        self.db.upsert(
            {"network_updated": {"$exists":True}},
            {"$set": 
              {"segments": network_config}
            }
        )
        elapsed_time = time.time() - start
        print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")

    def list_l3vpns(self):
        start = time.time()
        network_config = get_l3vpns(self.nsx_policy_client)
        self.db.upsert(
            {"network_updated": {"$exists":True}},
            {"$set": 
              {"l3vpn": network_config}
            }
        )
        elapsed_time = time.time() - start
        print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")

def lambda_handler(event, context):
    network_operations = NetworkConfig(S3_CONFIG)
    network_operations.list_customer_vpcs()
    network_operations.list_security_groups()
    network_operations.list_firewall_rules()
    network_operations.list_segments()
    network_operations.list_l3vpns()

def main():
    network_operations = NetworkConfig(S3_CONFIG)
    network_operations.list_customer_vpcs()
    network_operations.list_security_groups()
    network_operations.list_firewall_rules()
    network_operations.list_segments()
    network_operations.list_l3vpns()

if __name__ == '__main__':
    main()
