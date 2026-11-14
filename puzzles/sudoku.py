"""Sudoku as a constraint satisfaction problem: MRV heuristic plus backtracking."""


def _peers():
    peers = {}
    for r in range(9):
        for c in range(9):
            p = {(r, k) for k in range(9)} | {(k, c) for k in range(9)}
            br, bc = r // 3 * 3, c // 3 * 3
            p |= {(br + i, bc + j) for i in range(3) for j in range(3)}
            p.discard((r, c))
            peers[(r, c)] = p
    return peers


PEERS = _peers()


def solve(grid):
    """grid: 9x9 list of ints, 0 = empty. Returns a solved grid or None."""
    g = [row[:] for row in grid]

    def options(r, c):
        used = {g[pr][pc] for pr, pc in PEERS[(r, c)]}
        return [v for v in range(1, 10) if v not in used]

    for r in range(9):
        for c in range(9):
            if g[r][c] and g[r][c] in {g[pr][pc] for pr, pc in PEERS[(r, c)]}:
                return None

    def go():
        best, best_opts = None, None
        for r in range(9):
            for c in range(9):
                if g[r][c] == 0:
                    o = options(r, c)
                    if not o:
                        return False
                    if best_opts is None or len(o) < len(best_opts):
                        best, best_opts = (r, c), o
        if best is None:
            return True
        r, c = best
        for v in best_opts:
            g[r][c] = v
            if go():
                return True
        g[r][c] = 0
        return False

    return g if go() else None
