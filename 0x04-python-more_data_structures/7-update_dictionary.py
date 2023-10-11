#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    newlist = list(a_dictionary)
    x = 0
    listlen = len(newlist)
    while x < listlen:
        if newlist[x] == key:
            a_dictionary[newlist[x]] = value
        x = x + 1
    a_dictionary[key] = value
    return (a_dictionary)
