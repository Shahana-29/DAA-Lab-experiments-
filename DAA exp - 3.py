import heapq


# ---------------- Disjoint Set ----------------
class DisjointSet:

    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, vertex):

        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])

        return self.parent[vertex]

    def union(self, u, v):

        rootU = self.find(u)
        rootV = self.find(v)

        if rootU == rootV:
            return False

        if self.rank[rootU] < self.rank[rootV]:
            rootU, rootV = rootV, rootU

        self.parent[rootV] = rootU

        if self.rank[rootU] == self.rank[rootV]:
            self.rank[rootU] += 1

        return True


# ---------------- Kruskal ----------------
def kruskalAlgorithm(vertices, edges):

    edges.sort()

    ds = DisjointSet(vertices)

    mst = []
    totalCost = 0

    for weight, u, v in edges:

        if ds.union(u, v):

            mst.append((u, v, weight))
            totalCost += weight

            if len(mst) == vertices - 1:
                break

    return mst, totalCost


# ---------------- Prim ----------------
def primAlgorithm(vertices, graph, source=0):

    visited = [False] * vertices
    minimumCost = [float("inf")] * vertices
    parent = [-1] * vertices

    minimumCost[source] = 0

    priorityQueue = [(0, source)]

    mst = []
    totalCost = 0

    while priorityQueue:

        weight, current = heapq.heappop(priorityQueue)

        if visited[current]:
            continue

        visited[current] = True

        if parent[current] != -1:
            mst.append((parent[current], current, weight))
            totalCost += weight

        for neighbour, edgeWeight in graph.get(current, []):

            if not visited[neighbour] and edgeWeight < minimumCost[neighbour]:

                minimumCost[neighbour] = edgeWeight
                parent[neighbour] = current

                heapq.heappush(priorityQueue, (edgeWeight, neighbour))

    return mst, totalCost


# ---------------- Main ----------------
def main():

    vertices = 7

    # Modified Graph
    edges = [
        (6, 0, 1),
        (4, 0, 2),
        (5, 1, 2),
        (7, 1, 3),
        (3, 2, 4),
        (8, 3, 4),
        (6, 3, 5),
        (2, 4, 5),
        (5, 4, 6),
        (4, 5, 6)
    ]

    graph = {}

    for weight, u, v in edges:
        graph.setdefault(u, []).append((v, weight))
        graph.setdefault(v, []).append((u, weight))

    kruskalResult, kruskalWeight = kruskalAlgorithm(vertices, edges[:])
    primResult, primWeight = primAlgorithm(vertices, graph)

    print("Minimum Spanning Tree")
    print("=" * 50)

    print("\nUsing Kruskal's Algorithm")
    print("-" * 30)

    for u, v, weight in kruskalResult:
        print(f"Edge {u} - {v} : {weight}")

    print("Total Weight :", kruskalWeight)

    print("\nUsing Prim's Algorithm")
    print("-" * 30)

    for u, v, weight in primResult:
        print(f"Edge {u} - {v} : {weight}")

    print("Total Weight :", primWeight)


if __name__ == "__main__":
    main()
