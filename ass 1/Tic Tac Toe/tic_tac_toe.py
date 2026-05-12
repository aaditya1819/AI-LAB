"""
Assignment 1(a): Tic Tac Toe using Non-AI Technique

This program implements a two-player Tic Tac Toe game using simple
programming logic: lists, loops, conditions, and functions.
"""


def display_board(board):
    print()
    for row in range(3):
        print(" " + " | ".join(board[row]))
        if row < 2:
            print("---+---+---")
    print()


def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def is_board_full(board):
    return all(board[row][col] in ("X", "O") for row in range(3) for col in range(3))


def get_valid_move(board, player):
    while True:
        try:
            move = int(input(f"Player {player}, enter position (1-9): "))
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 9.")
            continue

        if move < 1 or move > 9:
            print("Invalid position. Please choose a number from 1 to 9.")
            continue

        row = (move - 1) // 3
        col = (move - 1) % 3

        if board[row][col] in ("X", "O"):
            print("This position is already occupied. Choose another position.")
            continue

        return row, col


def play_game():
    board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
    current_player = "X"

    print("Tic Tac Toe")
    print("Player 1: X")
    print("Player 2: O")
    display_board(board)

    while True:
        row, col = get_valid_move(board, current_player)
        board[row][col] = current_player
        display_board(board)

        if check_winner(board, current_player):
            print(f"Player {current_player} wins!")
            break

        if is_board_full(board):
            print("The game is a draw.")
            break

        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    play_game()
