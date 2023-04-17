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

    def update(self, *args, **kwargs):
        """ assigns attributes """
        if args and len(args) != 0:
            for c, i in enumerate(args):
                if c == 0:
                    if i is None:
                        super().__init__(self.id, self.size, self.x, self.y)
                    else:
                        self.id = i
                elif c == 1:
                    self.size = i
                elif c == 2:
                    self.x = i
                elif c == 3:
                    self.y = i

        else:
            if kwargs and len(kwargs) != 0:
                for key, value in kwargs.items():
                    if hasattr(self, key):
                        setattr(self, key, value)

    def to_dictionary(self):
        """ return dictionary rep of class """
        my_dict = {'id': self.id, 'x': self.x, 'size': self.size,
                    'y': self.y}
        return my_dict
