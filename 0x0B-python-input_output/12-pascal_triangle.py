#!/usr/bin/python3
""" pascal triangle """


def pascal_triangle(n):
    """ the function """
    mat = []
    for x in range(1, n+1):
        mat.append([1] * x)
    for y in range(2, n):
        r = mat[y]
        pr = mat[y-1]
        for m in range(1, len(r) - 1):
            r[m] = pr[m - 1] + pr[m]
    return mat
