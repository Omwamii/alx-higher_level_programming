#!/usr/bin/python3
"""
module with 'save_to_json'
"""
import json


def save_to_json_file(my_obj, filename):
    """ writes an object to text file with JSON rep"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
