"""Knight's tour using Warnsdorff's heuristic."""

MOVES = [(1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1)]


def solve(n=8, start=(0, 0)):
    """Return a list of squares visiting every square once, or None."""
    visited = {start}
    path = [start]

    def nxt(p):
        return [(p[0] + dr, p[1] + dc) for dr, dc in MOVES
                if 0 <= p[0] + dr < n and 0 <= p[1] + dc < n and (p[0] + dr, p[1] + dc) not in visited]

    def go(p):
        if len(path) == n * n:
            return True
        for q in sorted(nxt(p), key=lambda s: len(nxt(s))):
            visited.add(q); path.append(q)
            if go(q):
                return True
            visited.discard(q); path.pop()
        return False

    return path if go(start) else None
