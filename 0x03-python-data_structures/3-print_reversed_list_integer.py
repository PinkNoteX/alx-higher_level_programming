#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    inlen = len(my_list)
    x = inlen
    while x >= 0:
        print("{:d}".format(my_list[x]))
        x = x - 1
