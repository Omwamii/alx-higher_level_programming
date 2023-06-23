#!/usr/bin/python3
""" module to solve nqueens problem
"""
import sys


def is_safe(board, row, col):
    # Check if a queen can be placed at board[row][col]
    # without conflicting with any other queens

    # Check the left side of the current row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check the upper diagonal
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check the lower diagonal
    i = row
    j = col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve_nqueens(board, col):
    # Base case: If all queens are placed, print the solution
    if col >= N:
        print_solution(board)
        return True

    # Try placing a queen in each row of the current column
    for row in range(N):
        if is_safe(board, row, col):
            # Place the queen at board[row][col]
            board[row][col] = 1

            # Recur to place the rest of the queens
            solve_nqueens(board, col + 1)

            # Backtrack: Remove the queen from board[row][col]
            board[row][col] = 0

    return False


def print_solution(board):
    # Print the coordinates of the queens in the current solution
    solution = []
    for row in range(N):
        for col in range(N):
            if board[row][col] == 1:
                solution.append([row, col])
    print(solution)


# Check if the correct number of arguments is provided
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

# Parse and validate the input
try:
    N = int(sys.argv[1])
    if N < 4:
        raise ValueError
except ValueError:
    print("N must be a number and at least 4")
    sys.exit(1)

# Create an empty N x N board
board = [[0] * N for _ in range(N)]

# Solve the N Queens problem
solve_nqueens(board, 0)
