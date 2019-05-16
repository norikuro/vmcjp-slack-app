#!/usr/bin/env python

def compare_list_and_dict(ls, dic):
  value_list = []
  key_list = dic.keys()
  and_list = set(key_list) & set(ls)
  for id in and_list:
    value_list.append(dic[id])
#  print(value_list)
