#!/usr/bin/python3
""" module to find a peak in a list
"""


def find_peak(arg_list=None):
    """ fn to find a peak in a list
    """
    if len(arg_list) == 0 or len(arg_list) == 1:
        return None  # if only one item, no peak formed
    peak = None
    for index, item in enumerate(arg_list):
        if index == 0:
            if item > arg_list[index + 1]:
                peak = item
            else:
                peak = arg_list[index + 1]
        elif index == len(arg_list) - 1:
            if item > peak:
                peak = item  # last point is highest
        else:
            if item > arg_list[index - 1] and item > arg_list[index + 1]:
                return item  # peak found
            if item == arg_list[index - 1]:
                break  # plain detected __
    return peak
