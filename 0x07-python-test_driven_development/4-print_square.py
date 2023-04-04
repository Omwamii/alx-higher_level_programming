#!/usr/bin/python3
""" module with 'print_square function """


def print_square(size):
    """
    prints square with '#'
    Raises: TypeError: size is not int
            ValueError: size is < 0
            TypeError: size is float & less than 0
    """
    if isinstance(size, float) and size < 0:
        raise TypeError('size must be an integer')
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')

    for side in range(0, size):
        for w in range(0, size):
            print("#", end="")
        print()
