import sys
input = sys.stdin.readline

from collections import deque

T = int(input())

moves = [
    (2, 1), (2, -1), (-2, 1), (-2, -1),
    (1, 2), (1, -2), (-1, 2), (-1, -2)
]

def bfs(start, end, L):
    queue = deque([start])
    visited = [[False] * L for _ in range(L)]
    visited[start[0]][start[1]] = True
    distance = [[0] * L for _ in range(L)]
    
    while queue:
        x, y = queue.popleft()
        
        if (x, y) == end:
            return distance[x][y]
        
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < L and 0 <= ny < L and not visited[nx][ny]:
                visited[nx][ny] = True
                distance[nx][ny] = distance[x][y] + 1
                queue.append((nx, ny))

for _ in range(T):
    L = int(input())
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())
    
    result = bfs((start_x, start_y), (end_x, end_y), L)
    print(result)