#!/usr/bin/python3
"""
module with 'load_from_json'
"""


def load_from_json_file(filename):
    """ creates an object from JSON file """
    with open(filename) as f:
        return json.load(f)
