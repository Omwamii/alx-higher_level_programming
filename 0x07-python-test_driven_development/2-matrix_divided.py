#!/usr/bin/python3
""" module :divides all elements of matrix"""


def matrix_divided(matrix, div):
    """
    divides elements of matrix by div
    Raises: TypeError (matrix has any other type except int or float)
            TypeError (rows dont have same size)
            TypeError (div is not int or float)
            ZeroDivisionError (div is 0)

    Returns: new list with all divided elements
    """
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    new_mat = []
    row_len = len(matrix[0])
    type_err = "matrix must be a matrix (list of lists) of integers/floats"
    for row in matrix:
        if len(row) != row_len:  # every row len should be equal to first
            raise TypeError('Each row of the matrix must have the same size')
        rw = []
        for i in range(0, len(row)):
            if not isinstance(row[i], float) and not isinstance(row[i], int):
                raise TypeError(type_err)
            val = row[i] / div
            val = round(val, 2)
            rw.append(val)
        new_mat.append(rw)
    return new_mat
