#!/usr/bin/python3


""" not so empty square"""


def print_square(size):
    """print a square"""
    if isinstance(size, int) is False:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for x in range(0, size):
        print('#' * size)
