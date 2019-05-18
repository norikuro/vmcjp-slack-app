#!/usr/bin/env python

def get_config():
  f = json.load(open('s3config.json', 'r'))
  t = read_json_from_s3(f["bucket"], f["token"])
  j = read_json_from_s3(f["bucket"], f["config"])
