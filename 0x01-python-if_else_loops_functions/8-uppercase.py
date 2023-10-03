#!/usr/bin/python3
def uppercase(str):
    x = 0
    y = 0
    length = len(str)
    while x < length + 1:
        if ord(str[x]) > 97:
            y = chr(ord(str[x]) - 32)
        print("{}".format(y), end="")
        x = x + 1
    print("/n")
