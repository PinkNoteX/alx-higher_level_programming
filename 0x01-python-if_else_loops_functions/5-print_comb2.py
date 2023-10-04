#!/usr/bin/python3
x = 0
while x < 100:
    if x == 99:
        print("{}".format(x), end="\n")
    else:
        print("{:02}".format(x), end=", ")
    x = x + 1
