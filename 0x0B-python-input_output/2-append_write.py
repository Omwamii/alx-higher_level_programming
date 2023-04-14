#!/usr/bin/python3
"""
module with 'append_write
"""


def append_write(filename="", text=""):
    """ appends string at end of text file / create if not exist """
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
