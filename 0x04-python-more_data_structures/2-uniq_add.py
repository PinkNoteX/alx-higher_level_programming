#!/usr/bin/python3
def uniq_add(my_list=[]):
    store = 0
    my_list = list(dict.fromkeys(my_list))
    for l in my_list:
        store = store + my_list[l-1]
    return (store)
