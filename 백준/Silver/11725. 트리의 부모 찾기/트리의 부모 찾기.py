import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n + 1)]
parents = [0] * (n + 1)

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque([1])
while queue:
    node = queue.popleft()
    for neighbor in graph[node]:
        if parents[neighbor] == 0:
            parents[neighbor] = node
            queue.append(neighbor)

print("\n".join(map(str, parents[2:])))
