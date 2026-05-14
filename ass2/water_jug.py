from collections import deque
from math import gcd


def is_solvable(capacity_a, capacity_b, goal):
    if goal < 0:
        return False
    if goal == 0:
        return True
    if goal > max(capacity_a, capacity_b):
        return False
    return goal % gcd(capacity_a, capacity_b) == 0


def is_goal(state, goal):
    return state[0] == goal or state[1] == goal


def get_successors(state, capacity_a, capacity_b):
    a, b = state
    successors = []

    def add(next_state, action):
        if next_state != state:
            successors.append((next_state, action))

    add((capacity_a, b), "Fill Jug A")
    add((a, capacity_b), "Fill Jug B")
    add((0, b), "Empty Jug A")
    add((a, 0), "Empty Jug B")

    pour = min(a, capacity_b - b)
    add((a - pour, b + pour), "Pour Jug A into Jug B")

    pour = min(b, capacity_a - a)
    add((a + pour, b - pour), "Pour Jug B into Jug A")

    return successors


def reconstruct_path(parent, goal_state):
    path = []
    current = goal_state

    while current is not None:
        previous, action = parent[current]
        path.append((current, action))
        current = previous

    path.reverse()
    return path


def breadth_first_search(capacity_a, capacity_b, goal):
    start = (0, 0)
    queue = deque([start])
    visited = {start}
    parent = {start: (None, "Start")}

    while queue:
        state = queue.popleft()

        if is_goal(state, goal):
            return reconstruct_path(parent, state)

        for next_state, action in get_successors(state, capacity_a, capacity_b):
            if next_state not in visited:
                visited.add(next_state)
                parent[next_state] = (state, action)
                queue.append(next_state)

    return None


def depth_first_search(capacity_a, capacity_b, goal):
    start = (0, 0)
    stack = [start]
    visited = {start}
    parent = {start: (None, "Start")}

    while stack:
        state = stack.pop()

        if is_goal(state, goal):
            return reconstruct_path(parent, state)

        for next_state, action in reversed(get_successors(state, capacity_a, capacity_b)):
            if next_state not in visited:
                visited.add(next_state)
                parent[next_state] = (state, action)
                stack.append(next_state)

    return None


def print_solution(title, path):
    print(f"\n{title}")
    print("-" * len(title))

    if path is None:
        print("No solution found.")
        return

    for step, (state, action) in enumerate(path):
        print(f"Step {step}: {action:25s} -> Jug A = {state[0]}, Jug B = {state[1]}")

    print(f"Total operations: {len(path) - 1}")


def read_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a non-negative integer.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter an integer.")


def main():
    print("Water Jug Problem using DFS and BFS")
    print("-----------------------------------")

    capacity_a = read_positive_integer("Enter capacity of Jug A: ")
    capacity_b = read_positive_integer("Enter capacity of Jug B: ")
    goal = read_positive_integer("Enter target amount of water: ")

    if capacity_a == 0 and capacity_b == 0:
        print("\nBoth jugs cannot have zero capacity.")
        return

    if not is_solvable(capacity_a, capacity_b, goal):
        print("\nNo solution exists for these capacities and target.")
        print("A target is reachable only if it is not greater than the larger jug")
        print("and it is divisible by gcd(capacity of Jug A, capacity of Jug B).")
        return

    dfs_path = depth_first_search(capacity_a, capacity_b, goal)
    bfs_path = breadth_first_search(capacity_a, capacity_b, goal)

    print_solution("Depth First Search Solution", dfs_path)
    print_solution("Breadth First Search Solution", bfs_path)


if __name__ == "__main__":
    main()
