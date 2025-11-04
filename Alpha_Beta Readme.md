# Alpha–Beta Pruning in Minimax Algorithm

## Aim
To implement the **Alpha–Beta Pruning** optimization technique in the **Minimax Algorithm** to efficiently determine the optimal move in a two-player adversarial game (such as Tic-Tac-Toe or a simple decision tree).

---

## Overview

The **Minimax Algorithm** is used in decision-making and game theory to minimize the possible loss for a worst-case scenario.  
It assumes both players play optimally:
- **MAX** player tries to maximize the score.
- **MIN** player tries to minimize the score.

**Alpha–Beta Pruning** improves Minimax by eliminating branches that cannot influence the final decision, reducing computation time.

---

## Key Concepts

| Term | Description |
|------|--------------|
| **Minimax** | Evaluates all possible game moves recursively to find the optimal one. |
| **Alpha (α)** | Best value t
