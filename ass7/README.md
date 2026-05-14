# Assignment 7: Minimax Algorithm

This assignment implements the Minimax algorithm for Tic Tac Toe.

## Problem

Tic Tac Toe is a two-player game played on a 3 x 3 board. The goal is to place three symbols in a row, column, or diagonal.

## Minimax Idea

Minimax explores all possible future moves from the current board state:

- The computer tries to maximize its score.
- The human player is assumed to play optimally and tries to minimize the computer's score.
- Winning, losing, and drawing terminal states are scored.

Because Tic Tac Toe has a small search space, the computer can evaluate the complete game tree and always choose an optimal move.

## How to Run

Open a terminal in this folder and run:

```powershell
python .\minimax_tic_tac_toe.py
```

Use positions 1 to 9 to place your move:

```text
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9
```
