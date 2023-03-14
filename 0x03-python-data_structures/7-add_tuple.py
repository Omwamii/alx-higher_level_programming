#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        while len(tuple_a) < 2:
            tuple_a += (0,)
    if len(tuple_b) < 2:
        while len(tuple_b) < 2:
            tuple_b += (0,)
    add = []
    for i in range(0, 2):
        add.append(tuple_a[i] + tuple_b[i])

    return tuple(add)
