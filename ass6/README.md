# Assignment 6: Constraint Satisfaction Algorithm

This folder contains Python implementations of Constraint Satisfaction Algorithm for:

- Cryptarithmetic
- Crossword puzzle
- Map coloring problem

## CSP Idea

A Constraint Satisfaction Problem is defined using:

- Variables
- Domains
- Constraints

The program uses backtracking search. At every step, it assigns a value to one unassigned variable and checks whether all constraints are still satisfied.

## Problems Included

### Cryptarithmetic

Solves:

```text
SEND + MORE = MONEY
```

Each letter is assigned a unique digit from 0 to 9. The first letters `S` and `M` cannot be zero.

### Crossword Puzzle

Fills a small crossword grid by assigning words to across and down slots. Intersecting words must have matching letters.

### Map Coloring

Colors the regions of the Australia map using three colors. Adjacent regions cannot have the same color.

## How to Run

Open a terminal in this folder and run:

```powershell
python .\constraint_satisfaction.py
```

Then choose one of the menu options:

```text
1. Cryptarithmetic
2. Crossword Puzzle
3. Map Coloring
4. Run all
5. Exit
```
