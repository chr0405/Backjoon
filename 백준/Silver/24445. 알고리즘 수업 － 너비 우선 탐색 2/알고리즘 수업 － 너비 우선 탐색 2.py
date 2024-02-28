import sys
sys.setrecursionlimit(200000)
from collections import deque
input = sys.stdin.readline

N, M, R = map(int, input().split())

ConnectList = [[] for _ in range(N+1)]
CheckList = [0]*(N+1) # 범위가 N까지로 설정됨
Count = 1

for _ in range(M):
    i, j = map(int, input().split())
    ConnectList[i].append(j)
    ConnectList[j].append(i)

# BFS
CheckList[R] = 1
Q = deque([R])

while Q: # Q가 비어있지 않다면
    u = Q.popleft()
    ConnectList[u].sort(reverse=True)
    for v in ConnectList[u]: # u 노드와 인접한 모든 v 노드들에 대해서
        if CheckList[v] == 0:
            Q.append(v)
            Count += 1
            CheckList[v] = Count

for _ in range(1, N+1):
    print(CheckList[_])