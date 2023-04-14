#!/usr/bin/python3
"""
module with 'Student class'
"""


class Student:
    """ student class """
    def __init__(self, first_name, last_name, age):
        """ init variables"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ retrieves dict rep of Student instance """
        return self.__dict__
