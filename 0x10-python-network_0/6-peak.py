#!/usr/bin/python3
""" module to find a peak in a list
"""


def find_peak(arg_list=None):
    """ fn to find a peak in a list
    """
    if not isinstance(arg_list, list):
        return None
    if len(arg_list) == 0 or len(arg_list) == 1:
        return None  # if only one item, no peak formed
    peak = None
    for index, item in enumerate(arg_list):
        if not isinstance(item, int) and not isinstance(item, float):
            return None  # not a digit
        if index == 0:  # skip first item as peak
            continue
        if peak is None:
            peak = item
        else:
            if peak == item and arg_list[index - 1] == item:
                if peak < arg_list[0]:
                    peak = arg_list[0]
                    break
                else:
                    peak = item
                    break
            elif peak < item:
                peak = item
                if index < len(arg_list) - 1:
                    if arg_list[index + 1] < item:
                        break
    if peak == arg_list[1]:
        if arg_list[0] > peak:
            peak = arg_list[0]
    return peak
