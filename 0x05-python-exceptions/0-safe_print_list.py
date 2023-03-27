#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    ''' prints x elements of a list.'''
    i = 0
    while i < x:
        try:
            print(my_list[i], end="")
        except IndexError:
            print()
            return i
        else:
            i += 1
    print()
    return x
