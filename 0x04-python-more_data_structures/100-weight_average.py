#!/usr/bin/python3
def weight_average(my_list=[]):
    '''returns weighted average of all integers in tuple'''
    mult_sum ,weight_sum = 0, 0
    for item in my_list:
        mult_sum += (item[0] * item[1])
        weight_sum += item[1]

    return mult_sum / weight_sum
