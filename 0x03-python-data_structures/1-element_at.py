#!/usr/bin/python3
def element_at(my_list, idx):
    ''' retrieves an element from index idx in list '''
    if idx < 0 or idx >= len(my_list):
        return None
    else:
        return my_list[idx]
