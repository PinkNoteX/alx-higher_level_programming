#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        newlist = list(a_dictionary)
        listlen = len(newlist)
        x = store = value = xst = 0
        while x < listlen:
            value = a_dictionary.get(newlist[x])
            if value > store:
                store = value
                xst = x
            x = x + 1
        return newlist[xst]
    else:
        return None
