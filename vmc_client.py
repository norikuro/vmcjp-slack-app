#!/usr/bin/env python

from vmcutils.fileutils import load_json

def get_vmc_client():
  f = load_json("s3config.json")
  
