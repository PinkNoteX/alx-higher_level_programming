#!/usr/bin/python3
""" append a string at the end a text file """


def append_write(filename="", text=""):
    """ append string """
    with open(filename, 'a+', encoding='utf-8') as x:
        afile = x.write(text)
        x.close()
        return afile
