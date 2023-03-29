#!/usr/bin/python3
""" module with Square class"""


class Square:
    """Square class definition"""
    def __init__(self, size=0, position=(0, 0)):
        """ initialize variables """
        self.size = size
        self.position = position

    @property
    def size(self):
        """get size"""
        return self.__size

    @size.setter
    def size(self, value):
        """set size"""
        if isinstance(value, int):
            if value < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = value
        else:
            raise TypeError('size must be an integer')

    @property
    def position(self):
        """position getter"""
        return self.__position

    @position.setter
    def position(self, value):
        """position setter"""
        position_err = "position must be a tuple of 2 positive numbers"
        if isinstance(value, tuple) and len(value) == 2:
            if value[0] >= 0 and value[1] >= 0:
                self.__position = value
            else:
                raise TypeError(position_err)
        else:
            raise TypeError(position_err)

    def area(self):
        """gets area of square"""
        return self.__size ** 2

    def my_print(self):
        """prints square with '#' and spaces"""
        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__position[1]):
                print("")
            for x in range(0, self.__size):
                for b in range(0, self.__position[0]):
                    print(" ", end="")
                for i in range(0, self.__size):
                    print("#", end="")
                print()
