#!/usr/bin/python3
def roman_to_int(roman_string):
    ''' converts roman num to integer '''

    roman = {1: "I", 2: "II", 3: "III", 4: "IV", 5: "V",
             6: "VI", 7: "VII", 8: "VIII", 9: "IX", 10: "X",
             20: "XX", 30: "XXX", 40: "XL", 50: "L", 60: "LX",
             70: "LXX", 80: "LXXX", 90: "XC", 100: "C", 200: "CC",
             300: "CCC", 400: "CD", 500: "D", 600: "DC", 700: "DCC",
             800: "DCCC", 900: "CM", 1000: "M", 2000: "MM", 3000: "MMM"
             }

    def get_key(val):
        '''Get key value in dict'''
        for key, value in roman.items():
            if val == value:
                return key
    try:
        size = len(roman_string)
    except TypeError:
        return 0
    integer = 0
    index1 = 1
    index0 = 0

    while 1:
        while get_key(roman_string[index0:index1]) in roman:
            if index1 > size:
                break
            index1 += 1

        try:
            integer += get_key(roman_string[index0:index1 - 1])
        except TypeError:  # value not present
            return 0

        if index1 == size + 1:
            return integer
        index0 = index1 - 1
