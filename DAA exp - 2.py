import random


# ---------------- Naive Search ----------------
def naiveSearch(text, pattern):

    textLength = len(text)
    patternLength = len(pattern)

    matchIndex = []
    comparisonCount = 0

    for i in range(textLength - patternLength + 1):

        found = True

        for j in range(patternLength):
            comparisonCount += 1

            if text[i + j] != pattern[j]:
                found = False
                break

        if found:
            matchIndex.append(i)

    return matchIndex, comparisonCount


# ---------------- LPS Table ----------------
def createLPS(pattern):

    lps = [0] * len(pattern)

    length = 0
    i = 1

    while i < len(pattern):

        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1

        elif length != 0:
            length = lps[length - 1]

        else:
            lps[i] = 0
            i += 1

    return lps


# ---------------- KMP Search ----------------
def kmpSearch(text, pattern):

    lps = createLPS(pattern)

    textPointer = 0
    patternPointer = 0

    matchIndex = []
    comparisonCount = 0

    while textPointer < len(text):

        comparisonCount += 1

        if text[textPointer] == pattern[patternPointer]:

            textPointer += 1
            patternPointer += 1

            if patternPointer == len(pattern):
                matchIndex.append(textPointer - patternPointer)
                patternPointer = lps[patternPointer - 1]

        else:

            if patternPointer != 0:
                patternPointer = lps[patternPointer - 1]
            else:
                textPointer += 1

    return matchIndex, comparisonCount


# ---------------- Rabin-Karp ----------------
def rabinKarp(text, pattern):

    base = 256
    prime = 101

    n = len(text)
    m = len(pattern)

    patternHash = 0
    textHash = 0

    highestPower = pow(base, m - 1, prime)

    matchIndex = []
    comparisonCount = 0

    for i in range(m):
        patternHash = (base * patternHash + ord(pattern[i])) % prime
        textHash = (base * textHash + ord(text[i])) % prime

    for i in range(n - m + 1):

        if patternHash == textHash:

            matched = True

            for j in range(m):
                comparisonCount += 1

                if text[i + j] != pattern[j]:
                    matched = False
                    break

            if matched:
                matchIndex.append(i)

        if i < n - m:
            textHash = (
                base * (textHash - ord(text[i]) * highestPower)
                + ord(text[i + m])
            ) % prime

            if textHash < 0:
                textHash += prime

    return matchIndex, comparisonCount


# ---------------- Performance Comparison ----------------
def performanceTest():

    largeText = "".join(random.choices("ABCDE", k=12000))

    patterns = [
        "ABC",
        "BCDA",
        "ABCDEA",
        "ABCDEABC"
    ]

    print("\nPerformance Analysis")
    print("-" * 55)
    print("{:<12}{:<10}{:<10}{:<10}".format(
        "Pattern",
        "Naive",
        "KMP",
        "RK"
    ))
    print("-" * 55)

    for p in patterns:

        _, naiveCount = naiveSearch(largeText, p)
        _, kmpCount = kmpSearch(largeText, p)
        _, rkCount = rabinKarp(largeText, p)

        print("{:<12}{:<10}{:<10}{:<10}".format(
            p,
            naiveCount,
            kmpCount,
            rkCount
        ))


# ---------------- Main ----------------
def main():

    # Changed sample input
    text = "COMPUTERSCIENCECOMPUTER"
    pattern = "COM"

    print("Pattern Matching Algorithms")
    print("---------------------------")
    print("Text    :", text)
    print("Pattern :", pattern)

    naiveResult, naiveComp = naiveSearch(text, pattern)
    kmpResult, kmpComp = kmpSearch(text, pattern)
    rkResult, rkComp = rabinKarp(text, pattern)

    print("\nNaive Search")
    print("Match Positions :", naiveResult)
    print("Comparisons     :", naiveComp)

    print("\nKMP Search")
    print("Match Positions :", kmpResult)
    print("Comparisons     :", kmpComp)

    print("\nRabin-Karp Search")
    print("Match Positions :", rkResult)
    print("Comparisons     :", rkComp)

    performanceTest()


if __name__ == "__main__":
    main()
