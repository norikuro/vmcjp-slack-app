#!/usr/bin/env python

def compare_list_and_dict(ls, dic):
  key_list = dic.keys()
  and_list = set(key_list) & set(ls)
  return [dic[id] for id in and_list]
