"""Run every puzzle: python main.py"""
from puzzles import eight_puzzle, hanoi, knights_tour, missionaries, n_queens, sudoku, tic_tac_toe, water_jug

print("8-Queens:", n_queens.solve(8))
print("8-puzzle moves:", eight_puzzle.solve((1, 2, 3, 4, 0, 6, 7, 5, 8)))
print("Water jug 3L/5L -> 4L:", water_jug.solve(3, 5, 4))
print("Missionaries & cannibals steps:", len(missionaries.solve()) - 1)
print("Hanoi (4 disks) moves:", len(hanoi.solve(4)))
print("Knight's tour 6x6 length:", len(knights_tour.solve(6)))
board = list("XX OO    ")
print("Tic-tac-toe, X to move, best square:", tic_tac_toe.best_move(board, "X"))
puzzle = [[5,3,0,0,7,0,0,0,0],[6,0,0,1,9,5,0,0,0],[0,9,8,0,0,0,0,6,0],[8,0,0,0,6,0,0,0,3],[4,0,0,8,0,3,0,0,1],[7,0,0,0,2,0,0,0,6],[0,6,0,0,0,0,2,8,0],[0,0,0,4,1,9,0,0,5],[0,0,0,0,8,0,0,7,9]]
print("Sudoku:")
for row in sudoku.solve(puzzle):
    print(" ".join(map(str, row)))
