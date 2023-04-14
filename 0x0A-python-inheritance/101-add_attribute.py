#!/usr/bin/python3
"""
module 'add_attribute'
"""


def add_attribute(obj, name, value):
    """ sets attribute in an object """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
