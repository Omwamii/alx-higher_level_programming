#!/usr/bin/python3
def uppercase(str):
    output = ""
    for ch in str:
        asc = ord(ch)
        if asc < 97 or asc > 122:
            output += chr(asc)
            continue
        else:
            val = asc - 32
            output += chr(val)
    print("{}".format(output), end="")
    print()
