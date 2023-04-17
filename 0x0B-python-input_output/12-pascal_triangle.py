#!/usr/bin/python3
"""
module with 'pascal_triangle'
"""


def pascal_triangle(n):
    """ returns list representatio of the pascal's
    triangle of n
    """
    if n <= 0:
        return [[]]

    pascal = []
    for i in range(n):
        row = []
        for b in range(i+1):
            if b == 0 or b == i:
                row.append(1)
            else:
                num = pascal[i - 1][b - 1] + pascal[i - 1][b]
                row.append(num)
        pascal.append(row)

    return pascal
