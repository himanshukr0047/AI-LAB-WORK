def water_jug_problem():
    # capacities
    jug_a, jug_b = 4, 3
    visited = set()
    stack = [(0, 0)]  # initial state (A=0, B=0)

    while stack:
        a, b = stack.pop()
        if (a, b) in visited:
            continue
        visited.add((a, b))
        print(f"Jug A: {a}L, Jug B: {b}L")

        # Goal: 2 liters in Jug A
        if a == 2:
            print("Goal reached!")
            return

        # possible moves
        moves = [
            (jug_a, b),         # Fill Jug A
            (a, jug_b),         # Fill Jug B
            (0, b),             # Empty Jug A
            (a, 0),             # Empty Jug B
            (min(a + b, jug_a), a + b - min(a + b, jug_a)),  # Pour B -> A
            (a + b - min(a + b, jug_b), min(a + b, jug_b))   # Pour A -> B
        ]

        for move in moves:
            if move not in visited:
                stack.append(move)


if __name__ == "__main__":
    water_jug_problem()
