#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_set = set_1
    new_set.symmetric_difference_update(set_2)
    newlist = list(new_set)
    return (newlist)
