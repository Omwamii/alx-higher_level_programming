#!/usr/bin/python3
"""
module with 'Square' class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square class"""
    def __init__(self, size):
        """ initialize size """
        self.integer_validator("size", size)
        super().__init__(size, size)  # set l & w as size
        self.__size = size
