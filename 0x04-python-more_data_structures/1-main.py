#!/usr/bin/python3
search_replace = __import__('1-search_replace').search_replace

my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
new = [2,2,2,2,2,2,2,2]
new_list = search_replace(new, 2, 89)

print(new_list) # new_list
print(new) # my_list

