#!/usr/bin/env python

import argparse
import json

from datetime import datetime
from collections import OrderedDict
from six.moves.urllib import parse
from vmware.vapi.vmc.client import create_vmc_client
from vmware.vapi.vsphere.client import create_vsphere_client
from vmcutils.s3 import write_json_to_s3, read_json_from_s3


class ListSDDCs(object):
    def __init__(self):
        f = json.load(open('s3config.json', 'r'))
        j = read_json_from_s3(f["bucket"], f["file"])

        self.refresh_token = j["account"]["token"]
        self.org_id = j["org"]["id"]

        self.sddc_config = OrderedDict()
        self.sddc_config["updated"] = datetime.now().strftime("%Y/%m/%d")

        # Login to VMware Cloud on AWS
        self.vmc_client = create_vmc_client(self.refresh_token)

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
            a.append({"id": sddc.id, "name": sddc.name, "vmc_version": sddc.resource_config.sddc_manifest.vmc_version})
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
        self.connect_vcenter()
        rps = self.vsphere.vcenter.ResourcePool.list(filter=None)
        a = []
        for rp in rps:
          if rp.name != "Resources" and rp.name != "Mgmt-ResourcePool" and rp.name != "Compute-ResourcePool":
            a.append({"name": rp.name})
        self.sddc_config["resourcepools"] = a

#    def list_user_folders(self):

    def output_to_s3(self):
        write_json_to_s3("vmc-env", "sddc.json", self.sddc_config)

def lambda_handler(event, context):
    sddc_operations = ListSDDCs()
    sddc_operations.setup()
    sddc_operations.list_sddc()
    sddc_operations.list_vcenter()
    sddc_operations.list_user_resourcepools()
    sddc_operations.output_to_s3()

def main():
    sddc_operations = ListSDDCs()
    sddc_operations.setup()
    sddc_operations.list_sddc()
    sddc_operations.list_vcenter()
    sddc_operations.list_user_resourcepools()
    sddc_operations.output_to_s3()

if __name__ == '__main__':
    main()
