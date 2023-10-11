#!/usr/bin/python3
def common_elements(set_1, set_2):
    newlist = []
    for l in set_1:
        if l in set_2:
            newlist.append(l)

    return (newlist)
