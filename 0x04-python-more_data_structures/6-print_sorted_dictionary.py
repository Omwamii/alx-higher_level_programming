#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    '''prints a dictionary by ordered keys'''
    for item in sorted(a_dictionary):
        print("{}: {}".format(item, a_dictionary[item]))
