INF = float("inf")


def first_fit(items, capacity=1.0):
    """First Fit Bin Packing Algorithm"""
    remaining_space = []
    bins = []

    for item in items:
        allocated = False

        for i in range(len(remaining_space)):
            if remaining_space[i] >= item:
                remaining_space[i] -= item
                bins[i].append(item)
                allocated = True
                break

        if not allocated:
            remaining_space.append(capacity - item)
            bins.append([item])

    return bins


def first_fit_decreasing(items, capacity=1.0):
    """First Fit Decreasing (FFD)"""
    sorted_items = sorted(items, reverse=True)
    return first_fit(sorted_items, capacity)


def best_fit_decreasing(items, capacity=1.0):
    """Best Fit Decreasing (BFD)"""
    sorted_items = sorted(items, reverse=True)

    remaining_space = []
    bins = []

    for item in sorted_items:
        best_bin = -1
        minimum_space = INF

        for i in range(len(remaining_space)):
            if remaining_space[i] >= item:
                leftover = remaining_space[i] - item
                if leftover < minimum_space:
                    minimum_space = leftover
                    best_bin = i

        if best_bin == -1:
            remaining_space.append(capacity - item)
            bins.append([item])
        else:
            remaining_space[best_bin] -= item
            bins[best_bin].append(item)

    return bins


def print_bins(title, bins):
    """Display bins with utilization"""
    print(f"\n{title}")
    print("-" * 45)
    print(f"Total Bins Used : {len(bins)}\n")

    for index, current_bin in enumerate(bins, start=1):
        used = sum(current_bin)
        free = 1.0 - used
        graph = "█" * int(used * 20)

        print(f"Bin {index}")
        print(f" Items      : {current_bin}")
        print(f" Used Space : {used:.1f}")
        print(f" Free Space : {free:.1f}")
        print(f" [{graph:<20}]")
        print()


# ---------------- MAIN PROGRAM ---------------- #

items = [0.5, 0.7, 0.3, 0.9, 0.2, 0.6, 0.8, 0.4, 0.1, 0.5]
capacity = 1.0

total_size = sum(items)
lower_bound = int(-(-total_size // capacity))   # Ceiling Division

print("Efficient Bin Packing using Approximation Algorithms")
print("=" * 55)

print(f"Items            : {items}")
print(f"Bin Capacity     : {capacity}")
print(f"Total Item Size  : {total_size:.1f}")
print(f"Lower Bound Bins : {lower_bound}")

# Apply Algorithms
ff_result = first_fit(items, capacity)
ffd_result = first_fit_decreasing(items, capacity)
bfd_result = best_fit_decreasing(items, capacity)

# Display Results
print_bins("First Fit (FF)", ff_result)
print_bins("First Fit Decreasing (FFD)", ffd_result)
print_bins("Best Fit Decreasing (BFD)", bfd_result)

# Summary
print("=" * 55)
print("SUMMARY")
print("-" * 55)
print(f"Lower Bound              : {lower_bound}")
print(f"First Fit (FF)           : {len(ff_result)} bins")
print(f"First Fit Decreasing     : {len(ffd_result)} bins")
print(f"Best Fit Decreasing      : {len(bfd_result)} bins")
