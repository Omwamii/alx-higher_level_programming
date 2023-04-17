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

    def to_json(self, attrs=None):
        """ retrieves dict rep of Student instance """
        if type(attrs) == list:
            new = dict()
            for attr in sorted(attrs):
                try:
                    new[attr] = getattr(self, attr)
                except AttributeError:
                    continue
            return new
        return self.__dict__

    def reload_from_json(self, json):
        """ replaces class __dict__ with passed dict """
        for i, j in json.items():
            setattr(self, i, j)
