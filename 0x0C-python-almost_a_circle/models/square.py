#!/usr/bin/python3
"""
module with 'Square' class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ square class """
    def __init__(self, size, x=0, y=0, id=None):
        """ init vars """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ size getter """
        return self.width

    @size.setter
    def size(self, value):
        """ size setter """
        self.width = value
        self.height = value

    def __str__(self):
        """ override __str__ """
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)
