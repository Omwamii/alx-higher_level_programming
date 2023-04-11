#!/usr/bin/python3
"""
module with 'inherits_from'
"""


def inherits_from(obj, a_class):
    """ return true if obj inherits from a_class"""
    if issubclass(type(obj), a_class):
        return True
    return False
