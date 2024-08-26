from itertools import combinations
from collections import deque

inputArray = [list(input().strip()) for _ in range(5)]

indices = [(i, j) for i in range(5) for j in range(5)]
count = 0

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def is_connected(group):
    queue = deque([group[0]])
    visited = set([group[0]])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (nx, ny) in group and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny))
    return len(visited) == 7

for group in combinations(indices, 7):
    s_count = sum(1 for x, y in group if inputArray[x][y] == 'S')
    if s_count >= 4 and is_connected(group):
        count += 1

print(count)