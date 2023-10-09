#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    inlen = len(my_list) - 1
    while inlen >= 0:
        print("{:d}".format(my_list[inlen]))
        inlen = inlen - 1
