"""N-Queens via backtracking with column/diagonal sets."""


def solve(n=8):
    """Return one solution as a list where index = row and value = column, or None."""
    cols, d1, d2, board = set(), set(), set(), []

    def place(r):
        if r == n:
            return True
        for c in range(n):
            if c in cols or (r - c) in d1 or (r + c) in d2:
                continue
            cols.add(c); d1.add(r - c); d2.add(r + c); board.append(c)
            if place(r + 1):
                return True
            cols.remove(c); d1.remove(r - c); d2.remove(r + c); board.pop()
        return False

    return list(board) if place(0) else None


def count_solutions(n):
    def go(r, cols, d1, d2):
        if r == n:
            return 1
        total = 0
        for c in range(n):
            if c in cols or (r - c) in d1 or (r + c) in d2:
                continue
            total += go(r + 1, cols | {c}, d1 | {r - c}, d2 | {r + c})
        return total
    return go(0, frozenset(), frozenset(), frozenset())
