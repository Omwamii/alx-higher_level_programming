#!/usr/bin/python3
"""
module with 'matrix_mul'
"""


def matrix_mul(m_a, m_b):
    """ matrix multipication """
    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')
    if not isinstance(m_b, list):
        raise TypeError('m_b must be a list')
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    for item in m_a:
        if not isinstance(item, list):
            raise TypeError('m_a must be a list of lists')
        for b in item:
            if not isinstance(b, int) and not isinstance(b, float):
                raise TypeError('m_a should contain only integers or floats')
        size = len(m_a[0])
        if len(item) != size:
            raise TypeError('each row of m_a must be of the same size')

    for item in m_b:
        if not isinstance(item, list):
            raise TypeError('m_b must be a list of lists')
        for b in item:
            if not isinstance(b, int) and not isinstance(b, float):
                raise TypeError('m_b should contain only integers or floats')
            size = len(m_b[0])
            if len(item) != size:
                raise TypeError('each row of m_b must be of the same size')

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    mul = []
    for i in range(0, len(m_a)):
        tmp = []
        for j in range(0, len(m_b[0])):
            res = 0
            for k in range(0, len(m_a[0])):
                res += m_a[i][k] * m_b[k][j]
            tmp.append(res)
        mul.append(tmp)
    return mul
