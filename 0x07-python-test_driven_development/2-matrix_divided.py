#!/usr/bin/python3


""" div matrix """


def matrix_divided(matrix, div):
    """ divide a matrix """
    sError = 'Each row of the matrix must have the same size'
    lError = 'matrix must be a matrix (list of lists) of integers/floats'

    if type(matrix) is not list:
        raise TypeError(lError)
    for x in range(len(matrix)):
        if x != 0:
            result = x - 1
            if len(matrix[x]) != len(matrix[result]):
                raise TypeError(sError)
    if isinstance(div, int) is False:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    return [[round(x / div, 2) for x in alist] for alist in matrix]
