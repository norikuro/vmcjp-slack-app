#!/usr/bin/env python

import argparse
import json

from datetime import datetime
from collections import OrderedDict
from com.vmware.vcenter_client import ResourcePool, Folder
from com.vmware.content_client import Library
from com.vmware.content.library_client import SubscribedItem
from vmcutils.s3 import write_json_to_s3, read_json_from_s3
from vmcutils.metadata import get_members
from vmc_client import get_sddc, get_vsphere_client


class SDDCConfig(object):
    def __init__(self):
        self.sddc_config = OrderedDict()
        self.sddc_config["updated"] = datetime.now().strftime("%Y/%m/%d")
        self.vsphere = None
        self.sddc = get_sddc("s3config.json")

    def get_sddc(self):
        self.sddc_config["sddc"] = {"id": self.sddc.id,
                                    "name": self.sddc.name,
                                    "num_hosts": len(self.sddc.resource_config.esx_hosts),
                                    "vpc_cidr": self.sddc.resource_config.vpc_info.vpc_cidr,
                                    "vmc_version": self.sddc.resource_config.sddc_manifest.vmc_version}

    def get_vcenter(self):
        self.sddc_config["vcenter"] = {"vc_url": self.sddc.resource_config.vc_url}

#    def connect_vcenter(self):
#        vc_host = parse.urlparse(self.sddc.resource_config.vc_url).hostname
#        vc_host = sddc.resource_config.vc_management_ip
#        self.vsphere = create_vsphere_client(vc_host, username=self.sddc.resource_config.cloud_username, password=self.sddc.resource_config.cloud_password)
#        self.vsphere = get_vsphere_client(self.sddc)
    
    def list_user_resourcepools(self):
        management_pools = ["Resources", 
                            "Mgmt-ResourcePool", 
                            "Compute-ResourcePool"]

        if not self.vsphere:
          self.vsphere = get_vsphere_client(self.sddc)

        rps = self.vsphere.vcenter.ResourcePool.list(filter=None)

        a = {}
        a["name"] = [i.name for i in filter(lambda x: not x.name in management_pools, rps)]
        self.sddc_config["resourcepools"] = a

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

        if not self.vsphere:
          self.vsphere = get_vsphere_client(self.sddc)

        folder_filter_spec = Folder.FilterSpec(type="VIRTUAL_MACHINE")
        folders = self.vsphere.vcenter.Folder.list(folder_filter_spec)

        a = {}
        a["name"] = [i.name for i in filter(lambda x: not x.name in management_folders, folders)]
        self.sddc_config["folders"] = a

    def list_contentlibrary(self):
        if not self.vsphere:
          self.vsphere = get_vsphere_client(self.sddc)

        contentlib_ids = self.vsphere.content.Library.list()
        a = []
        for id in contentlib_ids:
          t = str(self.vsphere.content.Library.get(id).type)
          if t == "LOCAL":
            a.append({"name": self.vsphere.content.Library.get(id).name, "type": t})
          elif t == "SUBSCRIBED":
            a.append({"name": self.vsphere.content.Library.get(id).name, 
                      "type": t, 
                      "subscription_url": self.vsphere.content.Library.get(id).subscription_info.subscription_url, 
                      "on_demand": self.vsphere.content.Library.get(id).subscription_info.on_demand,
                      "automatic_sync_enabled": self.vsphere.content.Library.get(id).subscription_info.automatic_sync_enabled})
        self.sddc_config["contentlibrary"] = a
        print(self.sddc_config)

    def output_to_s3(self):
        write_json_to_s3("vmc-env", "sddc.json", self.sddc_config)

def lambda_handler(event, context):
    sddc_operations = SDDCConfig()
    sddc_operations.get_sddc()
    sddc_operations.get_vcenter()
    sddc_operations.list_user_resourcepools()
    sddc_operations.list_user_folders()
    sddc_operations.list_contentlibrary()
    sddc_operations.output_to_s3()

def main():
    sddc_operations = SDDCConfig()
    sddc_operations.get_sddc()
    sddc_operations.get_vcenter()
    sddc_operations.list_user_resourcepools()
    sddc_operations.list_user_folders()
    sddc_operations.list_contentlibrary()
    sddc_operations.output_to_s3()

if __name__ == '__main__':
    main()
