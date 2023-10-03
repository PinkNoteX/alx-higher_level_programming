#!/usr/bin/python3
def uppercase(str):
    x = 0
    length = len(str)
    while x < length:
       str[x] = chr(ord(str[x]) - 32)
       x = x + 1
    print("{}".format(str), end="\n")
