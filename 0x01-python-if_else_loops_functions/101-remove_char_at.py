#!/usr/bin/python3
def remove_char_at(str, n):

    string = str

    if n < 0 or n >= len(str):  # out of range
        return string

    return string[:n] + string[n+1:]
