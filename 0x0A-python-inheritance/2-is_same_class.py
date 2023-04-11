#!/usr/bin/python3
""" module with 'is_same_class' fn"""


def is_same_class(obj, a_class):
    """ return True if object is exactly an instance else false"""
    if type(obj) == a_class:
        return True
    return False
