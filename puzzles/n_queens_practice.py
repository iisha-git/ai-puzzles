N = 8

def solve_queens():
    positions = [-1] * N
    solutions = []

    def backtrack(col):
        if col == N:
            solutions.append(positions.copy())
            return

        for row in range(N):
            safe = True

            for previous_col in range(col):
                previous_row = positions[previous_col]

                if (previous_row == row or
                    abs(previous_row - row) == abs(previous_col - col)):
                    safe = False
                    break

            if safe:
                positions[col] = row

                backtrack(col + 1)

                positions[col] = -1

    backtrack(0)
    return solutions


def print_board(solution):
    for row in range(N):
        print(" ".join(
            "Q" if solution[col] == row else "."
            for col in range(N)
        ))


if __name__ == "__main__":
    all_solutions = solve_queens()

    print("Number of solutions:", len(all_solutions))

    print("First solution:")
    print_board(all_solutions[0])
