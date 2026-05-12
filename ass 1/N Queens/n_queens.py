"""
Assignment 1(b): N Queens using Non-AI Technique

This program solves the N Queens problem using backtracking.
The goal is to place N queens on an N x N chessboard so that no two
queens attack each other.
"""


def is_safe(board, row, col, n):
    for previous_row in range(row):
        if board[previous_row][col] == 1:
            return False

    previous_row = row - 1
    previous_col = col - 1
    while previous_row >= 0 and previous_col >= 0:
        if board[previous_row][previous_col] == 1:
            return False
        previous_row -= 1
        previous_col -= 1

    previous_row = row - 1
    previous_col = col + 1
    while previous_row >= 0 and previous_col < n:
        if board[previous_row][previous_col] == 1:
            return False
        previous_row -= 1
        previous_col += 1

    return True


def solve_n_queens(board, row, n, solutions):
    if row == n:
        solution = [current_row[:] for current_row in board]
        solutions.append(solution)
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_n_queens(board, row + 1, n, solutions)
            board[row][col] = 0


def print_board(board):
    for row in board:
        print(" ".join("Q" if cell == 1 else "." for cell in row))
    print()


def main():
    try:
        n = int(input("Enter the value of N: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    if n < 1:
        print("N must be greater than 0.")
        return

    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []

    solve_n_queens(board, 0, n, solutions)

    if not solutions:
        print(f"No solution exists for N = {n}.")
        return

    print(f"Total solutions for N = {n}: {len(solutions)}")
    print("First solution:")
    print_board(solutions[0])


if __name__ == "__main__":
    main()
