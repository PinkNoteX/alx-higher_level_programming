#!/usr/bin/python3
x = 0
while x < 100:
    if x == 99:
        print("{}".format(x),end="")
    else:
        print("{}".format(x),end=", ")
    x = x + 1
