#!/usr/bin/python3
""" to string """


import json


def from_json_string(my_str):
    """ return string """
    return json.loads(my_str)
