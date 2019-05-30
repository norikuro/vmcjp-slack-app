#!/usr/bin/env python

import argparse
import json

from datetime import datetime
from collections import OrderedDict
from com.vmware.vcenter_client import ResourcePool, Folder
from com.vmware.content_client import Library
from vmcutils import s3utils
from vmcutils import dbutils
from vmcutils.metadata import get_members
import vmc_client

class SDDCConfig(object):
    def __init__(self):
        vmc = vmc_client.vmc()
        
        self.sddc_config = OrderedDict()
        self.sddc_config["sddc_updated"] = datetime.now().strftime("%Y/%m/%d")
        self.sddc = vmc.get_sddc()
        self.vsphere = vmc.get_vsphere()
        
        self.db = dbutils.db()
        self.db.upsert(
            {"sddc.id": vmc.sddc_id}, 
            {"$set": 
              {"sddc_updated": datetime.now().strftime("%Y/%m/%d")}
            }
        )

    def get_sddc_config(self):
        sddc_config = {
            "id": self.sddc.id,
            "name": self.sddc.name,
            "num_hosts": len(self.sddc.resource_config.esx_hosts),
            "vpc_cidr": self.sddc.resource_config.vpc_info.vpc_cidr,
            "vmc_version": self.sddc.resource_config.sddc_manifest.vmc_version,
            "region": self.sddc.resource_config.region
        }
        
        self.sddc_config["sddc"] = sddc_config
        
        self.db.upsert(
            {"sddc.id": vmc.sddc_id}, 
            {"$set": 
              {"sddc": datetime.now().strftime("%Y/%m/%d")}
            }
        )
#        print(self.sddc_config)

    def get_vcenter(self):
        self.sddc_config["vcenter"] = {"vc_url": self.sddc.resource_config.vc_url}
#        print(self.sddc_config)

    def list_user_resourcepools(self):
        management_pools = ["Resources", 
                            "Mgmt-ResourcePool", 
                            "Compute-ResourcePool"]

        rps = self.vsphere.vcenter.ResourcePool.list(filter=None)

        self.sddc_config["resourcepools"] = {"name": [rp.name for rp in rps if not rp.name in management_pools]}
#        print(dict(self.sddc_config))

    def list_user_folders(self):
        management_folders = ["Discovered virtual machine", 
                              "VMs migrated to cloud", 
                              "ClonePrepInternalTemplateFolder", 
                              "ClonePrepReplicaVmFolder", 
                              "ClonePrepParentVmFolder", 
                              "ClonePrepResyncVmFolder", 
                              "vm", 
                              "Management VMs", 
                              "Workloads", "Templates"]

        folder_filter_spec = Folder.FilterSpec(type="VIRTUAL_MACHINE")
        folders = self.vsphere.vcenter.Folder.list(folder_filter_spec)

        self.sddc_config["folders"] = {"name": [fl.name for fl in folders if not fl.name in management_folders]}
#        print(dict(self.sddc_config))

    def list_contentlibrary(self):
        libs = self.vsphere.content.Library
        lib_ids = libs.list()
        
        a = []
        for id in lib_ids:
          lib = libs.get(id)
          t = str(lib.type)
          if t == "LOCAL":
            a.append({"name": lib.name, "type": t})
          elif t == "SUBSCRIBED":
            a.append({"name": lib.name, 
                      "type": t, 
                      "subscription_url": lib.subscription_info.subscription_url, 
                      "on_demand": lib.subscription_info.on_demand,
                      "automatic_sync_enabled": lib.subscription_info.automatic_sync_enabled})
        self.sddc_config["contentlibrary"] = a
#        print(self.sddc_config)
    def insert_to_db(self):
        db = dbutils.db()
#        db.insert(self.sddc_config)

    def output_to_s3(self):
        s3 = s3utils.s3()
        s3.write_json_to_s3("vmc-env", "sddc.json", self.sddc_config)

def lambda_handler(event, context):
    sddc_operations = SDDCConfig()
    sddc_operations.get_sddc_config()
    sddc_operations.get_vcenter()
    sddc_operations.list_user_resourcepools()
    sddc_operations.list_user_folders()
    sddc_operations.list_contentlibrary()
    sddc_operations.output_to_s3()

def main():
    sddc_operations = SDDCConfig()
    sddc_operations.get_sddc_config()
#    sddc_operations.get_vcenter()
#    sddc_operations.list_user_resourcepools()
#    sddc_operations.list_user_folders()
#    sddc_operations.list_contentlibrary()
#    sddc_operations.insert_to_db()
#    sddc_operations.output_to_s3()

if __name__ == '__main__':
    main()
