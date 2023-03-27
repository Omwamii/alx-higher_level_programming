#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    '''divides element by element in list'''
    result = 0
    i = 0
    new_list = [] * list_length

    while i < list_length:
        try:
            result = my_list_1[i] / my_list_2[i]
        except TypeError:
            result = 0
            print("wrong type")
        except ZeroDivisionError:
            result = 0
            print("division by 0")
        except IndexError:
            result = 0
            print("out of range")
        finally:
            new_list.append(result)
            i += 1
    return new_list
