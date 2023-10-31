#!/usr/bin/python3


"""nqueen solver"""


def killcheck(aqueen, n_queen):
    """ check if queens can kill each other """
    for x in range(n_queen):
        if aqueen[x] == aqueen[n_queen]:
            return False
        if abs(aqueen[x] - aqueen[n_queen]) == abs(x - n_queen):
            return False
    return True


def printer(aqueen, n_queen):
    """printer"""
    results = []

    for x in range(n_queen):
        results.append([x, aqueen[x]])
    print(results)


def Queen(aqueen, n_queen):
    """backtracker"""
    if n_queen == len(aqueen):
        printer(aqueen, n_queen)
        return
    aqueen[n_queen] = -1
    while(aqueen[n_queen] < len(aqueen) - 1):
        aqueen[n_queen] += 1
        if killcheck(aqueen, n_queen) is True:
            if n_queen < len(aqueen):
                Queen(aqueen, n_queen + 1)


def dobacktrack(s):
    """backtracker"""
    aqueen = [-1 for x in range(s)]
    Queen(aqueen, 0)


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 2 or len(sys.argv) == 1:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    s = int(sys.argv[1])
    if s < 4:
        print("N must be at least 4")
        sys.exit(1)
    dobacktrack(s)
