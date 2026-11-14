# ai-puzzles

Classic AI puzzles solved in plain Python 3, no dependencies. Each solver is one short file in `puzzles/`.

| Puzzle | Technique | File |
| --- | --- | --- |
| N-Queens | Backtracking | `puzzles/n_queens.py` |
| 8-puzzle | A* with Manhattan distance | `puzzles/eight_puzzle.py` |
| Water jug | BFS | `puzzles/water_jug.py` |
| Sudoku | CSP, MRV heuristic, backtracking | `puzzles/sudoku.py` |
| Missionaries and cannibals | BFS | `puzzles/missionaries.py` |
| Tic-tac-toe | Minimax with alpha-beta pruning | `puzzles/tic_tac_toe.py` |
| Knight's tour | Warnsdorff heuristic | `puzzles/knights_tour.py` |
| Tower of Hanoi | Recursion | `puzzles/hanoi.py` |

## Run

```
python main.py          # demo of every solver
pip install pytest
pytest                  # tests
```
