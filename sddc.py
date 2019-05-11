#!/usr/bin/env python

import argparse
import json

from datetime import datetime
from collections import OrderedDict
from six.moves.urllib import parse
from vmware.vapi.vmc.client import create_vmc_client
from vmware.vapi.vsphere.client import create_vsphere_client
from com.vmware.vcenter_client import ResourcePool, Folder
from com.vmware.content_client import Library
from com.vmware.content.library_client import SubscribedItem
from vmcutils.s3 import write_json_to_s3, read_json_from_s3


class SDDCConfig(object):
    def __init__(self):
        f = json.load(open('s3config.json', 'r'))
        j = read_json_from_s3(f["bucket"], f["file"])

        self.refresh_token = j["account"]["token"]
        self.org_id = j["org"]["id"]

        self.sddc_config = OrderedDict()
        self.sddc_config["updated"] = datetime.now().strftime("%Y/%m/%d")

        # Login to VMware Cloud on AWS
        self.vmc_client = create_vmc_client(self.refresh_token)

        self.vsphere = ""

    def setup(self):
        # Check if the organization exists
        orgs = self.vmc_client.Orgs.list()
        if self.org_id not in [org.id for org in orgs]:
            raise ValueError("Org with ID {} doesn't exist".format(
                self.org_id))

        self.sddcs = self.vmc_client.orgs.Sddcs.list(self.org_id)

    def list_sddc(self):
        if not self.sddcs:
            raise ValueError('require at least one SDDC associated'
                             'with the calling user')

        a = []
        for sddc in self.sddcs:
          if not len(sddc.resource_config.esx_hosts) == 1:
            a.append({"id": sddc.id, "name": sddc.name, "num_hosts": len(sddc.resource_config.esx_hosts), "vpc_cidr": sddc.resource_config.vpc_info.vpc_cidr, "vmc_version": sddc.resource_config.sddc_manifest.vmc_version})
        self.sddc_config["sddcs"] = a

    def list_vcenter(self):
        a = []
        for sddc in self.sddcs:
          if not len(sddc.resource_config.esx_hosts) == 1:
            a.append({"vc_url": sddc.resource_config.vc_url})
        self.sddc_config["vcenters"] = a

    def connect_vcenter(self):
        sddc = self.sddcs[0]
        vc_host = parse.urlparse(sddc.resource_config.vc_url).hostname
#        vc_host = sddc.resource_config.vc_management_ip
        self.vsphere = create_vsphere_client(vc_host, username=sddc.resource_config.cloud_username, password=sddc.resource_config.cloud_password)

    def list_user_resourcepools(self):
        management_pools = ["Resources", "Mgmt-ResourcePool", "Compute-ResourcePool"]

        if not self.vsphere:
          self.connect_vcenter()

        rps = self.vsphere.vcenter.ResourcePool.list(filter=None)
        a = []
        for rp in rps:
          if not rp.name in management_pools:
            a.append({"name": rp.name})
        self.sddc_config["resourcepools"] = a

    def list_user_folders(self):
        management_folders = ["Discovered virtual machine", "VMs migrated to cloud", "ClonePrepInternalTemplateFolder", "ClonePrepReplicaVmFolder", "ClonePrepParentVmFolder", "ClonePrepResyncVmFolder", "vm", "Management VMs", "Workloads", "Templates"]

        if not self.vsphere:
          self.connect_vcenter()

        folder_filter_spec = Folder.FilterSpec(type="VIRTUAL_MACHINE")
        folders = self.vsphere.vcenter.Folder.list(folder_filter_spec)
        a = []
        for folder in folders:
          if not folder.name in management_folders:
            a.append({"name": folder.name})
        self.sddc_config["folders"] = a

    def list_contentlibrary(self):
        if not self.vsphere:
          self.connect_vcenter()

        contentlib_ids = self.vsphere.content.Library.list()
        a = []
        for id in contentlib_ids:
          model = self.vsphere.content.Library.get(id)
          t = str(model.type)
          if t == "LOCAL":
            a.append({"name": model.name, "type": t})
          elif t == "SUBSCRIBED":
            a.append({"name": model.name, "type": t, "subscription_url": model.subscription_info.subscription_url, "on_demand": model.subscription_info.on_demand, "automatic_sync_enabled": model.subscription_info.automatic_sync_enabled})
        self.sddc_config["contentlibrary"] = a
        print(a)

    def output_to_s3(self):
        write_json_to_s3("vmc-env", "sddc.json", self.sddc_config)

def lambda_handler(event, context):
    sddc_operations = SDDCConfig()
    sddc_operations.setup()
    sddc_operations.list_sddc()
    sddc_operations.list_vcenter()
    sddc_operations.list_user_resourcepools()
    sddc_operations.list_user_folders()
    sddc_operations.output_to_s3()

def main():
    sddc_operations = SDDCConfig()
    sddc_operations.setup()
    sddc_operations.list_sddc()
    sddc_operations.list_vcenter()
    sddc_operations.list_user_resourcepools()
    sddc_operations.list_user_folders()
    sddc_operations.list_contentlibrary()
#    sddc_operations.output_to_s3()

if __name__ == '__main__':
    main()
