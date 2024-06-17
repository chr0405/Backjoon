import sys
from collections import deque

row, col = map(int, sys.stdin.readline().split())

paper = []
artCount = 0
maxSize = 0

for _ in range(row):
  paper.append(list(map(int, sys.stdin.readline().split())))

def BFS(x, y):
  paper[x][y] = 0 # 방문했으니
  testX = [1, -1, 0, 0]
  testY = [0, 0, 1, -1]
  size = 1

  queue = deque()
  queue.append([x, y])

  while queue:
    x, y = queue.popleft()

    for i in range(4):

      xPosition = testX[i] + x
      yPosition = testY[i] + y

      if 0 <= xPosition < row and 0 <= yPosition < col and paper[xPosition][yPosition] == 1:
        queue.append([xPosition, yPosition])
        paper[xPosition][yPosition] = 0
        size += 1

  return size
    

for i in range(row):
  for j in range(col):
    if paper[i][j] == 1:
      artCount += 1
      maxSize = max(BFS(i, j), maxSize)

print(artCount)
print(maxSize)