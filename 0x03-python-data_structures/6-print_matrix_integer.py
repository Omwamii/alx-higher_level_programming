#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    '''prints matrix of integers'''
    if int(len(matrix)) == 0:
        print()
    else:
        for row in matrix:
            for d in range(len(row)):
                if d < len(row) - 1:
                    print("{}".format(row[d]), end=" ")
                else:
                    print("{}".format(row[d]), end="")
            print()
