#!/usr/bin/python3
""" module with add function """


def add_integer(a, b=98):
    """ adds 2 integers or floats

    Returns: sum of two integers

    Raises: TypeError if any passed value is not an integer
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError('a must be an integer')
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError('b must be an integer')
    else:
        return int(a) + int(b)
