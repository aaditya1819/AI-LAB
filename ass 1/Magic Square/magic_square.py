"""
Assignment 1(c): Magic Square using Non-AI Technique

This program generates a magic square for any valid order N except N = 2.
A magic square contains numbers 1 to N*N, arranged so every row, column,
and both main diagonals have the same sum.
"""


def generate_odd_magic_square(n):
    square = [[0 for _ in range(n)] for _ in range(n)]
    row = 0
    col = n // 2

    for number in range(1, n * n + 1):
        square[row][col] = number

        next_row = (row - 1) % n
        next_col = (col + 1) % n

        if square[next_row][next_col] != 0:
            row = (row + 1) % n
        else:
            row = next_row
            col = next_col

    return square


def generate_doubly_even_magic_square(n):
    square = [[n * row + col + 1 for col in range(n)] for row in range(n)]
    max_value = n * n + 1

    for row in range(n):
        for col in range(n):
            if row % 4 == col % 4 or (row % 4) + (col % 4) == 3:
                square[row][col] = max_value - square[row][col]

    return square


def generate_singly_even_magic_square(n):
    half = n // 2
    sub_square = generate_odd_magic_square(half)
    square = [[0 for _ in range(n)] for _ in range(n)]
    add_values = [0, 2 * half * half, 3 * half * half, half * half]

    for row in range(half):
        for col in range(half):
            square[row][col] = sub_square[row][col] + add_values[0]
            square[row][col + half] = sub_square[row][col] + add_values[1]
            square[row + half][col] = sub_square[row][col] + add_values[2]
            square[row + half][col + half] = sub_square[row][col] + add_values[3]

    columns_to_swap = (n - 2) // 4

    for row in range(half):
        for col in range(columns_to_swap):
            square[row][col], square[row + half][col] = square[row + half][col], square[row][col]

        for col in range(n - columns_to_swap + 1, n):
            square[row][col], square[row + half][col] = square[row + half][col], square[row][col]

    middle_col = columns_to_swap
    middle_row = half // 2
    square[middle_row][middle_col], square[middle_row + half][middle_col] = (
        square[middle_row + half][middle_col],
        square[middle_row][middle_col],
    )
    square[middle_row][0], square[middle_row + half][0] = (
        square[middle_row + half][0],
        square[middle_row][0],
    )

    return square


def generate_magic_square(n):
    if n % 2 == 1:
        return generate_odd_magic_square(n)
    if n % 4 == 0:
        return generate_doubly_even_magic_square(n)
    return generate_singly_even_magic_square(n)


def magic_constant(n):
    return n * (n * n + 1) // 2


def print_square(square):
    width = len(str(len(square) * len(square)))
    for row in square:
        print(" ".join(f"{value:{width}d}" for value in row))


def verify_magic_square(square):
    n = len(square)
    expected_sum = magic_constant(n)

    for row in square:
        if sum(row) != expected_sum:
            return False

    for col in range(n):
        if sum(square[row][col] for row in range(n)) != expected_sum:
            return False

    if sum(square[i][i] for i in range(n)) != expected_sum:
        return False

    if sum(square[i][n - 1 - i] for i in range(n)) != expected_sum:
        return False

    numbers = [value for row in square for value in row]
    return sorted(numbers) == list(range(1, n * n + 1))


def main():
    try:
        n = int(input("Enter the order of magic square: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    if n < 3:
        print("Magic square is possible only for N >= 3, except N = 2 has no solution.")
        return

    square = generate_magic_square(n)

    print(f"\nMagic Square of order {n}:")
    print_square(square)
    print(f"\nMagic constant: {magic_constant(n)}")

    if verify_magic_square(square):
        print("Verification: Valid magic square.")
    else:
        print("Verification: Invalid magic square.")


if __name__ == "__main__":
    main()
