#!/usr/bin/python3
def max_integer(my_list=[]):
    bigm = 0
    inlen = len(my_list)
    x = inlen - 1
    if inlen == 0:
        return None
    while 0 <= x:
        if my_list[x] > bigm:
            bigm = my_list[x]
        x = x - 1
    return bigm
