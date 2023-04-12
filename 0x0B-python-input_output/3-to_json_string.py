#!/usr/bin/python3
"""
module with 'to_json-string'
"""
import json


def to_json_string(my_obj):
    """ returns JSON rep of an object """
    return json.dumps(my_obj)
