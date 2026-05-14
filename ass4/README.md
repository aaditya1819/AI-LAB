# Assignment 4: Best First Search

This folder contains Python implementations of Best First Search for:

- 8 puzzle
- Robot Navigation problem
- Cities Distance problem

## Best First Search Idea

Best First Search is a heuristic search technique. It uses a priority queue and always expands the node with the best heuristic value.

For 8 puzzle and Robot Navigation, lower heuristic values are considered better:

- 8 puzzle uses Manhattan distance of tiles from their goal positions.
- Robot Navigation uses Manhattan distance from the current cell to the goal cell.
- Cities Distance uses a cost-aware Best First Search priority, `f(n) = g(n) + h(n)`, so it can produce the shortest route by combining travelled distance and straight-line distance to Bucharest.

## How to Run

Open a terminal in this folder and run:

```powershell
python .\best_first_search.py
```

Then choose one of the menu options:

```text
1. 8 Puzzle
2. Robot Navigation
3. Cities Distance
4. Run all
5. Exit
```

## Note

Greedy Best First Search chooses the next state using only the heuristic value `h(n)`.
For the weighted Cities Distance problem, this program includes path cost `g(n)` with the heuristic so the route distance is minimized.
