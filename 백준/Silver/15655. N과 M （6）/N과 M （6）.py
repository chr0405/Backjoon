import sys

N, M = map(int, sys.stdin.readline().split())
arr = sorted(map(int, sys.stdin.readline().split()))

selected = []

def backtrack(start):
    if len(selected) == M:
        print(' '.join(map(str, selected)))
        return
    
    for i in range(start, N):
        selected.append(arr[i])
        backtrack(i + 1)
        selected.pop()

backtrack(0)