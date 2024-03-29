#!/usr/bin/python3
""" module with square class definition """


class Square:
    """ square class definition """
    def __init__(self, size=0):
        """initialize size"""
        if isinstance(size, int):
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an integer')
