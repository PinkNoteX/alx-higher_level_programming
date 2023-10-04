#!/usr/bin/python3
x = 0
y = 0
while x < 10:
    while y < 10:
        if x == 8 and y == 9:
            print("{}{}".format(x, y), end="\n")
        elif x != y:
            print("{}{}".format(x, y), end=", ")
        y = y + 1
    x = x + 1
    y = x
