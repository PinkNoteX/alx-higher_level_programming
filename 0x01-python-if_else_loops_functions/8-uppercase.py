#!/usr/bin/python3
def uppercase(str):
    x = 0
    y = a
    length = len(str)
    while x < length + 1:
        if x > 97:
            y = chr(ord(str[x]) - 32)
        print("{}".format(y), end="")
    print("/n")
