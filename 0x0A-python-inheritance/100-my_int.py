#!/usr/bin/python3
"""
class 'MyInt' module
"""


class MyInt(int):
    """ rebel class: inverts == and != """
    def __init__(self, value):
        """ initialize vars """
        self.value = value

    def __eq__(self, other):
        """ define eq for MyInt """
        return self.value != other

    def __ne__(self, other):
        """ define != for MyInt"""
        return self.value == other
