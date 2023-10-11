#!/usr/bin/python3
def common_elements(set_1, set_2):
    newlist = []
    flen = len(set_1)
    slen = len(set_2)
    x = r = 0
    while r < flen:
        while x < slen:
            if set_1[r] == set_2[x]:
                newlist.append(set_1[r])
            x = x + 1
        r = r + 1
    return (newlist)
