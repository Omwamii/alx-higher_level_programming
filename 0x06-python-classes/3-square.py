#!/usr/bin/python3
""" module with Square class"""


class Square:
    """ Square class"""
    def __init__(self, size=0):
        """initialize size variable"""
        if isinstance(size, int):
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an integer')

    def area(self):
        """find area of square"""
        return self.__size ** 2
