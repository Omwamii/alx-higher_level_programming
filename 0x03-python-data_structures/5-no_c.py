#!/usr/bin/python3
def no_c(my_string):
    '''  removes all characters c and C from a string '''
    string = my_string.translate({ord(i): None for i in "cC"})
    return string
