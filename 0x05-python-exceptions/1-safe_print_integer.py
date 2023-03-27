#!/usr/bin/python3
def safe_print_integer(value):
    ''' prints an integer with format'''
    try:
        print("{:d}".format(value))
    except ValueError:
        return False
    else:
        return True