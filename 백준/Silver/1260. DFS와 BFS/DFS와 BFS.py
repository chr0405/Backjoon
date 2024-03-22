import sys
input = sys.stdin.readline
from collections import deque

N, M, V = map(int, input().split())
ConnectList = [[] for _ in range(N+1)]

for i in range(M) :
    i, j = map(int, input().split())
    ConnectList[i].append(j)
    ConnectList[j].append(i)

# dfs용
visited_dfs = [0] * (N+1)
# bfs용
visited_bfs = [0] * (N+1)

#dfs
def dfs(V):
    visited_dfs[V] = 1
    print(V, end=" ")
    ConnectList[V].sort()
    for i in ConnectList[V]:
        if not visited_dfs[i]:
            dfs(i)

#bfs
def bfs(V):
    q = deque([V])
    visited_bfs[V] = 1
    ConnectList[V].sort()
    while q:
        V = q.popleft()
        print(V, end=" ")
        for i in ConnectList[V]:
            if not visited_bfs[i]:
                q.append(i)
                visited_bfs[i] = 1
dfs(V)
print()
bfs(V)