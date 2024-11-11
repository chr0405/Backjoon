import sys
from collections import deque

input = sys.stdin.readline

# 상하좌우
offsetY = [1, -1, 0, 0]
offsetX = [0, 0, -1, 1]

def BFS(y, x):
    global NxM_matrix
    global visited_matrix

    queue = deque([])

    queue.append((y, x))

    while queue:
        # BFS의 경우 선입선출로 방문
        nowY, nowX = queue.popleft()
        visited_matrix[nowY][nowX] = True

        for offsetIndex in range(4):
            testY = nowY + offsetY[offsetIndex]
            testX = nowX + offsetX[offsetIndex]
            
            # 메트릭스 범위 안에 있으며, 배추의 위치 중 방문하지 않은 배추 위치에 한하여
            if 0 <= testY < N and 0 <= testX < M and NxM_matrix[testY][testX] == 1 and not visited_matrix[testY][testX]:
                visited_matrix[testY][testX] = True
                queue.append((testY, testX))
        
    return 1

testCase = int(input().strip())

for tc in range(testCase):
    # 가로 길이(열의 갯수), 세로 길이(행의 갯수), 배추가 심어져 있는 위치의 개수
    M, N, K = map(int, input().split())
    NxM_matrix = list([0] * M for _ in range(N))
    visited_matrix = list([False] * M for _ in range(N))
    answer = 0

    for _ in range(K):
        X, Y = map(int, input().split())
        NxM_matrix[Y][X] = 1
    
    for y in range(N):
        for x in range(M):
            if NxM_matrix[y][x] == 1 and visited_matrix[y][x] == False:
                answer += BFS(y, x)
    
    print(answer)
