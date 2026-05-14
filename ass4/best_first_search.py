"""
Assignment 4: Best First Search

Problems covered:
1. 8 Puzzle
2. Robot Navigation
3. Cities Distance shortest path

Best First Search expands the most promising node first.
The priority queue is ordered by heuristic value h(n).
"""

import heapq


GOAL_PUZZLE = (
    1, 2, 3,
    4, 5, 6,
    7, 8, 0,
)

BOARD_SIZE = 3


def reconstruct_path(parent, goal_state):
    path = []
    current = goal_state

    while current is not None:
        previous, action = parent[current]
        path.append((current, action))
        current = previous

    path.reverse()
    return path


def best_first_search(start, is_goal, get_neighbors, heuristic):
    priority_queue = []
    counter = 0
    heapq.heappush(priority_queue, (heuristic(start), counter, start))

    visited = {start}
    parent = {start: (None, "Start")}

    while priority_queue:
        _, _, current = heapq.heappop(priority_queue)

        if is_goal(current):
            return reconstruct_path(parent, current)

        for next_state, action in get_neighbors(current):
            if next_state not in visited:
                visited.add(next_state)
                parent[next_state] = (current, action)
                counter += 1
                heapq.heappush(priority_queue, (heuristic(next_state), counter, next_state))

    return None


def best_first_search_with_cost(start, goal, get_weighted_neighbors, heuristic):
    priority_queue = []
    counter = 0
    heapq.heappush(priority_queue, (heuristic(start), counter, start))

    parent = {start: (None, "Start")}
    cost_so_far = {start: 0}
    visited = set()

    while priority_queue:
        _, _, current = heapq.heappop(priority_queue)

        if current in visited:
            continue

        visited.add(current)

        if current == goal:
            return reconstruct_path(parent, current), cost_so_far[current]

        for next_state, distance, action in get_weighted_neighbors(current):
            new_cost = cost_so_far[current] + distance

            if next_state not in cost_so_far or new_cost < cost_so_far[next_state]:
                cost_so_far[next_state] = new_cost
                parent[next_state] = (current, action)
                counter += 1
                priority = new_cost + heuristic(next_state)
                heapq.heappush(priority_queue, (priority, counter, next_state))

    return None, None


def print_puzzle_board(state):
    for row in range(BOARD_SIZE):
        start = row * BOARD_SIZE
        values = state[start:start + BOARD_SIZE]
        print(" ".join("_" if value == 0 else str(value) for value in values))
    print()


def get_goal_positions():
    positions = {}
    for index, tile in enumerate(GOAL_PUZZLE):
        positions[tile] = (index // BOARD_SIZE, index % BOARD_SIZE)
    return positions


GOAL_POSITIONS = get_goal_positions()


def puzzle_heuristic(state):
    distance = 0

    for index, tile in enumerate(state):
        if tile == 0:
            continue

        current_row = index // BOARD_SIZE
        current_col = index % BOARD_SIZE
        goal_row, goal_col = GOAL_POSITIONS[tile]
        distance += abs(current_row - goal_row) + abs(current_col - goal_col)

    return distance


def get_puzzle_neighbors(state):
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


def is_puzzle_solvable(state):
    numbers = [tile for tile in state if tile != 0]
    inversions = 0

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] > numbers[j]:
                inversions += 1

    return inversions % 2 == 0


def solve_8_puzzle():
    start = (
        1, 2, 3,
        4, 0, 6,
        7, 5, 8,
    )

    print("\n8 Puzzle using Best First Search")
    print("--------------------------------")
    print("Start State:")
    print_puzzle_board(start)
    print("Goal State:")
    print_puzzle_board(GOAL_PUZZLE)

    if not is_puzzle_solvable(start):
        print("This puzzle is not solvable.")
        return

    path = best_first_search(
        start,
        lambda state: state == GOAL_PUZZLE,
        get_puzzle_neighbors,
        puzzle_heuristic,
    )

    if path is None:
        print("No solution found.")
        return

    for step, (state, action) in enumerate(path):
        print(f"Step {step}: {action}, h = {puzzle_heuristic(state)}")
        print_puzzle_board(state)

    print(f"Total moves: {len(path) - 1}")


GRID = [
    [0, 0, 0, 0, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0],
]

ROBOT_START = (0, 0)
ROBOT_GOAL = (4, 4)


def robot_heuristic(position):
    row, col = position
    goal_row, goal_col = ROBOT_GOAL
    return abs(row - goal_row) + abs(col - goal_col)


def get_robot_neighbors(position):
    row, col = position
    neighbors = []

    moves = [
        ("Up", -1, 0),
        ("Down", 1, 0),
        ("Left", 0, -1),
        ("Right", 0, 1),
    ]

    for action, row_change, col_change in moves:
        new_row = row + row_change
        new_col = col + col_change

        if 0 <= new_row < len(GRID) and 0 <= new_col < len(GRID[0]):
            if GRID[new_row][new_col] == 0:
                neighbors.append(((new_row, new_col), action))

    return neighbors


def print_robot_grid(path_positions):
    path_set = set(path_positions)

    for row in range(len(GRID)):
        values = []
        for col in range(len(GRID[0])):
            position = (row, col)

            if position == ROBOT_START:
                values.append("S")
            elif position == ROBOT_GOAL:
                values.append("G")
            elif GRID[row][col] == 1:
                values.append("#")
            elif position in path_set:
                values.append("*")
            else:
                values.append(".")

        print(" ".join(values))


def solve_robot_navigation():
    print("\nRobot Navigation using Best First Search")
    print("----------------------------------------")
    print("S = Start, G = Goal, # = Obstacle, * = Path")

    path = best_first_search(
        ROBOT_START,
        lambda position: position == ROBOT_GOAL,
        get_robot_neighbors,
        robot_heuristic,
    )

    if path is None:
        print("No path found.")
        return

    positions = [state for state, _ in path]
    print_robot_grid(positions)

    print("\nPath:")
    for step, (position, action) in enumerate(path):
        print(f"Step {step}: {action:5s} -> {position}, h = {robot_heuristic(position)}")

    print(f"Total moves: {len(path) - 1}")


CITY_GRAPH = {
    "Arad": [("Zerind", 75), ("Sibiu", 140), ("Timisoara", 118)],
    "Zerind": [("Arad", 75), ("Oradea", 71)],
    "Oradea": [("Zerind", 71), ("Sibiu", 151)],
    "Sibiu": [("Arad", 140), ("Oradea", 151), ("Fagaras", 99), ("Rimnicu Vilcea", 80)],
    "Timisoara": [("Arad", 118), ("Lugoj", 111)],
    "Lugoj": [("Timisoara", 111), ("Mehadia", 70)],
    "Mehadia": [("Lugoj", 70), ("Drobeta", 75)],
    "Drobeta": [("Mehadia", 75), ("Craiova", 120)],
    "Craiova": [("Drobeta", 120), ("Rimnicu Vilcea", 146), ("Pitesti", 138)],
    "Rimnicu Vilcea": [("Sibiu", 80), ("Craiova", 146), ("Pitesti", 97)],
    "Fagaras": [("Sibiu", 99), ("Bucharest", 211)],
    "Pitesti": [("Rimnicu Vilcea", 97), ("Craiova", 138), ("Bucharest", 101)],
    "Bucharest": [("Fagaras", 211), ("Pitesti", 101), ("Giurgiu", 90), ("Urziceni", 85)],
    "Giurgiu": [("Bucharest", 90)],
    "Urziceni": [("Bucharest", 85), ("Hirsova", 98), ("Vaslui", 142)],
    "Hirsova": [("Urziceni", 98), ("Eforie", 86)],
    "Eforie": [("Hirsova", 86)],
    "Vaslui": [("Urziceni", 142), ("Iasi", 92)],
    "Iasi": [("Vaslui", 92), ("Neamt", 87)],
    "Neamt": [("Iasi", 87)],
}

CITY_HEURISTIC = {
    "Arad": 366,
    "Bucharest": 0,
    "Craiova": 160,
    "Drobeta": 242,
    "Eforie": 161,
    "Fagaras": 176,
    "Giurgiu": 77,
    "Hirsova": 151,
    "Iasi": 226,
    "Lugoj": 244,
    "Mehadia": 241,
    "Neamt": 234,
    "Oradea": 380,
    "Pitesti": 100,
    "Rimnicu Vilcea": 193,
    "Sibiu": 253,
    "Timisoara": 329,
    "Urziceni": 80,
    "Vaslui": 199,
    "Zerind": 374,
}


def city_heuristic(city):
    return CITY_HEURISTIC[city]


def get_city_neighbors(city):
    return [(neighbor, f"Go to {neighbor}") for neighbor, _ in CITY_GRAPH[city]]


def get_weighted_city_neighbors(city):
    return [(neighbor, distance, f"Go to {neighbor}") for neighbor, distance in CITY_GRAPH[city]]


def solve_city_distance():
    start = "Arad"
    goal = "Bucharest"

    print("\nCities Distance using Best First Search")
    print("---------------------------------------")
    print(f"Start city: {start}")
    print(f"Goal city: {goal}")

    path, total_distance = best_first_search_with_cost(
        start,
        goal,
        get_weighted_city_neighbors,
        city_heuristic,
    )

    if path is None:
        print("No route found.")
        return

    for step, (city, action) in enumerate(path):
        print(f"Step {step}: {action:16s} -> {city}, h = {city_heuristic(city)}")

    print(f"Route: {' -> '.join(city for city, _ in path)}")
    print(f"Total distance: {total_distance} km")


def main():
    while True:
        print("\nBest First Search")
        print("-----------------")
        print("1. 8 Puzzle")
        print("2. Robot Navigation")
        print("3. Cities Distance")
        print("4. Run all")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            solve_8_puzzle()
        elif choice == "2":
            solve_robot_navigation()
        elif choice == "3":
            solve_city_distance()
        elif choice == "4":
            solve_8_puzzle()
            solve_robot_navigation()
            solve_city_distance()
        elif choice == "5":
            print("Exiting.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
