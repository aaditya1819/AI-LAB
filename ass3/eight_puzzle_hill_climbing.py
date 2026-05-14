"""
Assignment 3: 8 Puzzle using Hill Climbing

The blank tile is represented by 0.
The program uses Manhattan distance as the heuristic value.
"""

GOAL_STATE = (
    1, 2, 3,
    4, 5, 6,
    7, 8, 0,
)

BOARD_SIZE = 3


def print_board(state):
    for row in range(BOARD_SIZE):
        start = row * BOARD_SIZE
        print(" ".join("_" if value == 0 else str(value) for value in state[start:start + BOARD_SIZE]))
    print()


def get_goal_positions():
    positions = {}
    for index, tile in enumerate(GOAL_STATE):
        positions[tile] = (index // BOARD_SIZE, index % BOARD_SIZE)
    return positions


GOAL_POSITIONS = get_goal_positions()


def manhattan_distance(state):
    distance = 0

    for index, tile in enumerate(state):
        if tile == 0:
            continue

        current_row = index // BOARD_SIZE
        current_col = index % BOARD_SIZE
        goal_row, goal_col = GOAL_POSITIONS[tile]
        distance += abs(current_row - goal_row) + abs(current_col - goal_col)

    return distance


def get_neighbors(state):
    neighbors = []
    blank_index = state.index(0)
    blank_row = blank_index // BOARD_SIZE
    blank_col = blank_index % BOARD_SIZE

    moves = [
        ("Up", -1, 0),
        ("Down", 1, 0),
        ("Left", 0, -1),
        ("Right", 0, 1),
    ]

    for action, row_change, col_change in moves:
        new_row = blank_row + row_change
        new_col = blank_col + col_change

        if 0 <= new_row < BOARD_SIZE and 0 <= new_col < BOARD_SIZE:
            new_index = new_row * BOARD_SIZE + new_col
            next_state = list(state)
            next_state[blank_index], next_state[new_index] = next_state[new_index], next_state[blank_index]
            neighbors.append((tuple(next_state), action))

    return neighbors


def is_solvable(state):
    numbers = [tile for tile in state if tile != 0]
    inversions = 0

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] > numbers[j]:
                inversions += 1

    return inversions % 2 == 0


def hill_climbing(start_state):
    current_state = start_state
    current_heuristic = manhattan_distance(current_state)
    path = [(current_state, "Start", current_heuristic)]
    visited = {current_state}

    while current_state != GOAL_STATE:
        neighbors = get_neighbors(current_state)
        scored_neighbors = []

        for neighbor, action in neighbors:
            if neighbor not in visited:
                scored_neighbors.append((manhattan_distance(neighbor), neighbor, action))

        if not scored_neighbors:
            return path, False, "No unvisited neighboring states are available."

        best_heuristic, best_state, best_action = min(scored_neighbors, key=lambda item: item[0])

        if best_heuristic >= current_heuristic:
            return path, False, "Stopped because no neighbor improves the heuristic value."

        current_state = best_state
        current_heuristic = best_heuristic
        visited.add(current_state)
        path.append((current_state, best_action, current_heuristic))

    return path, True, "Goal state reached."


def read_start_state():
    default_state = (
        1, 2, 3,
        4, 0, 6,
        7, 5, 8,
    )

    print("Enter the start state as 9 numbers from 0 to 8.")
    print("Use 0 for the blank tile.")
    user_input = input("Press Enter for default puzzle, or enter values: ").strip()

    if not user_input:
        return default_state

    try:
        state = tuple(int(value) for value in user_input.split())
    except ValueError:
        print("Invalid input. Please enter only integers.")
        return None

    if len(state) != 9 or sorted(state) != list(range(9)):
        print("Invalid puzzle. Enter each number from 0 to 8 exactly once.")
        return None

    return state


def print_solution(path, success, message):
    print("\nHill Climbing Search Path")
    print("-------------------------")

    for step, (state, action, heuristic) in enumerate(path):
        print(f"Step {step}: {action}, h = {heuristic}")
        print_board(state)

    print(message)
    print(f"Total moves: {len(path) - 1}")

    if not success:
        print("Hill Climbing did not find the goal from this start state.")
        print("This can happen because Hill Climbing may get stuck in a local minimum or plateau.")


def main():
    print("8 Puzzle Problem using Hill Climbing")
    print("------------------------------------")
    print("Goal State:")
    print_board(GOAL_STATE)

    start_state = read_start_state()
    if start_state is None:
        return

    if not is_solvable(start_state):
        print("\nThis puzzle is not solvable.")
        print("For a 3 x 3 puzzle, the number of inversions must be even.")
        return

    path, success, message = hill_climbing(start_state)
    print_solution(path, success, message)


if __name__ == "__main__":
    main()
