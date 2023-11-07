#!/usr/bin/python3
""" return dictionary for json """


def class_to_json(obj):
    """ function """
    dec = {}
    if hasattr(obj, "__dict__"):
        dec = obj.__dict__.copy()
    return dec
