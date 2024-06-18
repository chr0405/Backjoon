import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

maze = []
dist = []

for _ in range(N):
  maze.append(list(map(int, sys.stdin.readline().strip())))
  dist.append([-1 for _ in range(M)])

def BFS(x, y):
  queue = deque()
  queue.append((x, y))
  dist[x][y] = 1

  testX = [1, -1, 0, 0]
  testY = [0, 0, 1, -1]

  while queue:
    x, y = queue.popleft()

    for i in range(4):
      xPosition = testX[i] + x
      yPosition = testY[i] + y

      if 0 <= xPosition < N and 0 <= yPosition < M and maze[xPosition][yPosition] == 1 and dist[xPosition][yPosition] == -1:
        queue.append((xPosition, yPosition))
        dist[xPosition][yPosition] = dist[x][y] + 1

  return dist[N-1][M-1]

print(BFS(0, 0))