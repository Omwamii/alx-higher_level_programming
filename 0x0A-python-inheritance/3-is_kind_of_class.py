#!/usr/bin/python3
"""
module with 'is_kind_of_class'
"""


def is_kind_of_class(obj, a_class):
    """ return True if obj is instance or inherits from """
    if isinstance(obj, a_class) or issubclass(type(obj), a_class):
        return True
    return False
