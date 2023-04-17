#!/usr/bin/python3
"""
base class module
"""
import json


class Base:
    """ 'Base' class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns JSON string rep of arg """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)
