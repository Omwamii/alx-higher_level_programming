#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    '''returns set of elements present in only one set'''
    diff = list(set_1.difference(set_2))
    diff += list(set_2.difference(set_1))
    return sorted(diff)
