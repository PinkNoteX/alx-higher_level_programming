#!/usr/bin/python3
""" add all args to a list then save them """
from sys import argv
import json


save_file = __import__('5-save_to_json_file').save_to_json_file
load_file = __import__('6-load_from_json_file').load_from_json_file

my_list = []
ac = len(argv)
try:
    my_list = load_file("add_item.json")
except BaseException:
    pass
for x in range(1, ac):
    my_list.append(argv[x])
save_file(my_list, "add_item.json")
