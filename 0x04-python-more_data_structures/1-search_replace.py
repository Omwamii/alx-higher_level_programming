#!/usr/bin/python3
def search_replace(my_list, search, replace):
    '''replaces all occurrences of an element by another in a new list.'''
    if my_list is None:
        return None

    new_list = my_list.copy()
    if len(new_list) == 0:
        return new_list
    try:
        index = new_list.index(search)
    except ValueError:
        return new_list  # no instance found

    while index >= 0:
        new_list.remove(search)
        new_list.insert(index, replace)
        try:
            index = new_list.index(search)
        except ValueError:
            break
    return new_list
