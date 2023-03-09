#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count = 0
    if len(sys.argv) == 1:
        print("{} arguments.".format(len(sys.argv) - 1))
    elif len(sys.argv) == 2:
        count += 1
        print("{} argument:".format(len(sys.argv) - 1))
        print("{}: {}".format(count, sys.argv[1]))
    else:
        print("{} arguments:".format(len(sys.argv) - 1))
        for a in (sys.argv):
            if a == sys.argv[0]:
                continue
            count += 1
            print("{}: {}".format(count, a))
