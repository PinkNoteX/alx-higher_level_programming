#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    newlist = list(a_dictionary.keys())
    sortedlist = sorted(newlist)
    listlen = len(sortedlist)
    x = 0
    while x < listlen:
        print("{}: {}".format(sortedlist[x], a_dictionary.get(sortedlist[x])))
        x = x + 1
