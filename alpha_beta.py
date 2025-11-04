
Alpha–Beta Pruning Implementation in Minimax Algorithm
------------------------------------------------------

AIM:
To demonstrate how Alpha–Beta Pruning optimizes Minimax by pruning
unnecessary branches in a decision tree.
"""


def minimax(depth, node_index, maximizing_player, values, alpha, beta, max_depth):
    """
    Recursive function to perform Minimax with Alpha–Beta Pruning.
    """
    # Base Case: Leaf node reached
    if depth == max_depth:
        return values[node_index]

    if maximizing_player:
        best = float('-inf')

        # Explore left and right children
        for i in range(2):
            val = minimax(depth + 1, node_index * 2 + i, False, values, alpha, beta, max_depth)
            best = max(best, val)
            alpha = max(alpha, best)

            # Beta Cutoff
            if beta <= alpha:
                break
        return best

    else:
        best = float('inf')

        # Explore left and right children
        for i in range(2):
            val = minimax(depth + 1, node_index * 2 + i, True, values, alpha, beta, max_depth)
            best = min(best, val)
            beta = min(beta, best)

            # Alpha Cutoff
            if beta <= alpha:
                break
        return best


if __name__ == "__main__":
    # Example binary game tree with 8 leaf nodes (3 levels deep)
    values = [3, 5, 6, 9, 1, 2, 0, -1]
    depth = 0
    node_index = 0
    max_depth = 3

    print("Leaf Node Values:", values)
    optimal_value = minimax(depth, node_index, True, values, float('-inf'), float('inf'), max_depth)
    print("\nThe Optimal Value (with Alpha–Beta Pruning) is:", optimal_value)
