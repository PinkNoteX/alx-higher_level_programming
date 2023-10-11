#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        return([[n*n for n in r] for r in matrix])
