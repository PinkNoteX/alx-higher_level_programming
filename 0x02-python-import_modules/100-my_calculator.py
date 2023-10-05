#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    ar = sys.argv
    argscount = len(ar)
    ope = ['+', '-', '/', '*']
    r = 1
    if argscount != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(ar[1])
        b = int(ar[3])
        if ar[2] in ope:
            if ar[2] == '+':
                print("{} + {} = {}".format(ar[1], ar[3], add(a, b)))
            elif ar[2] == '-':
                print("{} - {} = {}".format(ar[1], ar[3], sub(a, b)))
            elif ar[2] == '/':
                print("{} / {} = {}".format(ar[1], ar[3], div(a, b)))
            elif ar[2] == '*':
                print("{} * {} = {}".format(ar[1], ar[3], mul(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
