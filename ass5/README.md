# Assignment 5: A* Algorithm

This folder contains Python implementations of the A* algorithm for:

- 8 puzzle
- Robot Navigation problem
- Cities Distance shortest path problem

## A* Search Idea

A* is an informed search algorithm. It selects the next node using:

```text
f(n) = g(n) + h(n)
```

- `g(n)` is the actual cost from the start node to the current node.
- `h(n)` is the estimated cost from the current node to the goal node.
- `f(n)` is the total estimated cost of the best solution through that node.

## Heuristics Used

- 8 Puzzle: Manhattan distance of each tile from its goal position.
- Robot Navigation: Manhattan distance from the current grid cell to the goal cell.
- Cities Distance: Straight-line distance to Bucharest.

## How to Run

Open a terminal in this folder and run:

```powershell
python .\a_star_algorithm.py
```

Then choose one of the menu options:

```text
1. 8 Puzzle
2. Robot Navigation
3. Cities Distance
4. Run all
5. Exit
```

## Output

The program prints the solution path and shows the `g`, `h`, and `f` values for each step.
