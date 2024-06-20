import sys
from collections import deque

R, C = map(int, sys.stdin.readline().split())
maze = [list(sys.stdin.readline().strip()) for _ in range(R)]

def BFS(start_points):
    distances = [[-1] * C for _ in range(R)]
    queue = deque(start_points)
    
    for r, c in start_points:
        distances[r][c] = 0  # 시작점의 거리를 0으로 설정
    
    testX = [1, -1, 0, 0]
    testY = [0, 0, 1, -1]
    
    while queue:
        r, c = queue.popleft()
        
        for i in range(4):
            xPosition, yPosition = r + testY[i], c + testX[i]

            if 0 <= xPosition < R and 0 <= yPosition < C and maze[xPosition][yPosition] != '#' and distances[xPosition][yPosition] == -1:
                distances[xPosition][yPosition] = distances[r][c] + 1
                queue.append((xPosition, yPosition))
                
    return distances

def solveDEF():
    fire_start = []
    JH_start = []
    
    for r in range(R):
        for c in range(C):
            if maze[r][c] == 'F':
                fire_start.append((r, c))
            elif maze[r][c] == 'J':
                JH_start.append((r, c))
                
    fire_distances = BFS(fire_start)
    JH_distances = BFS(JH_start)
    
    min_escape_time = float('inf')
    
    for r in range(R):
        for c in range(C):
            if maze[r][c] != '#':
                if (r == 0 or r == R-1 or c == 0 or c == C-1) and JH_distances[r][c] != -1:
                    if fire_distances[r][c] == -1 or JH_distances[r][c] < fire_distances[r][c]:
                        min_escape_time = min(min_escape_time, JH_distances[r][c] + 1)
    
    if min_escape_time == float('inf'):
        return "IMPOSSIBLE"
    else:
        return min_escape_time

print(solveDEF())