#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    '''prints the first x elements of a list, only integers'''
    i = 0
    b = 0
    while i < x:
        try:
            print("{:d}".format(my_list[i]), end="")
        except (ValueError, TypeError):
            print("", end="")
            i += 1
            b += 1
        else:
            i += 1
    print()
    return i - b
