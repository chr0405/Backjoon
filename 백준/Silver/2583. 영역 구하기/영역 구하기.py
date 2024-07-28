import sys
from collections import deque

M, N, K = map(int, sys.stdin.readline().split())
rectangles = [list(map(int, sys.stdin.readline().split())) for _ in range(K)]

grid = [[0] * M for _ in range(N)]

def BFS(x, y, grid):
    queue = deque([[x, y]])
    grid[x][y] = 1
    area = 0

    # 상하좌우
    offsetX = [0, 0, -1, 1]
    offsetY = [1, -1, 0, 0]

    while queue:
        startX, startY = queue.popleft()
        area += 1

        for offset in range(4):
            testX, testY = startX + offsetX[offset], startY + offsetY[offset]
            if 0 <= testX < N and 0 <= testY < M and grid[testX][testY] == 0:
                grid[testX][testY] = 1
                queue.append([testX, testY])
    
    return area

for rectangle in rectangles:
    x1, y1, x2, y2 = rectangle

    for x in range(x1, x2):
        for y in range(y1, y2):
            grid[x][y] = 1
    
areas = []

for x in range(N):
    for y in range(M):
        if grid[x][y] == 0:
            area = BFS(x, y, grid)
            areas.append(area)

areas.sort()

print(len(areas))
print(' '.join(map(str, areas)))