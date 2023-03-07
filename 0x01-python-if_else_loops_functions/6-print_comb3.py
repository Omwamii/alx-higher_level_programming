#!/usr/bin/python3
for n in range(0, 9):
    for a in range(n+1, 10):
        if n == 8 and a == 9:  # last iteration
            print(n, end="")
            print(a)
        else:
            print(n, end="")
            print(a, end=", ")
