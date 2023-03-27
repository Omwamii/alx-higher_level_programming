#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    ''' prints an integer '''
    try:
        print("{:d}".format(value))
    except ValueError as val:
        print(f"Exception: {val}", file=sys.stderr)
        return False
    else:
        return True
