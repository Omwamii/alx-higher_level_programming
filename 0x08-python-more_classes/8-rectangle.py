#!/usr/bin/python3
""" module with defined Rectangle class"""


class Rectangle:
    """ Rectangle class """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ initialize variables"""
        type(self).number_of_instances += 1
        self.height = height
        self.width = width

    def __del__(self):
        """ define destructor """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

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
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """ define printable """
        rect = []
        count = 0
        if self.__width == 0 or self.__height == 0:
            return ""
        for h in range(0, self.__height):
            count += 1
            for w in range(0, self.__width):
                rect.append(str(self.print_symbol))
            if count < self.__height:
                rect.append("\n")
        return "".join(rect)

    def __repr__(self):
        """ define __repr__ """
        return f"Rectangle({self.__width}, {self.__height})"

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ return rect with biggest area """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
            return
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
            return
        if rect_1.area() > rect_2.area():
            return rect_1
        if rect_1.area() < rect_2.area():
            return rect_2
        else:
            return rect_1
