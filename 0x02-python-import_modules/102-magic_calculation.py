#!/usr/bin/python3
from magic_calculation_102 import add, sub


def some_function(a, b):
    if a < b:
        c = add(a, b)

        for i in range(4, 6):
            c = add(c, i)

        return c

    return sub(a, b)
