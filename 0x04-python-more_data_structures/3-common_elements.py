#!/usr/bin/python3
def common_elements(set_1, set_2):
    newlist = []

    for la in set_1:
        if la in set_2:
            newlist.append(la)

    return newlist
