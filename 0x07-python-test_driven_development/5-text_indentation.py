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
    for i in range(0, len(text)):
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            print(text[i])
            print()
            setl = 1
        else:
            if text[i] == " " and setl == 1:
                continue
            print(text[i], end="")
            setl = 0
