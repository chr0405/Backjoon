import sys
from collections import deque

N = int(sys.stdin.readline().strip())
rectangles = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

def BFS(x, y, rectangles):
    queue = deque([[x, y]])
    rectangles[x][y] = 2
    area = 1 

    # 상하좌우
    offsetX = [0, 0, -1, 1]
    offsetY = [1, -1, 0, 0]

    while queue:
        startX, startY = queue.popleft()

        for offset in range(4):
            testX, testY = startX + offsetX[offset], startY + offsetY[offset]
            if 0 <= testX < N and 0 <= testY < N and rectangles[testX][testY] == 1:
                rectangles[testX][testY] = 2
                queue.append([testX, testY])
                area += 1
    
    return area
    
areas = []

for x in range(N):
    for y in range(N):
        if rectangles[x][y] == 1:
            area = BFS(x, y, rectangles)
            areas.append(area)

areas.sort()

print(len(areas))
for area in areas:
    print(area)