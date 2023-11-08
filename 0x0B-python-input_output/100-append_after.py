#!/usr/bin/python3
""" insert line to a file """


def append_after(filename="", search_string="", new_string=""):
    """ Function """
    aptext = ""
    with open(filename, 'r', encoding='utf-8') as x:
        for r in x:
            aptext += r
            if search_string in r:
                aptext += new_string
        x.close()
    with open(filename, 'w', encoding='utf-8') as x:
        x.write(aptext)
        x.close()
