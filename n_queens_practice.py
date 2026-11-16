n = 8

col = []
posDiag = []
negDiag = []

res = []
board = [["."] * n for i in range(n)]

def backtrack(r):

    if r == n:
        copy = ["".join(row) for row in board]
        res.append(copy)
        return

    for c in range(n):

        if c in col or (r + c) in posDiag or (r - c) in negDiag:
            continue

        col.append(c)
        posDiag.append(r + c)
        negDiag.append(r - c)

        board[r][c] = "Q"

        backtrack(r + 1)

        col.remove(c)
        posDiag.remove(r + c)
        negDiag.remove(r - c)
        board[r][c] = "."

backtrack(0)

print("Number of solutions:", len(res))
print("First solution:")

for row in res[0]:
    print(row)
