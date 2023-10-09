#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    inlen = len(my_list) - 1
    x = 0
    newlist = [None] * (inlen + 1)
    while x <= inlen:
        if my_list[x] % 2 == 0:
            newlist[x] = True
        else:
            newlist[x] = False
        x = x + 1
    return newlist
