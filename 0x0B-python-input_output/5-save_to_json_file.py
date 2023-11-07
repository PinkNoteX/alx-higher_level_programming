#!/usr/bin/python3
""" write obj to text file using Json """
import json


def save_to_json_file(my_obj, filename):
    """ function """
    with open(filename, 'w', encoding="utf-8") as x:
        json.dump(my_obj, x)
