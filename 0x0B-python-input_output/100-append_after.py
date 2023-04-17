#!/usr/bin/python3
"""
module with 'append_after'
"""


def append_after(filename="", search_string="", new_string=""):
    """ inserts line of text to a file after occurence of certain string"""
    with open(filename, mode="r", encoding="utf-8") as f:
        file_data = f.readlines()

    indices = []
    for i, line in enumerate(file_data):
        if search_string in line:
            indices.append(i + 1)

    for index in reversed(indices):
        file_data.insert(index, new_string)

    with open(filename, mode="w", encoding="utf-8") as f:
        f.writelines(file_data)
