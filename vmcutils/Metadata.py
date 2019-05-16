#!/usr/bin/env python
import inspect

def get_members(obj):
  for x in inspect.getmembers(obj, inspect.ismethod):
    print x[0]
