from collections import deque
import sys

N = int(sys.stdin.readline().rstrip())

array = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 상하좌우
testX = [0, 0, -1, 1]
testY = [1, -1, 0, 0]

def BFS(x, y, height, visited):
    queue = deque([[x, y]])
    visited[x][y] = True

    while queue:
        initialX, initialY = queue.popleft()

        for offset in range(4):
            testValueX = initialX + testX[offset]
            testValueY = initialY + testY[offset]

            if 0 <= testValueX < N and 0 <= testValueY < N and not visited[testValueX][testValueY] and array[testValueX][testValueY] > height:
                queue.append([testValueX, testValueY])
                visited[testValueX][testValueY] = True

maxCount = 0
max_height = max(map(max, array))

for height in range(max_height):
    visited = [[False] * N for _ in range(N)]
    count = 0

    for x in range(N):
        for y in range(N):
            if array[x][y] > height and not visited[x][y]:
                BFS(x, y, height, visited)
                count += 1
    maxCount = max(maxCount, count)

print(maxCount)