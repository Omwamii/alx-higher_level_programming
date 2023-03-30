#!/usr/bin/python3
""" module with Square class """


class Square:
    """ Square class """
    def __init__(self, size=0):
        """initialize size"""
        self.size = size

    @property
    def size(self):
        """ size getter """
        return self.__size

    @size.setter
    def size(self, size):
        """ size setter """
        if isinstance(size, int) or isinstance(size, float):
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be a number')

    def area(self):
        """ get square area"""
        return self.__size * self.__size

    def __eq__(self, other):
        """ respond to == operator """
        if not isinstance(other, Square):
            # don't compare against unrelated types
            return NotImplemented
        return self.__size == other.__size

    def __lt__(self, other):
        """ respond to < """
        if not isinstance(other, Square):
            return NotImplemented
        return self.__size < other.__size

    def __le__(self, other):
        """ respond to <= """
        if not isinstance(other, Square):
            return NotImplemented
        return self.__size <= other.__size

    def __ne__(self, other):
        """ respond to != """
        if not isinstance(other, Square):
            return NotImplemented
        return self.__size != other.__size

    def __gt__(self, other):
        """ respond to > """
        if not isinstance(other, Square):
            return NotImplemented
        return self.__size > other.__size

    def __ge__(self, other):
        """ respond to >= """
        if not isinstance(other, Square):
            return NotImplemented
        return self.__size >= other.__size
