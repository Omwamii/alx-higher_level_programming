#!/usr/bin/python3
"""
module with 'MyList' class
"""


class MyList(list):
    """ 'MyList' class """
    def print_sorted(self):
        """ prints list in ascending order """
        self.sort()
        print(self)
