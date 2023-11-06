#!/usr/bin/python3
"""check if obj is an instance of a class that is inherited"""


def inherits_from(obj, a_class):
    """ returns true or false """
    if type(obj) == a_class:
        return (False)
    return isinstance(obj, a_class)
