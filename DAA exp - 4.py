import heapq


# ---------------- Dijkstra Algorithm ----------------
def dijkstraAlgorithm(network, source):

    totalVertices = len(network)

    shortestDistance = [float("inf")] * totalVertices
    previousVertex = [-1] * totalVertices
    isVisited = [False] * totalVertices

    shortestDistance[source] = 0

    priorityQueue = [(0, source)]

    while priorityQueue:

        currentDistance, currentVertex = heapq.heappop(priorityQueue)

        if isVisited[currentVertex]:
            continue

        isVisited[currentVertex] = True

        for nextVertex, edgeWeight in network[currentVertex]:

            newDistance = currentDistance + edgeWeight

            if newDistance < shortestDistance[nextVertex]:

                shortestDistance[nextVertex] = newDistance
                previousVertex[nextVertex] = currentVertex

                heapq.heappush(priorityQueue, (newDistance, nextVertex))

    return shortestDistance, previousVertex


# ---------------- Display Path ----------------
def displayPath(previousVertex, source, destination):

    path = []

    while destination != -1:
        path.append(destination)
        destination = previousVertex[destination]

    path.reverse()

    if path and path[0] == source:
        return path

    return []


# ---------------- Main ----------------
def main():

    # Modified Input Graph
    network = {
        0: [(1, 2), (2, 7)],
        1: [(2, 3), (3, 4)],
        2: [(3, 2), (4, 6)],
        3: [(4, 1), (5, 5)],
        4: [(5, 2), (6, 4)],
        5: [(6, 3)],
        6: []
    }

    sourceVertex = 0

    distance, previous = dijkstraAlgorithm(network, sourceVertex)

    print("Shortest Path Using Dijkstra's Algorithm")
    print("=" * 68)

    print("{:<10}{:<12}{}".format("Vertex", "Distance", "Path"))
    print("-" * 68)

    for vertex in range(len(network)):

        route = displayPath(previous, sourceVertex, vertex)

        if route:
            path = " -> ".join(map(str, route))
        else:
            path = "No Path"

        cost = (
            distance[vertex]
            if distance[vertex] != float("inf")
            else "INF"
        )

        print("{:<10}{:<12}{}".format(vertex, cost, path))


if __name__ == "__main__":
    main()
