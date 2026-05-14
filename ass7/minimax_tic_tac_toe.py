"""
Assignment 7: Minimax Algorithm for Tic Tac Toe

This program implements an interactive human-vs-computer Tic Tac Toe game.
The computer uses the Minimax algorithm, so it always chooses an optimal move.
"""

HUMAN = "X"
COMPUTER = "O"
EMPTY = " "

WIN_SCORE = 10
LOSE_SCORE = -10
DRAW_SCORE = 0


def display_board(board):
    print()
    for row in range(3):
        values = []
        for col in range(3):
            cell = board[row][col]
            if cell == EMPTY:
                values.append(str(row * 3 + col + 1))
            else:
                values.append(cell)

        print(" " + " | ".join(values))
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

    if all(board[index][index] == player for index in range(3)):
        return True

    if all(board[index][2 - index] == player for index in range(3)):
        return True

    return False


def is_board_full(board):
    return all(board[row][col] != EMPTY for row in range(3) for col in range(3))


def get_available_moves(board):
    moves = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                moves.append((row, col))
    return moves


def evaluate_terminal_state(board, depth, computer_symbol, human_symbol):
    if check_winner(board, computer_symbol):
        return WIN_SCORE - depth

    if check_winner(board, human_symbol):
        return LOSE_SCORE + depth

    if is_board_full(board):
        return DRAW_SCORE

    return None


def minimax(board, depth, is_maximizing, computer_symbol, human_symbol):
    score = evaluate_terminal_state(board, depth, computer_symbol, human_symbol)
    if score is not None:
        return score

    if is_maximizing:
        best_score = float("-inf")
        symbol = computer_symbol
    else:
        best_score = float("inf")
        symbol = human_symbol

    for row, col in get_available_moves(board):
        board[row][col] = symbol
        next_score = minimax(
            board,
            depth + 1,
            not is_maximizing,
            computer_symbol,
            human_symbol,
        )
        board[row][col] = EMPTY

        if is_maximizing:
            best_score = max(best_score, next_score)
        else:
            best_score = min(best_score, next_score)

    return best_score


def find_best_move(board, computer_symbol, human_symbol):
    best_score = float("-inf")
    best_move = None

    for row, col in get_available_moves(board):
        board[row][col] = computer_symbol
        move_score = minimax(
            board,
            depth=0,
            is_maximizing=False,
            computer_symbol=computer_symbol,
            human_symbol=human_symbol,
        )
        board[row][col] = EMPTY

        if move_score > best_score:
            best_score = move_score
            best_move = (row, col)

    return best_move


def get_human_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): "))
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 9.")
            continue

        if move < 1 or move > 9:
            print("Invalid position. Please choose a number from 1 to 9.")
            continue

        row = (move - 1) // 3
        col = (move - 1) % 3

        if board[row][col] != EMPTY:
            print("This position is already occupied. Choose another position.")
            continue

        return row, col


def get_symbol_choice():
    while True:
        symbol = input("Choose your symbol (X/O): ").strip().upper()
        if symbol in ("X", "O"):
            return symbol
        print("Invalid choice. Please enter X or O.")


def get_first_player_choice():
    while True:
        choice = input("Do you want to play first? (y/n): ").strip().lower()
        if choice in ("y", "yes"):
            return True
        if choice in ("n", "no"):
            return False
        print("Invalid choice. Please enter y or n.")


def announce_result(board, human_symbol, computer_symbol):
    if check_winner(board, human_symbol):
        print("You win!")
        return True

    if check_winner(board, computer_symbol):
        print("Computer wins!")
        return True

    if is_board_full(board):
        print("The game is a draw.")
        return True

    return False


def play_game():
    board = [[EMPTY for _ in range(3)] for _ in range(3)]

    print("Tic Tac Toe using Minimax Algorithm")
    print("-----------------------------------")
    human_symbol = get_symbol_choice()
    computer_symbol = "O" if human_symbol == "X" else "X"
    human_turn = get_first_player_choice()

    print(f"\nYou are {human_symbol}. Computer is {computer_symbol}.")
    display_board(board)

    while True:
        if human_turn:
            row, col = get_human_move(board)
            board[row][col] = human_symbol
            display_board(board)

            if announce_result(board, human_symbol, computer_symbol):
                break
        else:
            print("Computer is thinking...")
            row, col = find_best_move(board, computer_symbol, human_symbol)
            board[row][col] = computer_symbol
            print(f"Computer chose position {row * 3 + col + 1}.")
            display_board(board)

            if announce_result(board, human_symbol, computer_symbol):
                break

        human_turn = not human_turn


def main():
    while True:
        play_game()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print("Exiting.")
            break


if __name__ == "__main__":
    main()
