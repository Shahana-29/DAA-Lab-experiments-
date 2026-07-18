import random

comparisonCount = 0


# ---------------- Divide and Conquer ----------------
def divideConquerMinMax(values, start, end):

    global comparisonCount

    # Only one element
    if start == end:
        return values[start], values[start]

    # Two elements
    if end == start + 1:

        comparisonCount += 1

        if values[start] < values[end]:
            return values[start], values[end]

        return values[end], values[start]

    # Divide into two halves
    middle = (start + end) // 2

    leftMin, leftMax = divideConquerMinMax(values, start, middle)
    rightMin, rightMax = divideConquerMinMax(values, middle + 1, end)

    # Combine the results
    comparisonCount += 1
    minimumValue = leftMin if leftMin < rightMin else rightMin

    comparisonCount += 1
    maximumValue = leftMax if leftMax > rightMax else rightMax

    return minimumValue, maximumValue


# ---------------- Naive Method ----------------
def normalMinMax(values):

    minimumValue = values[0]
    maximumValue = values[0]

    comparisons = 0

    for number in values[1:]:

        comparisons += 1
        if number < minimumValue:
            minimumValue = number

        comparisons += 1
        if number > maximumValue:
            maximumValue = number

    return minimumValue, maximumValue, comparisons


# ---------------- Performance Analysis ----------------
def compareMethods():

    global comparisonCount

    testCases = [10, 100, 1000, 10000]

    print("\nPerformance Analysis")
    print("-" * 65)
    print("{:<10}{:<18}{:<18}{:<15}".format(
        "Size",
        "D&C Count",
        "Naive Count",
        "Expected"
    ))
    print("-" * 65)

    for size in testCases:

        values = [random.randint(10, 9999) for i in range(size)]

        comparisonCount = 0

        divideConquerMinMax(values, 0, len(values) - 1)

        divideCount = comparisonCount

        _, _, naiveCount = normalMinMax(values)

        expectedCount = (3 * size // 2) - 2

        print("{:<10}{:<18}{:<18}{:<15}".format(
            size,
            divideCount,
            naiveCount,
            expectedCount
        ))


# ---------------- Main ----------------
def main():

    global comparisonCount

    # Modified Sample Input
    values = [27, 11, 48, 5, 33, 19, 62, 8, 41, 14]

    comparisonCount = 0

    minimumValue, maximumValue = divideConquerMinMax(
        values, 0, len(values) - 1
    )

    divideCount = comparisonCount

    _, _, naiveCount = normalMinMax(values)

    print("Minimum and Maximum using Divide & Conquer")
    print("=" * 55)

    print("Input Array :", values)
    print("Minimum     :", minimumValue)
    print("Maximum     :", maximumValue)

    print("\nComparison Count")
    print("Divide & Conquer :", divideCount)
    print("Naive Method     :", naiveCount)

    compareMethods()


if __name__ == "__main__":
    main()
