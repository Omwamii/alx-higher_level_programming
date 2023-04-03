#!/usr/bin/python3
""" module with defined Rectangle class"""


class Rectangle:
    """ Rectangle class """
    def __init__(self, width=0, height=0):
        """ initialize variables"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if isinstance(value, int):
            if value < 0:
                raise ValueError('width must be >= 0')
            else:
                self.__width = value
        else:
            raise TypeError('width must be an integer')

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if isinstance(value, int):
            if value < 0:
                raise ValueError('height must be >= 0')
            else:
                self.__height = value
        else:
            raise TypeError('height must be an integer')

    def area(self):
        """ get area """
        return self.__width * self.__height

    def perimeter(self):
        """ get rect perimeter """
        return 2 * (self.__width + self.__height)
