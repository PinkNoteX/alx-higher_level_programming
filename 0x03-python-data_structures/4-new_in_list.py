#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    inlen = len(my_list)
    copy_list = my_list[:]
    if idx < 0 or idx >= inlen:
        return my_list
    else:
        copy_list[idx] = element
        return copy_list
