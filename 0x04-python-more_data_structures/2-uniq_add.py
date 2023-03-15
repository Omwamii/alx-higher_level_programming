#!/usr/bin/python3
def uniq_add(my_list=[]):
    ''' adds all unique integers in a list'''
    add = set(my_list)
    result = 0
    for n in add:
        result += n

    return result
