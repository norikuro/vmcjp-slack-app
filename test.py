#!/usr/bin/env python

from vmcutils.metadata import get_members
from vmc_client import get_sddc, get_vsphere

def main():
  sddc = get_sddc("s3config.json")
  vsphere = get_vsphere(sddc)
  print(get_members(sddc))
  print(sddc.to_dict())
  
if __name__ == '__main__':
  main()
