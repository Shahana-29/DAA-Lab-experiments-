def is_safe(board, row, col):
    # Check previous rows
    for prev_row in range(row):
        placed = board[prev_row]

        # Same column
        if placed == col:
            return False

        # Same diagonal
        if abs(prev_row - row) == abs(placed - col):
            return False

    return True


def solve_n_queens(n):
    board = [-1] * n
    solutions = []
    backtrack_count = [0]

    def backtrack(row):

        if row == n:
            solutions.append(board[:])
            return

        for col in range(n):

            if is_safe(board, row, col):
                board[row] = col

                backtrack(row + 1)

                # Backtrack
                board[row] = -1
                backtrack_count[0] += 1

    # Start solving
    backtrack(0)

    return solutions, backtrack_count[0]


def display_board(solution, n):

    print(" +" + "---+" * n)

    for row in range(n):

        print(" |", end="")

        for col in range(n):

            if solution[row] == col:
                print(" Q |", end="")
            else:
                print(" . |", end="")

        print()
        print(" +" + "---+" * n)


# ---------------- Main Program ----------------

# Changed input values
for n in [5, 7]:

    solutions, backtracks = solve_n_queens(n)

    print(f"\nN = {n}")
    print(f"Total Solutions : {len(solutions)}")
    print(f"Backtracks      : {backtracks}")

    # Display only the first solution for N = 5
    if n == 5:
        print("\nFirst Solution:\n")
        display_board(solutions[0], n)
