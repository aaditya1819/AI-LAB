# Assignment 3: 8 Puzzle using Hill Climbing

This folder contains a Python implementation of the 8 puzzle problem using the Hill Climbing technique.

## Problem Statement

The 8 puzzle has a 3 x 3 board containing tiles numbered 1 to 8 and one blank space represented by `0`.
The goal is to move the blank space up, down, left, or right so that the puzzle reaches the goal state:

```text
1 2 3
4 5 6
7 8 0
```

Example start state:

```text
1 2 3
4 0 6
7 5 8
```

## Hill Climbing Idea

Hill Climbing is a heuristic search technique. It starts from the current state, checks all neighboring states, and moves to the neighbor that looks better.

In this program:

- The heuristic is Manhattan distance.
- Manhattan distance counts how far every tile is from its correct goal position.
- A smaller heuristic value means the board is closer to the goal.
- The algorithm always chooses the neighbor with the lowest heuristic value.
- If no neighbor improves the heuristic value, the algorithm stops.

Hill Climbing is fast and simple, but it is not complete. It may get stuck at a local minimum or plateau even when a solution exists.

## How to Run

Open a terminal in this folder and run:

```powershell
python .\eight_puzzle_hill_climbing.py
```

You can either use the default puzzle or enter your own 9 numbers from `0` to `8`.

Example custom input:

```text
Enter 9 numbers separated by spaces: 1 2 3 4 0 6 7 5 8
```

