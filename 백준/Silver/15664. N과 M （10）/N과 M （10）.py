import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

visited = [False] * N
result = []

def backtrack(depth, start):
    if depth == M:
        print(' '.join(map(str, result)))
        return
    
    prev = -1
    for i in range(start, N):
        if not visited[i] and arr[i] != prev:
            visited[i] = True
            result.append(arr[i])
            backtrack(depth + 1, i + 1)
            result.pop()
            visited[i] = False
            prev = arr[i]

backtrack(0, 0)