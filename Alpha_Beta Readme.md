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
| **Alpha (α)** | Best value the maximizer currently can guarantee. |
| **Beta (β)** | Best value the minimizer currently can guarantee. |
| **Pruning** | Skipping parts of the search tree that won’t affect the final decision. |

---

## Algorithm Explanation

### 1. Without Alpha–Beta Pruning
In a standard Minimax tree:
- Every node is expanded.
- Time complexity = O(b^d), where  
  - b = branching factor  
  - d = depth of the tree

### 2. With Alpha–Beta Pruning
By keeping track of α and β:
- **α**: Maximum lower bound for MAX player.
- **β**: Minimum upper bound for MIN player.

If at any node:
then further exploration of that node’s children can be **stopped (pruned)**.

---

## Steps in the Algorithm

1. Start at the root (MAX player).
2. Traverse down the tree recursively.
3. At each MAX node:
   - Initialize α = -∞
   - Update α = max(α, value)
   - Prune if α ≥ β
4. At each MIN node:
   - Initialize β = +∞
   - Update β = min(β, value)
   - Prune if α ≥ β
5. Return the best possible value at the root.

---

## Pseudocode

```python
function minimax(node, depth, alpha, beta, isMaximizing):
    if node is a leaf:
        return node.value
    
    if isMaximizing:
        maxEval = -∞
        for each child of node:
            eval = minimax(child, depth+1, alpha, beta, False)
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # beta cutoff
        return maxEval

    else:
        minEval = +∞
        for each child of node:
            eval = minimax(child, depth+1, alpha, beta, True)
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break  # alpha cutoff
        return minEval
             (MAX)
            /     \
         (MIN)     (MIN)
        /  \       /   \
       3    5     6     9


Without Pruning:

All leaf nodes (3, 5, 6, 9) are checked.

With Alpha–Beta Pruning:

If the left MIN returns 3 for MAX, and the right MIN starts with a value 6 (greater than 3),
the right branch can be pruned early.

Complexity Analysis
Term - Description
Without - Pruning	O(b^d)
With Pruning - O(b^(d/2)) in the best case
Space Complexity -	O(b * d) (for recursion stack)
Optimality - Yes (same result as Minimax)



