#!/usr/bin/env python

def replace_strings_in_list(ls, st):
  ls2 = [l.replace(st, "") for l in ls]
  print(ls2)
  return ls2
