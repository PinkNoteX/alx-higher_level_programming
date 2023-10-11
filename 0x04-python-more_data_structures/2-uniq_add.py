#!/usr/bin/python3
def uniq_add(my_list=[]):
    newlist = []
    store = m = r = 0
    mainlen = len(my_list)
    while r < mainlen:
        newlist.append(my_list[r])
        r = r + 1
    newlist = list(dict.fromkeys(newlist))
    newlen = len(newlist)
    while m < newlen:
        store = store + newlist[m]
        m = m + 1
    return (store)
