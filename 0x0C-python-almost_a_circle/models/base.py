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

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes JSON string rep to a file """
        filename = cls.__name__ + ".json"
        if list_objs is None:
            data = "[]"
        else:
            obj_dicts = []
            for obj in list_objs:
                obj_dicts.append(obj.to_dictionary())  # store dict rep of objs
            data = cls.to_json_string(obj_dicts)  # convert list to json rep
        with open(filename, "w") as f:
            f.write(data)
