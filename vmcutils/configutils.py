#!/usr/bin/env python

def get_config():
  t = read_json_from_s3(f["bucket"], f["token"])
  j = read_json_from_s3(f["bucket"], f["config"])
