#!/usr/bin/python3
def search_replace(my_list, search, replace):
    '''replaces all occurrences of an element by another in a new list.'''
    if my_list is None or len(my_list) == 0:
        return my_list
    new_list = my_list.copy()
    index = new_list.index(search)

    while index:
        new_list.remove(search)
        new_list.insert(index, replace)
        try:
            index = new_list.index(search)
        except ValueError:
            break
    return new_list
