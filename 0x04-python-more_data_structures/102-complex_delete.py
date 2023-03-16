#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    '''deletes keys with certain values'''
    def get_key(val):
        '''gets key of val in dict'''
        for key, val in a_dictionary.items():
            if val == value:
                return key
        return None

    key = get_key(value)
    if key is not None:
        while key is not None:
            del a_dictionary[key]
            key = get_key(value)
        return a_dictionary
    else:
        return a_dictionary
