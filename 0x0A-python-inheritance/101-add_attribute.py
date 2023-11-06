#!/usr/bin/python3
""" add attribute """


def add_attribute(obj, attr, value):
    """ add attr """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)

