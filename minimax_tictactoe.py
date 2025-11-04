
Minimax Algorithm – Tic Tac Toe
-------------------------------
A simple Python implementation where the computer uses
the Minimax algorithm to play an optimal game of Tic-Tac-Toe.
"""

import math

# Define players
HUMAN = 'X'
AI = 'O'
EMPTY = '_'


def print_board(board):
    for row in board:
        print(' | '.join(row))
    print()


def check_winner(board):
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    return None


def is_moves_left(board):
    for row in board:
        if EMPTY in row:
            return True
    return False


def evaluate(board):
    winner = check_winner(board)
    if winner == AI:
        return 1
    elif winner == HUMAN:
        return -1
    else:
        return 0


def minimax(board, depth, is_maximizing):
    score = evaluate(board)

    # Terminal conditions
    if score == 1 or score == -1:
        return score
    if not is_moves_left(board):
        return 0

    if is_maximizing:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = AI
                    best = max(best, minimax(board, depth + 1, False))
                    board[i][j] = EMPTY
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = HUMAN
                    best = min(best, minimax(board, depth + 1, True))
                    board[i][j] = EMPTY
        return best


def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = AI
                move_val = minimax(board, 0, False)
                board[i][j] = EMPTY
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val
    return best_move


if __name__ == "__main__":
    board = [
        ['X', 'O', 'X'],
        ['_', 'X', 'O'],
        ['O', '_', '_']
    ]

    print("Current Board:")
    print_board(board)

    move = find_best_move(board)
    print(f"Computer chooses position: {move}")

    if move != (-1, -1):
        board[move[0]][move[1]] = AI
        print("\nUpdated Board:")
        print_board(board)

    result = check_winner(board)
    if result:
        print(f"{result} wins!")
    elif not is_moves_left(board):
        print("It's a draw!")
    else:
        print("Game continues...")
