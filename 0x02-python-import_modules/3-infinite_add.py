#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count = 0
    for n in (sys.argv):
        if n == sys.argv[0]:
            continue
        count += int(n)
    print("{}".format(count))
