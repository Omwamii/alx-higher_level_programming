#!/usr/bin/python3
"""
module with 'BaseGeometry'
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class """
    def __init__(self, width, height):
        """ initialize varibles
        args:
            width: width of new rectangle
            height: height of new rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
