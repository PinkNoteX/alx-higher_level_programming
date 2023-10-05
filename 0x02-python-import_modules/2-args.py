#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv
    argscount = len(args)
    x = 1
    if argscount == 2:
        print("1 argument:")
        while x < argscount:
            print("{}: {}".format(x, args[x]))
            x = x + 1
    elif argscount < 2:
        print("0 arguments.")
    else:
        print("{} arguments:".format(argscount - 1))
        while x < argscount:
            print("{}: {}".format(x, args[x]))
            x = x + 1
