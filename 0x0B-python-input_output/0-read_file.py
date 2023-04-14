#!/usr/bin/python3
"""
module with 'read_file'
"""


def read_file(filename=""):
    """ reads a text file and print content """
    with open(filename, mode="r", encoding="utf-8") as f:
        print(f.read(), end="")
