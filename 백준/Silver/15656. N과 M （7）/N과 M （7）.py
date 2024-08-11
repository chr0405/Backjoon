import sys

N, M = map(int, sys.stdin.readline().split())
arr = sorted(map(int, sys.stdin.readline().split()))

selected = []

def backtrack():
    if len(selected) == M:
        print(' '.join(map(str, selected)))
        return
    
    for i in range(N):
        selected.append(arr[i])
        backtrack()
        selected.pop()

backtrack()