import sys
input = sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, a, b):
    rootA = find(parent, a)
    rootB = find(parent, b)

    if rootA != rootB:
        if rank[rootA] > rank[rootB]:
            parent[rootB] = rootA
        elif rank[rootA] < rank[rootB]:
            parent[rootA] = rootB
        else:
            parent[rootB] = rootA
            rank[rootA] += 1

def kruskal(V, edges):
    mst_weight = 0
    parent = [i for i in range(V + 1)]
    rank = [0] * (V + 1)

    edges.sort(key=lambda x: x[2])

    for a, b, weight in edges:
        if find(parent, a) != find(parent, b):
            union(parent, rank, a, b)
            mst_weight += weight

    return mst_weight

V, E = map(int, input().split())
edges = []

for _ in range(E):
    A, B, C = map(int, input().split())
    edges.append((A, B, C))

print(kruskal(V, edges))