#!/usr/bin/python3
def max_integer(my_list=[]):
    inlen = len(my_list)
    x = inlen - 1
    if inlen == 0:
        return None
    bigm = my_list[0]
    while 0 <= x:
        if my_list[x] > bigm:
            bigm = my_list[x]
        x = x - 1
    return bigm
