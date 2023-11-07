#!/usr/bin/python3
""" write to file """


def write_file(filename="", text=""):
    """ write to file """
    with open(filename, 'w', encoding='utf-8') as x:
        wfile = x.write(text)
        x.close()
        return wfile
