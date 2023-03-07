#!/usr/bin/python3
for a in range(90, 64, -1):
    if a % 2 == 0:
        al = chr(a + 32)
    else:
        al = chr(a)

    print("{}".format(al), end="")
