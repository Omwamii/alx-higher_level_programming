#!/usr/bin/python3
"""
module with 'class_to_json'
"""


def class_to_json(obj):
    """ return dict description of obj """
    return obj.__dict__
