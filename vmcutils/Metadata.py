#!/usr/bin/env python
import inspect

def get_members(obj):
  for x in dir(obj):
    print x, ':', type(eval("obj."+x))
#  for x in inspect.getmembers(obj, inspect.ismethod):
#    print x[0]
