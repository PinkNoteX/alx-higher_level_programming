#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newdic = a_dictionary.copy()
    newlist = list(newdic)
    x = 0
    listlen = len(newlist)
    while x < listlen:
        newdic[newlist[x]] = newdic.get(newlist[x]) * 2
        x = x + 1
    return newdic
