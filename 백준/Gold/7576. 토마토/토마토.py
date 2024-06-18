import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
box = []
dist = []

for _ in range(N):
    box.append(list(map(int, sys.stdin.readline().split())))
    dist.append([-1 for _ in range(M)])

queue = deque()

for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            queue.append([i, j])
            dist[i][j] = 0

def BFS():
    global queue
    testX = [1, -1, 0, 0]
    testY = [0, 0, 1, -1]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            xPosition = x + testX[i]
            yPosition = y + testY[i]

            if 0 <= xPosition < N and 0 <= yPosition < M:
                if box[xPosition][yPosition] == 0 and dist[xPosition][yPosition] == -1:
                    dist[xPosition][yPosition] = dist[x][y] + 1
                    queue.append([xPosition, yPosition])

BFS()

result = 0
for i in range(N):
    for j in range(M):
        if box[i][j] == 0 and dist[i][j] == -1:
            print(-1)
            exit(0)
        result = max(result, dist[i][j])

print(result)