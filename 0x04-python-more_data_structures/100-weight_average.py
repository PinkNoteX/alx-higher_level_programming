#!/usr/bin/pyhton3
def weight_average(my_list=[]):
    listlen = len(my_list)
    x = store1 = store2 = 0
    if listlen == 0:
        return 0
    while x < listlen:
        store2 = store2 + my_list[x][1]
        store1 = store1 + (my_list[x][0] * my_list[x][1])
        x += 1
    return store1 / store2
