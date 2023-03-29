#!/usr/bin/python3
""" module with Square class"""


class Square:
    """ Square class definition"""
    def __init__(self, size=0):
        """initialize size"""
        self.size = size

    @property
    def size(self):
        """size getter"""
        return self.__size

    @size.setter
    def size(self, size):
        """size setter"""
        if isinstance(size, int):
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an integer')

    def area(self):
        """gets area"""
        return self.__size ** 2

    def my_print(self):
        """prints square with '#' """
        if self.__size == 0:
            print()
        else:
            for x in range(0, self.__size):
                for i in range(0, self.__size):
                    print("#", end="")
                print()
