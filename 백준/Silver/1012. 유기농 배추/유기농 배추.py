import sys
sys.setrecursionlimit(10000)

def dfs(x, y):
    # 이동할 네 방향 정의 (상, 하, 좌, 우)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # 방문 처리
    visited[x][y] = True
    
    # 네 방향에 대해 탐색
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m:
            if not visited[nx][ny] and field[nx][ny] == 1:
                dfs(nx, ny)

t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())
    field = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    
    for _ in range(k):
        x, y = map(int, input().split())
        field[y][x] = 1
    
    count = 0
    for i in range(n):
        for j in range(m):
            if field[i][j] == 1 and not visited[i][j]:
                dfs(i, j)
                count += 1
    
    print(count)