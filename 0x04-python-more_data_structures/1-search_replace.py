#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newl = []
    m = x = 0
    mainlen = len(my_list)
    while x < mainlen:
        newl.append(my_list[x])
        x = x + 1
    newlen = len(newl)
    while m < newlen:
        if newl[m] == search:
            newl[m] = replace
        m = m + 1
    return (newl)
