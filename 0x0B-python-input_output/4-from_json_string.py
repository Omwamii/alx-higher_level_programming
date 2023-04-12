#!/usr/bin/python3
"""
module with 'from_json_string'
"""
import json


def from_json_string(my_str):
    """ returns object rep by json"""
    return json.loads(my_str)
