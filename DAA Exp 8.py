from itertools import permutations

INF = float("inf")


def reduce_matrix(matrix):
    """
    Perform row and column reduction on a cost matrix.
    Returns:
        reduced_matrix, reduction_cost
    """
    reduced = [row[:] for row in matrix]
    size = len(reduced)
    reduction_cost = 0

    # ---------- Row Reduction ----------
    for i in range(size):
        row_min = min(reduced[i])
        if row_min != INF and row_min > 0:
            reduction_cost += row_min
            for j in range(size):
                if reduced[i][j] != INF:
                    reduced[i][j] -= row_min

    # ---------- Column Reduction ----------
    for j in range(size):
        col_min = min(reduced[i][j] for i in range(size))
        if col_min != INF and col_min > 0:
            reduction_cost += col_min
            for i in range(size):
                if reduced[i][j] != INF:
                    reduced[i][j] -= col_min

    return reduced, reduction_cost


def tsp_brute_force(cost_matrix):
    """
    Finds the optimal TSP tour using brute-force.
    Returns:
        best_path, minimum_cost
    """
    n = len(cost_matrix)
    cities = list(range(1, n))

    minimum_cost = INF
    best_path = []

    for perm in permutations(cities):
        current_path = [0] + list(perm) + [0]

        current_cost = sum(
            cost_matrix[current_path[i]][current_path[i + 1]]
            for i in range(n)
        )

        if current_cost < minimum_cost:
            minimum_cost = current_cost
            best_path = current_path

    return best_path, minimum_cost


def display_matrix(matrix, labels):
    """Print the cost matrix neatly."""
    print("5-City TSP - Cost Matrix\n")

    print(f'{"":>5}', end="")
    for city in labels:
        print(f"{city:>6}", end="")
    print()

    for i, row in enumerate(matrix):
        print(f"{labels[i]:>5}", end="")
        for value in row:
            print(f'{"INF" if value == INF else value:>6}', end="")
        print()


def display_path(path, labels, matrix):
    """Display the optimal path with edge costs."""
    print("\nOptimal Tour:")
    print(" -> ".join(labels[i] for i in path))

    total_cost = sum(matrix[path[i]][path[i + 1]]
                     for i in range(len(path) - 1))

    print(f"\nMinimum Cost : {total_cost}")

    print("\nPath Verification")
    print("-" * 35)

    for i in range(len(path) - 1):
        u, v = path[i], path[i + 1]
        print(f"{labels[u]} -> {labels[v]} : {matrix[u][v]}")


# ---------------- MAIN PROGRAM ---------------- #

cost = [
    [INF, 10, 8, 9, 7],
    [10, INF, 10, 5, 6],
    [8, 10, INF, 8, 9],
    [9, 5, 8, INF, 6],
    [7, 6, 9, 6, INF]
]

city_names = ["A", "B", "C", "D", "E"]

display_matrix(cost, city_names)

reduced_matrix, reduction_cost = reduce_matrix(cost)

print("\nInitial Matrix Reduction Cost :", reduction_cost)

best_path, minimum_cost = tsp_brute_force(cost)

display_path(best_path, city_names, cost)
