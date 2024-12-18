from collections import deque

m, n, h = map(int, input().split())
graph = []
queue = deque()

for i in range(h):
    layer = []
    for j in range(n):
        row = list(map(int, input().split()))
        for k in range(m):
            if row[k] == 1:
                queue.append((i, j, k))
        layer.append(row)
    graph.append(layer)

directions = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]

while queue:
    x, y, z = queue.popleft()
    for dx, dy, dz in directions:
        nx, ny, nz = x + dx, y + dy, z + dz
        if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m and graph[nx][ny][nz] == 0:
            graph[nx][ny][nz] = graph[x][y][z] + 1
            queue.append((nx, ny, nz))

result = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 0:
                print(-1)
                exit(0)
            result = max(result, graph[i][j][k])

print(result - 1)
