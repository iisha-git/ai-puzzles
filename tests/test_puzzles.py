import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from puzzles import eight_puzzle, hanoi, knights_tour, missionaries, n_queens, sudoku, tic_tac_toe, water_jug


def test_queens():
    s = n_queens.solve(8)
    assert len(set(s)) == 8
    assert all(abs(s[i] - s[j]) != j - i for i in range(8) for j in range(i + 1, 8))
    assert n_queens.count_solutions(6) == 4 and n_queens.count_solutions(8) == 92
    assert n_queens.solve(3) is None


def test_eight_puzzle():
    start = (1, 2, 3, 4, 0, 6, 7, 5, 8)
    path = eight_puzzle.solve(start)
    assert len(path) == 2
    assert eight_puzzle.solve((1, 2, 3, 4, 5, 6, 8, 7, 0)) is None


def test_water_jug():
    p = water_jug.solve(3, 5, 4)
    assert p[0] == (0, 0) and 4 in p[-1] and len(p) - 1 == 6
    assert water_jug.solve(2, 4, 3) is None


def test_missionaries():
    assert len(missionaries.solve()) - 1 == 11


def test_hanoi():
    assert len(hanoi.solve(5)) == 31


def test_knights_tour():
    p = knights_tour.solve(6)
    assert len(set(p)) == 36


def test_tic_tac_toe():
    assert tic_tac_toe.best_move(list("XX OO    "), "X") == 2
    assert tic_tac_toe.best_move(list("OO X  X  "), "O") == 2


def test_sudoku():
    g = [[5,3,0,0,7,0,0,0,0],[6,0,0,1,9,5,0,0,0],[0,9,8,0,0,0,0,6,0],[8,0,0,0,6,0,0,0,3],[4,0,0,8,0,3,0,0,1],[7,0,0,0,2,0,0,0,6],[0,6,0,0,0,0,2,8,0],[0,0,0,4,1,9,0,0,5],[0,0,0,0,8,0,0,7,9]]
    s = sudoku.solve(g)
    assert all(sorted(r) == list(range(1, 10)) for r in s)
    assert all(sorted(s[r][c] for r in range(9)) == list(range(1, 10)) for c in range(9))
