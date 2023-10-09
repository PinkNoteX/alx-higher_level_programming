#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for el in matrix:
        for r in el:
            print("{:d}".format(r), end=" ")
            if r == el[len(el) - 1]:
                print("", end="")
        print("")
