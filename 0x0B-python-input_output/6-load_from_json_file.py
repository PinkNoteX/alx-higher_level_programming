#!/usr/bin/python3
""" create obj from json file """
import json


def load_from_json_file(filename):
    """ function """
    with open(filename, 'r', encoding="utf-8") as x:
        return json.load(x)
