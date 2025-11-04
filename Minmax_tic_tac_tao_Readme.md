# Minimax Algorithm – Tic Tac Toe

## Aim
To implement the **Minimax Algorithm** for playing an optimal game of **Tic-Tac-Toe**, ensuring that the computer never loses and either wins or draws.

---

## Overview
The **Minimax Algorithm** is a recursive algorithm used in **adversarial games** (like Chess, Checkers, or Tic-Tac-Toe).  
It simulates all possible moves of both players and selects the move that maximizes the AI’s chance of winning, while minimizing the opponent’s chances.

---

## Game Description
Tic-Tac-Toe is a simple 3×3 grid game:
- Two players: **X (Human)** and **O (Computer)**
- Players take turns placing their marks
- The goal is to align **three symbols in a row**, column, or diagonal

---

## Algorithm

### Step-by-Step Process

1. Generate all possible moves (empty cells).
2. For each move:
   - Simulate the move.
   - Recursively call Minimax to evaluate the outcome.
   - Undo the move (backtrack).
3. If it's the **AI's turn (maximizer)** → choose the move with the **maximum score**.
4. If it's the **Human's turn (minimizer)** → choose the move with the **minimum score**.
5. Continue until a **terminal state** (win, lose, draw) is reached.

---

## Minimax Scoring

| Result | Score |
|---------|--------|
| AI (O) wins | +1 |
| Human (X) wins | -1 |
| Draw | 0 |

---

## Pseudocode


function minimax(board, depth, isMaximizing):
    if terminal_state:
        return score(board)
    
    if isMaximizing:
        best = -∞
        for each possible move:
            make move
            value = minimax(board, depth+1, False)
            undo move
            best = max(best, value)
        return best
    else:
        best = +∞
        for each possible move:
            make move
            value = minimax(board, depth+1, True)
            undo move
            best = min(best, value)
        return best
