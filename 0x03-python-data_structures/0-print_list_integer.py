#!/usr/bin/python3
def print_list_integer(my_list=[]):
    i = 0
    indlen = len(my_list)
    while i < indlen:
        print("{:d}".format(my_list[i]))
        i = i + 1
