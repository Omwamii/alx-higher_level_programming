#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    add = []
    for row in matrix:
        for x in row:
            add.append(x**2)
        new.append(add)
        add = []
    return new
