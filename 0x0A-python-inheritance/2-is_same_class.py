#!/usr/bin/python3
""" return true or false """
def is_same_class(obj, a_class):
    return issubclass(a_class, type(obj))
