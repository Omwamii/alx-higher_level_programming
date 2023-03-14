#!/usr/bin/python3
def max_integer(my_list=[]):
    '''finds biggest integer in list'''
    if len(my_list) == 0:
        return None

    biggest = my_list[0]
    for n in my_list:
        if n > biggest:
            biggest = n
    return biggest
