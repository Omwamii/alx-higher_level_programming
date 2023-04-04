#!/usr/bin/python3
""" module with text_indentation fn"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each of chars:
                                - '.' '?' ':'
    Raises: TypeError: text is not string
    * No space at the beginning or end of each printed line
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    for item in text:
        if item == '.' or item == '?' or item == ':':
            print(item, end="")
            print()
            print()
        else:
            print(item, end="")
