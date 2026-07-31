import random
import time
import sys

# Increase recursion depth for large inputs
sys.setrecursionlimit(20000)

comparison_count = 0


def partition(arr, low, high):
    """Partition the array using the last element as pivot."""
    global comparison_count

    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        comparison_count += 1

        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def deterministic_quick_sort(arr, low, high):
    """Standard Quick Sort using last element as pivot."""
    if low < high:
        pivot_index = partition(arr, low, high)

        deterministic_quick_sort(arr, low, pivot_index - 1)
        deterministic_quick_sort(arr, pivot_index + 1, high)


def randomized_quick_sort(arr, low, high):
    """Randomized Quick Sort."""
    if low < high:

        # Select a random pivot
        random_index = random.randint(low, high)
        arr[random_index], arr[high] = arr[high], arr[random_index]

        pivot_index = partition(arr, low, high)

        randomized_quick_sort(arr, low, pivot_index - 1)
        randomized_quick_sort(arr, pivot_index + 1, high)


def evaluate_algorithm(sort_function, data):
    """Run sorting algorithm and measure comparisons & execution time."""
    global comparison_count

    temp = data[:]
    comparison_count = 0

    start = time.perf_counter()

    sort_function(temp, 0, len(temp) - 1)

    elapsed = (time.perf_counter() - start) * 1000

    return comparison_count, elapsed


# ---------------------- MAIN PROGRAM ---------------------- #

SIZE = 5000

test_cases = {
    "Random": [random.randint(1, 100000) for _ in range(SIZE)],
    "Sorted": list(range(SIZE)),
    "Reverse": list(range(SIZE, 0, -1)),
    "Nearly Sorted": list(range(SIZE))
}

# Slightly shuffle the nearly sorted list
nearly_sorted = test_cases["Nearly Sorted"]

for _ in range(SIZE // 20):
    i = random.randint(0, SIZE - 1)
    j = random.randint(0, SIZE - 1)
    nearly_sorted[i], nearly_sorted[j] = nearly_sorted[j], nearly_sorted[i]

print("\nImproving Quick Sort Efficiency using Randomized Algorithm")
print("=" * 90)

print(f'{"Input Type":<18}'
      f'{"DQS Comparisons":>18}'
      f'{"DQS Time(ms)":>15}'
      f'{"RQS Comparisons":>18}'
      f'{"RQS Time(ms)":>15}')

print("-" * 90)

for case_name, data in test_cases.items():

    dqs_comp, dqs_time = evaluate_algorithm(
        deterministic_quick_sort, data)

    rqs_comp, rqs_time = evaluate_algorithm(
        randomized_quick_sort, data)

    print(f"{case_name:<18}"
          f"{dqs_comp:>18}"
          f"{dqs_time:>15.2f}"
          f"{rqs_comp:>18}"
          f"{rqs_time:>15.2f}")

print("=" * 90)
print("DQS : Deterministic Quick Sort")
print("RQS : Randomized Quick Sort")
