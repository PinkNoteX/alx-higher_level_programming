#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    t1len = len(tuple_a)
    t2len = len(tuple_b)
    c = (0, 0)
    if t1len == 1 and t2len == 1:
        c = (tuple_a[0] + tuple_b[0], 0)
        return c
    elif t1len == 2 and t2len == 2:
        c = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
        return c
    elif t1len == 1 and t2len == 2:
        c = (tuple_a[0] + tuple_b[0], tuple_b[1])
        return c
    elif t1len == 2 and t2len == 1:
        c = (tuple_a[0] + tuple_b[0], tuple_a[1])
        return c
    elif t1len != 0 and t2len == 0:
        c = tuple_a[:]
        return c
    elif t1len == 0 and t2len != 0:
        c = tuple_b[:]
        return c
    elif t1len == 0 and t2len == 0:
        return c
    else:
        c = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
        return c
