import sys
input = sys.stdin.readline

ComputerCount = int(input())
EdgeCount = int(input())

# 0부터 시작하니까 + 1를 한다
# (n + 1)*(1) 행렬
Graph = [[] for _ in range(ComputerCount + 1)]
Check = [0]*(ComputerCount+1)
Count = 0

# 엣지를 받고 그래프 생성
# 연결 리스트 방식
for _ in range(EdgeCount):
    i, j = map(int, input().split())
    Graph[i] += [j]
    Graph[j] += [i]

def DFS(v):
    Check[v] = 1
    for _ in Graph[v]:
        if Check[_] == 0:
            DFS(_)

DFS(1)
print(sum(Check)-1)