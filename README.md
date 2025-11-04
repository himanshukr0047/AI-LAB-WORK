AI Search Problem Solutions

This repository contains multiple AI problem solutions implemented using various search and optimization algorithms.
Each section includes a clear aim, algorithm explanation, and complexity analysis.

1. Magic Square Problem (Backtracking)
Aim

To generate a Magic Square of order n using the Backtracking (Depth-First Search) approach, ensuring that the sum of every row, column, and both diagonals is the same.

Description

A Magic Square is an n × n matrix filled with numbers 1 to n² such that:

Each number is used exactly once.

The sum of every row, column, and diagonal equals a constant:

M = n(n² + 1) / 2


where M is called the Magic Constant.

Algorithm

State Representation

Use a 2D array to represent the current square.

Maintain a boolean array to track which numbers (1 to n²) are used.

Validity Check

After placing a number in position (row, col):

Ensure that no row, column, or diagonal sum exceeds M.

If any row/column/diagonal is complete, its sum must equal M.

Backtracking Procedure

Fill the square one cell at a time (row by row).

Try all unused numbers for each cell.

If the current placement keeps the square valid → recurse to the next cell.

If invalid → backtrack (undo the move and try the next number).

Stop when the entire square is filled correctly.

Pseudocode
def solve_magic_square(matrix, used, row, col, n, M):
    if row == n:
        return True  # all cells filled

    next_row, next_col = (row + (col + 1) // n, (col + 1) % n)
    
    for num in range(1, n*n + 1):
        if not used[num]:
            matrix[row][col] = num
            used[num] = True

            if is_valid(matrix, row, col, n, M):
                if solve_magic_square(matrix, used, next_row, next_col, n, M):
                    return True

            matrix[row][col] = 0
            used[num] = False

    return False

Complexity

Time Complexity: O((n²)! × n)

Space Complexity: O(n²)

2. Water Jug Problem (Breadth-First Search)
Aim

To find the sequence of steps required to measure an exact amount of water using two jugs of given capacities with Breadth-First Search (BFS).

Problem Description

Given two jugs with capacities C1 and C2, and a target amount T, determine the steps to get exactly T liters in either jug.

Allowed Operations:

Fill any jug completely.

Empty any jug.

Pour water from one jug to another until one is full or the other is empty.

Algorithm

State Representation

Each state is represented as (jug1, jug2) representing the amount of water in both jugs.

Maintain a parent mapping for path reconstruction.

BFS Approach

Use a queue to explore states level-by-level.

For each state, generate all possible next states based on allowed operations.

Stop when either jug has T liters.

Use a set to store visited states to avoid repetition.

Pseudocode
from collections import deque

def water_jug_bfs(C1, C2, T):
    visited = set()
    q = deque()
    q.append((0, 0))  # initial state

    while q:
        j1, j2 = q.popleft()

        if (j1, j2) in visited:
            continue
        visited.add((j1, j2))

        if j1 == T or j2 == T:
            print(f"Solution found: Jug1={j1}, Jug2={j2}")
            return

        # Possible operations
        next_states = [
            (C1, j2),  # Fill jug1
            (j1, C2),  # Fill jug2
            (0, j2),   # Empty jug1
            (j1, 0),   # Empty jug2
            (min(C1, j1 + j2), max(0, j2 - (C1 - j1))),  # Pour jug2 -> jug1
            (max(0, j1 - (C2 - j2)), min(C2, j1 + j2))   # Pour jug1 -> jug2
        ]

        for state in next_states:
            if state not in visited:
                q.append(state)

Example
C1 = 4, C2 = 3, Target = 2
Output Steps:
(0, 0) → (4, 0) → (1, 3) → (1, 0) → (0, 1) → (4, 1) → (2, 3)

Complexity

Time Complexity: O(C1 × C2)

Space Complexity: O(C1 × C2)

3. Hill Climbing (Magic Square Optimization)
Aim

To construct a Magic Square using the Hill Climbing optimization algorithm, minimizing the difference between each row/column/diagonal sum and the magic constant.

Description

Instead of exhaustive backtracking, Hill Climbing treats the problem as an optimization task:

Start from a random arrangement of 1..n² numbers.

Define a cost function measuring how “far” the current square is from being magic.

Iteratively improve the square by making small changes that reduce the cost.

Algorithm

State Representation

state: n×n matrix containing numbers 1..n².

cost: absolute difference between current sums and the magic constant.

Heuristic / Cost Function

cost = sum(abs(sum(row_i) - M)) + sum(abs(sum(col_i) - M)) + abs(diagonal_sum - M)


Algorithm Steps

Generate an initial random square.

Compute its cost.

Swap two random cells to create a neighbor.

Compute the new cost:

If it improves → move to that neighbor.

Else → continue searching (or stop after max iterations).

Repeat until cost = 0 or no better move is found.

Pseudocode
import random

def hill_climb_magic_square(n):
    M = n * (n**2 + 1) // 2

    def cost(square):
        diff = 0
        for i in range(n):
            diff += abs(sum(square[i]) - M)
            diff += abs(sum(square[j][i] for j in range(n)) - M)
        diff += abs(sum(square[i][i] for i in range(n)) - M)
        diff += abs(sum(square[i][n - i - 1] for i in range(n)) - M)
        return diff

    # Random initial square
    nums = list(range(1, n**2 + 1))
    random.shuffle(nums)
    square = [nums[i*n:(i+1)*n] for i in range(n)]

    current_cost = cost(square)

    for _ in range(10000):  # iteration limit
        a, b = random.sample(range(n*n), 2)
        i1, j1, i2, j2 = divmod(a, n)[0], divmod(a, n)[1], divmod(b, n)[0], divmod(b, n)[1]
        square[i1][j1], square[i2][j2] = square[i2][j2], square[i1][j1]
        new_cost = cost(square)

        if new_cost < current_cost:
            current_cost = new_cost
        else:
            square[i1][j1], square[i2][j2] = square[i2][j2], square[i1][j1]  # revert

        if current_cost == 0:
            break

    return square

Complexity

Time Complexity: O(k × n²)
(where k = number of iterations)

Space Complexity: O(n²)


# 8-Puzzle Problem using A* Search Algorithm

## Aim
To solve the **8-Puzzle Problem** using the **A* Search Algorithm**, an informed search method that uses both actual cost and a heuristic estimate to find the optimal path to the goal.

---

## Problem Description
The **8-Puzzle** is a 3×3 grid puzzle with eight numbered tiles and one blank space (`0`).  
The objective is to move the blank tile to arrange all tiles into the goal configuration.

### Example

**Initial State**
1 2 3
4 0 6
7 5 8



**Goal State**
1 2 3
4 5 6
7 8 0



---

 Algorithm Overview

 1. State Representation
Each state (board configuration) is represented as:
- A 1D list of 9 integers (0–8), where 0 represents the blank.
- A reference to the **parent state** (for path reconstruction).
- Two cost values:
  - **g(n):** Cost from start state to current state.
  - **h(n):** Heuristic estimate from current state to goal.
  - **f(n):** Total estimated cost (`f(n) = g(n) + h(n)`).

---

2. Move Generation
For the blank tile (0), valid moves include:
- **Left** (if `index % 3 > 0`)
- **Right** (if `index % 3 < 2`)
- **Up** (if `index // 3 > 0`)
- **Down** (if `index // 3 < 2`)

Each move generates a new child state by swapping the blank with the target tile.

---

3. Heuristic Function
We use the **Manhattan Distance** heuristic:

h(n) = Σ |x_current - x_goal| + |y_current - y_goal|

sql
Copy code

where (x, y) are the coordinates of each tile (excluding 0).  
This heuristic is **admissible** — it never overestimates the true cost to reach the goal.

---

4. A* Search Steps

1. Initialize a **priority queue (min-heap)** ordered by `f(n) = g(n) + h(n)`.
2. Insert the start state into the queue.
3. While the queue is not empty:
   - Pop the state with the lowest `f(n)`.
   - If it matches the goal → reconstruct the path.
   - Generate all valid neighbor states.
   - For each neighbor, calculate new `g`, `h`, and `f`.
   - Add unvisited neighbors to the priority queue.
4. Maintain a **closed list** of visited states.

---

 Pseudocode

function A_STAR(start, goal):
    open_list = PriorityQueue()
    open_list.push(start, f = g + h)
    closed = set()

    while open_list not empty:
        current = open_list.pop()
        if current == goal:
            return reconstruct_path(current)
        closed.add(current)
        for neighbor in generate_moves(current):
            if neighbor not in closed:
                compute g, h, f
                open_list.push(neighbor, f)
    return None
Complexity Analysis
Term	Meaning	Typical Range
b	Branching Factor	2 – 4
d	Depth of Optimal Solution	Variable
n	Total Possible States	9! = 362,880

Time Complexity: O(b^d) in the worst case

Space Complexity: O(b^d) for storing visited and frontier states

Per State Memory: 9 integers + costs + parent pointer

Example Output
less
Copy code
Initial State: [1, 2, 3, 4, 0, 6, 7, 5, 8]
Goal State:    [1, 2, 3, 4, 5, 6, 7, 8, 0]

Path:
[1, 2, 3, 4, 0, 6, 7, 5, 8]
[1, 2, 3, 4, 5, 6, 7, 0, 8]
[1, 2, 3, 4, 5, 6, 7, 8, 0]
Goal Reached!

