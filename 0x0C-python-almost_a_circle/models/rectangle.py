#!/usr/bin/python3
"""
module with 'rectangle' class
"""
from models.base import Base


class Rectangle(Base):
    """ 'Rectangle' class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ initialize vars """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ x getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ x setter"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ y getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ y setter """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ returns area of rectangle """
        return self.__width * self.__height

    def display(self):
        """ prints rectangle with '#' character """
        for n in range(self.__y):
            print()
        for length in range(self.__height):
            for n in range(self.__x):
                print(" ", end='')
            for width in range(self.__width):
                print("#", end='')
            print()

    def __str__(self):
        """ return custom representation """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """ assign argument to each attribute """
        if args and len(args) != 0:
            count = 0
            for arg in args:
                if count == 0:  # first
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif count == 1:
                    self.width = arg
                elif count == 2:
                    self.height = arg
                elif count == 3:
                    self.x = arg
                elif count == 4:
                    self.y = arg
                count += 1
        else:
            if kwargs and len(kwargs) != 0:
                for key, value in kwargs.items():
                    if hasattr(self, key):
                        setattr(self, key, value)

    def to_dictionary(self):
        """ returns dict representation of class """
        my_dict = {'x': self.x, 'y': self.y, 'height': self.height,
                   'width': self.width}
        return my_dict
