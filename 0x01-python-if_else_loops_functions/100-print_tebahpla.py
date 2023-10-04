#!/usr/bin/python3
r = 25
rev = 0
while r >= 0 and r < 26:
    rev = r + ord('A')
    if r % 2 == 1:
        rev = rev + 32
    print("{}".format(chr(rev)), end='')
    r = r - 1
