#!/usr/bin/python3
"""
module with 'lookup' fn
"""


def lookup(obj):
    """ returns list of available attributes and methods of obj"""
    return list(dir(obj))
