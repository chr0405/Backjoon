import sys
sys.setrecursionlimit(150000)
input = sys.stdin.readline

N, M, R = map(int, input().split())

ConnectList = [[] for _ in range(N+1)]
CheckList = [0]*(N+1) # 범위가 N까지로 설정됨
Count = 1

for _ in range(M):
    i, j = map(int, input().split())
    ConnectList[i].append(j)
    ConnectList[j].append(i)

# DFS
def DFS(v):
    global Count
    CheckList[v] = Count
    ConnectList[v].sort()
    for _ in ConnectList[v]:
        if CheckList[_] == 0:
            Count += 1
            DFS(_)

DFS(R)

for _ in range(1, N+1):
    print(CheckList[_])