#!/usr/bin/python3
"""
module with locked class
"""


class LockedClass:
    """
    locked class: prevent instances for anything
    but attributes with the name 'first_name'
    """

    __slots__ = ["first_name"]
