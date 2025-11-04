

## 🐍 PART 2: `eight_puzzle_astar.py`


"""
8-Puzzle Problem using A* Search Algorithm
------------------------------------------

AIM:
To solve the 8-Puzzle Problem using the A* Search Algorithm with
the Manhattan Distance heuristic function.
"""

import heapq


class PuzzleState:
    """Represents a single state of the 8-puzzle."""
    def __init__(self, value, parent=None, g=0):
        self.value = value  # 3x3 flattened list (0-8)
        self.parent = parent
        self.g = g  # Cost from start to current state
        self.h = 0  # Heuristic cost to goal
        self.f = 0  # Total cost f = g + h

    def __lt__(self, other):
        """Defines priority queue ordering based on total cost f."""
        return self.f < other.f


def manhattan_distance(state, goal):
    """Calculate Manhattan distance between current and goal states."""
    distance = 0
    for i in range(9):
        if state[i] != 0:
            goal_index = goal.index(state[i])
            x1, y1 = i // 3, i % 3
            x2, y2 = goal_index // 3, goal_index % 3
            distance += abs(x1 - x2) + abs(y1 - y2)
    return distance


def get_neighbors(state):
    """Generate valid neighbor states by moving the blank (0)."""
    neighbors = []
    index = state.index(0)
    row, col = index // 3, index % 3

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

    for dx, dy in moves:
        new_row, new_col = row + dx, col + dy
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_index = new_row * 3 + new_col
            new_state = state.copy()
            new_state[index], new_state[new_index] = new_state[new_index], new_state[index]
            neighbors.append(new_state)
    return neighbors


def reconstruct_path(node):
    """Reconstruct the path from goal to start."""
    path = []
    while node:
        path.append(node.value)
        node = node.parent
    return path[::-1]


def a_star_search(start, goal):
    """A* Search algorithm implementation."""
    open_list = []
    closed = set()

    start_state = PuzzleState(start)
    start_state.h = manhattan_distance(start, goal)
    start_state.f = start_state.g + start_state.h
    heapq.heappush(open_list, start_state)

    while open_list:
        current = heapq.heappop(open_list)

        if current.value == goal:
            return reconstruct_path(current)

        closed.add(tuple(current.value))

        for neighbor in get_neighbors(current.value):
            if tuple(neighbor) in closed:
                continue

            child = PuzzleState(neighbor, current, current.g + 1)
            child.h = manhattan_distance(neighbor, goal)
            child.f = child.g + child.h
            heapq.heappush(open_list, child)

    return None


if __name__ == "__main__":
    # Example Test
    start_state = [1, 2, 3, 4, 0, 6, 7, 5, 8]
    goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]

    path = a_star_search(start_state, goal_state)

    if path:
        print("Path Found:")
        for p in path:
            print(p)
        print("Goal Reached!")
    else:
        print("No path exists.")
