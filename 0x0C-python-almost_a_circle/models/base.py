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

    @staticmethod
    def from_json_string(json_string):
        """ return list of the JSON string rep """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes set """
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        elif cls.__name__ == "Square":
            new = cls(1)
        new.update(**dictionary)
        return new
