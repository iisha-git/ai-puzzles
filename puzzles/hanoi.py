"""Tower of Hanoi, recursive."""


def solve(n, src="A", aux="B", dst="C"):
    if n == 0:
        return []
    return solve(n - 1, src, dst, aux) + [(src, dst)] + solve(n - 1, aux, src, dst)
