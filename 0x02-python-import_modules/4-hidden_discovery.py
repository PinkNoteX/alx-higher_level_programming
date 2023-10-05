#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    ns = dir(hidden_4)
    for n in ns:
        if n[1] != '_':
            print(n)
