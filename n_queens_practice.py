n = 8

def solve(row, queens, solutions):

    if row == n:
        solutions.append(queens.copy())
        return

    for col in range(n):

        if all(col != c and abs(col-c) != row-r
               for r, c in enumerate(queens)):

            queens.append(col)

            solve(row+1, queens, solutions)

            queens.pop()


def print_board(solution):

    for row in range(n):
        print(" ".join(
            "Q" if solution[row] == col else "."
            for col in range(n)
        ))


queens = []
solutions = []

solve(0, queens, solutions)

print("Number of solutions:", len(solutions))
print("First solution:")
print_board(solutions[0])
