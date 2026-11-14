"""Tic-tac-toe with minimax and alpha-beta pruning. The AI never loses."""

LINES = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]


def winner(board):
    for a, b, c in LINES:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]
    return None


def _score(board, player, me, alpha=-2, beta=2):
    w = winner(board)
    if w:
        return 1 if w == me else -1
    if " " not in board:
        return 0
    other = "O" if player == "X" else "X"
    maximizing = player == me
    best = -2 if maximizing else 2
    for i in range(9):
        if board[i] == " ":
            board[i] = player
            s = _score(board, other, me, alpha, beta)
            board[i] = " "
            if maximizing:
                best = max(best, s); alpha = max(alpha, best)
            else:
                best = min(best, s); beta = min(beta, best)
            if beta <= alpha:
                break
    return best


def best_move(board, player):
    """board: list of 9 chars ('X', 'O', ' '). Returns the index of the best move."""
    other = "O" if player == "X" else "X"
    scored = []
    for i in range(9):
        if board[i] == " ":
            board[i] = player
            scored.append((_score(board, other, player), -i, i))
            board[i] = " "
    return max(scored)[2]
