#!/usr/bin/env python

import json

def load_json(filename):
  return json.load(open(filename, 'r'))
