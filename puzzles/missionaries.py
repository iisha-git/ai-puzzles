"""Missionaries and cannibals solved with BFS."""
from collections import deque


def solve(total=3, boat=2):
    """State = (missionaries left, cannibals left, boat on left). Returns a state path."""
    def safe(m, c):
        return (m == 0 or m >= c) and (total - m == 0 or total - m >= total - c)

    start, goal = (total, total, 1), (0, 0, 0)
    prev = {start: None}
    q = deque([start])
    while q:
        s = q.popleft()
        if s == goal:
            path = []
            while s:
                path.append(s)
                s = prev[s]
            return path[::-1]
        m, c, b = s
        sign = -1 if b else 1
        for dm in range(boat + 1):
            for dc in range(boat + 1 - dm):
                if dm + dc == 0:
                    continue
                nm, nc = m + sign * dm, c + sign * dc
                if 0 <= nm <= total and 0 <= nc <= total and safe(nm, nc):
                    n = (nm, nc, 1 - b)
                    if n not in prev:
                        prev[n] = s
                        q.append(n)
    return None
