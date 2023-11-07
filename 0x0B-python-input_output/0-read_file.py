#!/usr/bin/python3
""" read file and print it """


def read_file(filename=""):
    """ Read file """
    with open(filename, 'r', encoding='utf-8') as x:
        for m in x:
            print(m, end='')
    x.close()
