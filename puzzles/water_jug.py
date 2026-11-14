"""Water jug puzzle solved with BFS (fewest steps)."""
from collections import deque
from math import gcd


def solve(cap_a, cap_b, target):
    """Return a list of (a, b) states from (0, 0) to a state holding target, or None."""
    if target > max(cap_a, cap_b) or target % gcd(cap_a, cap_b):
        return None
    start = (0, 0)
    prev = {start: None}
    q = deque([start])
    while q:
        a, b = q.popleft()
        if target in (a, b):
            path, s = [], (a, b)
            while s is not None:
                path.append(s)
                s = prev[s]
            return path[::-1]
        pour_ab = min(a, cap_b - b)
        pour_ba = min(b, cap_a - a)
        for s in ((cap_a, b), (a, cap_b), (0, b), (a, 0),
                  (a - pour_ab, b + pour_ab), (a + pour_ba, b - pour_ba)):
            if s not in prev:
                prev[s] = (a, b)
                q.append(s)
    return None
