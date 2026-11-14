"""8-puzzle solved with A* and the Manhattan distance heuristic."""
import heapq

GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)


def _manhattan(state):
    total = 0
    for i, v in enumerate(state):
        if v:
            g = v - 1
            total += abs(i // 3 - g // 3) + abs(i % 3 - g % 3)
    return total


def is_solvable(state):
    tiles = [v for v in state if v]
    inversions = sum(1 for i in range(8) for j in range(i + 1, 8) if tiles[i] > tiles[j])
    return inversions % 2 == 0


def _neighbors(state):
    z = state.index(0)
    r, c = divmod(z, 3)
    for dr, dc, name in ((-1, 0, "up"), (1, 0, "down"), (0, -1, "left"), (0, 1, "right")):
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            s = list(state)
            s[z], s[nr * 3 + nc] = s[nr * 3 + nc], 0
            yield tuple(s), name


def solve(start):
    """Return the shortest list of moves (blank direction) or None if unsolvable."""
    start = tuple(start)
    if not is_solvable(start):
        return None
    frontier = [(_manhattan(start), 0, start, [])]
    best = {start: 0}
    while frontier:
        _, g, state, path = heapq.heappop(frontier)
        if state == GOAL:
            return path
        for nxt, move in _neighbors(state):
            if g + 1 < best.get(nxt, 1 << 30):
                best[nxt] = g + 1
                heapq.heappush(frontier, (g + 1 + _manhattan(nxt), g + 1, nxt, path + [move]))
    return None
