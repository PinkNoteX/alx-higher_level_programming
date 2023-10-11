#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    newlist = list(a_dictionary.keys())
    for r in newlist:
        if a_dictionary.get(r) == value:
            del a_dictionary[r]
    return a_dictionary
