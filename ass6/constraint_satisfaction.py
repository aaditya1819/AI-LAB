"""
Assignment 6: Constraint Satisfaction Algorithm

Problems covered:
1. Cryptarithmetic
2. Crossword puzzle
3. Map coloring problem

A Constraint Satisfaction Problem (CSP) has:
- Variables
- Domains of possible values
- Constraints that restrict valid combinations of values

This program uses backtracking search with a simple MRV heuristic.
MRV means Minimum Remaining Values: choose the unassigned variable with
the smallest remaining domain first.
"""


def select_unassigned_variable(variables, domains, assignment):
    unassigned = [variable for variable in variables if variable not in assignment]
    return min(unassigned, key=lambda variable: len(domains[variable]))


def is_consistent(variable, value, assignment, constraints):
    test_assignment = assignment.copy()
    test_assignment[variable] = value

    for constraint in constraints:
        if not constraint(test_assignment):
            return False

    return True


def backtracking_search(variables, domains, constraints, assignment=None):
    if assignment is None:
        assignment = {}

    if len(assignment) == len(variables):
        return assignment.copy()

    variable = select_unassigned_variable(variables, domains, assignment)

    for value in domains[variable]:
        if is_consistent(variable, value, assignment, constraints):
            assignment[variable] = value
            result = backtracking_search(variables, domains, constraints, assignment)

            if result is not None:
                return result

            del assignment[variable]

    return None


def all_different_constraint(variables):
    def constraint(assignment):
        assigned_values = [
            assignment[variable]
            for variable in variables
            if variable in assignment
        ]
        return len(assigned_values) == len(set(assigned_values))

    return constraint


def solve_cryptarithmetic():
    print("\nCryptarithmetic using CSP")
    print("-------------------------")
    print("Problem: SEND + MORE = MONEY")

    letters = ["D", "E", "Y", "N", "R", "O", "S", "M"]
    domains = {letter: list(range(10)) for letter in letters}

    def leading_letters_are_not_zero(assignment):
        if assignment.get("S") == 0:
            return False
        if assignment.get("M") == 0:
            return False
        return True

    def column_constraints(assignment):
        if {"D", "E", "Y"}.issubset(assignment):
            total = assignment["D"] + assignment["E"]
            if total % 10 != assignment["Y"]:
                return False
            carry1 = total // 10
        else:
            carry1 = None

        if carry1 is not None and {"N", "R", "E"}.issubset(assignment):
            total = assignment["N"] + assignment["R"] + carry1
            if total % 10 != assignment["E"]:
                return False
            carry2 = total // 10
        else:
            carry2 = None

        if carry2 is not None and {"E", "O", "N"}.issubset(assignment):
            total = assignment["E"] + assignment["O"] + carry2
            if total % 10 != assignment["N"]:
                return False
            carry3 = total // 10
        else:
            carry3 = None

        if carry3 is not None and {"S", "M", "O"}.issubset(assignment):
            total = assignment["S"] + assignment["M"] + carry3
            if total % 10 != assignment["O"] or total // 10 != assignment["M"]:
                return False

        if {"S", "E", "N", "D", "M", "O", "R", "Y"}.issubset(assignment):
            send = (
                assignment["S"] * 1000
                + assignment["E"] * 100
                + assignment["N"] * 10
                + assignment["D"]
            )
            more = (
                assignment["M"] * 1000
                + assignment["O"] * 100
                + assignment["R"] * 10
                + assignment["E"]
            )
            money = (
                assignment["M"] * 10000
                + assignment["O"] * 1000
                + assignment["N"] * 100
                + assignment["E"] * 10
                + assignment["Y"]
            )
            return send + more == money

        return True

    constraints = [
        all_different_constraint(letters),
        leading_letters_are_not_zero,
        column_constraints,
    ]

    solution = backtracking_search(letters, domains, constraints)

    if solution is None:
        print("No solution found.")
        return

    send = int("".join(str(solution[letter]) for letter in "SEND"))
    more = int("".join(str(solution[letter]) for letter in "MORE"))
    money = int("".join(str(solution[letter]) for letter in "MONEY"))

    print("Letter assignments:")
    for letter in sorted(solution):
        print(f"{letter} = {solution[letter]}")

    print(f"\n{send} + {more} = {money}")


def solve_crossword():
    print("\nCrossword Puzzle using CSP")
    print("--------------------------")

    variables = ["A1", "A2", "D1", "D2"]
    domains = {
        "A1": ["CAT", "CAR", "BAR", "BAT"],
        "A2": ["RUN", "ARE", "ART", "RAT", "TAR"],
        "D1": ["CAB", "CAR", "BAR", "BAT"],
        "D2": ["TREE", "TONE", "AREA", "EARN"],
    }

    positions = {
        "A1": [(0, 0), (0, 1), (0, 2)],
        "A2": [(2, 0), (2, 1), (2, 2)],
        "D1": [(0, 0), (1, 0), (2, 0)],
        "D2": [(0, 2), (1, 2), (2, 2), (3, 2)],
    }

    def no_repeated_words(assignment):
        words = list(assignment.values())
        return len(words) == len(set(words))

    def crossing_constraints(assignment):
        filled_cells = {}

        for variable, word in assignment.items():
            for index, cell in enumerate(positions[variable]):
                letter = word[index]

                if cell in filled_cells and filled_cells[cell] != letter:
                    return False

                filled_cells[cell] = letter

        return True

    constraints = [no_repeated_words, crossing_constraints]
    solution = backtracking_search(variables, domains, constraints)

    if solution is None:
        print("No solution found.")
        return

    print("Word placement:")
    print("A1: row 0, columns 0-2")
    print("A2: row 2, columns 0-2")
    print("D1: column 0, rows 0-2")
    print("D2: column 2, rows 0-3")

    for variable in variables:
        print(f"{variable} = {solution[variable]}")

    print("\nFilled crossword:")
    print_crossword_grid(solution, positions)


def print_crossword_grid(solution, positions):
    grid = [["#" for _ in range(3)] for _ in range(4)]

    for variable, word in solution.items():
        for index, (row, col) in enumerate(positions[variable]):
            grid[row][col] = word[index]

    for row in grid:
        print(" ".join(row))


def solve_map_coloring():
    print("\nMap Coloring using CSP")
    print("----------------------")
    print("Map: Australia")

    regions = ["WA", "NT", "SA", "Q", "NSW", "V", "T"]
    colors = ["Red", "Green", "Blue"]
    domains = {region: colors[:] for region in regions}

    neighbors = [
        ("WA", "NT"),
        ("WA", "SA"),
        ("NT", "SA"),
        ("NT", "Q"),
        ("SA", "Q"),
        ("SA", "NSW"),
        ("SA", "V"),
        ("Q", "NSW"),
        ("NSW", "V"),
    ]

    def adjacent_regions_have_different_colors(assignment):
        for first, second in neighbors:
            if first in assignment and second in assignment:
                if assignment[first] == assignment[second]:
                    return False
        return True

    solution = backtracking_search(
        regions,
        domains,
        [adjacent_regions_have_different_colors],
    )

    if solution is None:
        print("No solution found.")
        return

    print("Color assignments:")
    for region in regions:
        print(f"{region}: {solution[region]}")


def run_all():
    solve_cryptarithmetic()
    solve_crossword()
    solve_map_coloring()


def main():
    while True:
        print("\nConstraint Satisfaction Algorithm")
        print("---------------------------------")
        print("1. Cryptarithmetic")
        print("2. Crossword Puzzle")
        print("3. Map Coloring")
        print("4. Run all")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            solve_cryptarithmetic()
        elif choice == "2":
            solve_crossword()
        elif choice == "3":
            solve_map_coloring()
        elif choice == "4":
            run_all()
        elif choice == "5":
            print("Exiting.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
