#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    '''returns new dictionary with values mult by 2'''
    new_dict = a_dictionary.copy()
    for item in a_dictionary:
        new_dict[item] = a_dictionary[item] * 2

    return new_dict
