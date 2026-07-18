import random
import time


# ---------------- Interpolation Search ----------------
def interpolationSearch(numbers, element):
    start = 0
    end = len(numbers) - 1
    count = 0

    while start <= end and numbers[start] <= element <= numbers[end]:
        count += 1

        if start == end:
            if numbers[start] == element:
                return start, count
            return -1, count

        # Prevent division by zero
        if numbers[start] == numbers[end]:
            break

        # Estimate the probable position
        indexPos = start + (
            (element - numbers[start]) * (end - start)
        ) // (numbers[end] - numbers[start])

        if numbers[indexPos] == element:
            return indexPos, count

        elif numbers[indexPos] < element:
            start = indexPos + 1

        else:
            end = indexPos - 1

    return -1, count


# ---------------- Binary Search ----------------
def binarySearch(numbers, element):
    left = 0
    right = len(numbers) - 1
    count = 0

    while left <= right:
        count += 1

        middle = (left + right) // 2

        if numbers[middle] == element:
            return middle, count

        elif numbers[middle] < element:
            left = middle + 1

        else:
            right = middle - 1

    return -1, count


# ---------------- Performance Analysis ----------------
def analyzePerformance():

    testSizes = (1000, 5000, 10000, 50000, 100000)

    print("\nPerformance Comparison")
    print("-" * 80)
    print("{:<10}{:<16}{:<16}{:<18}{:<18}".format(
        "Size",
        "IS Time(ms)",
        "BS Time(ms)",
        "IS Count",
        "BS Count"
    ))
    print("-" * 80)

    for size in testSizes:

        numbers = sorted(random.sample(range(size * 10), size))
        element = random.choice(numbers)

        # Interpolation Search Timing
        startTime = time.perf_counter()

        for i in range(100):
            _, isCount = interpolationSearch(numbers, element)

        interpolationTime = ((time.perf_counter() - startTime) / 100) * 1000

        # Binary Search Timing
        startTime = time.perf_counter()

        for i in range(100):
            _, bsCount = binarySearch(numbers, element)

        binaryTime = ((time.perf_counter() - startTime) / 100) * 1000

        print("{:<10}{:<16.5f}{:<16.5f}{:<18}{:<18}".format(
            size,
            interpolationTime,
            binaryTime,
            isCount,
            bsCount
        ))


# ---------------- Main Function ----------------
def main():

    numbers = [4, 9, 15, 21, 28, 36, 44, 53, 68, 79, 91, 110]
    element = 44

    print("Interpolation Search Demonstration")
    print("----------------------------------")
    print("Array   :", numbers)
    print("Element :", element)

    position, comparisons = interpolationSearch(numbers, element)

    if position != -1:
        print("Result  : Element found at index", position)
    else:
        print("Result  : Element not found")

    print("Comparisons :", comparisons)

    analyzePerformance()


if __name__ == "__main__":
    main()
