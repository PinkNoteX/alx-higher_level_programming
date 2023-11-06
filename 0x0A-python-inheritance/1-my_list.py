#!/usr/bin/python3
"""mylist"""


class MyList(list):
    """print sorted list"""
    def print_sorted(self):
        print(sorted(self))
