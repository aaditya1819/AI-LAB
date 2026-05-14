# Assignment 2: Water Jug Problem

This folder contains a Python implementation of the Water Jug problem using uninformed search strategies:

1. Depth First Search
2. Breadth First Search

## Problem Statement

Given two jugs with fixed capacities and no measuring marks, measure an exact target amount of water using only these operations:

- Fill a jug completely
- Empty a jug completely
- Pour water from one jug to the other until the source jug is empty or the destination jug is full

Each state is represented as:

```text
(amount_in_jug_a, amount_in_jug_b)
```

The initial state is:

```text
(0, 0)
```

The goal is reached when either jug contains the target amount.

## How to Run

Open a terminal in this folder and run:

```powershell
python .\water_jug.py
```

Example input:

```text
Enter capacity of Jug A: 4
Enter capacity of Jug B: 3
Enter target amount of water: 2
```

## Notes

- BFS explores states level by level and gives the shortest solution in number of operations.
- DFS explores one path deeply first and may not produce the shortest solution.
- A visited set is used in both algorithms to avoid repeating states.
