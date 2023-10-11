#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    newlist = list(a_dictionary.keys())
    x = 0
    listlen = len(newlist)
    while x < listlen:
        if newlist[x] == key:
            a_dictionary.pop(key)
        x = x + 1
    return a_dictionary
