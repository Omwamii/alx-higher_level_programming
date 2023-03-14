#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    ''' prints all integers of list in reverse '''
    if len(my_list) == 0:
        return print()
    my_list.reverse()
    for n in my_list:
        print("{:d}".format(n))
