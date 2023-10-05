#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv
    argsc = len(args)
    z = 1
    thesum = 0
    if argsc == 1:
        print("0")
    else:
        while z < argsc:
            thesum = thesum + int(args[z])
            z = z + 1
        print("{}".format(thesum))
