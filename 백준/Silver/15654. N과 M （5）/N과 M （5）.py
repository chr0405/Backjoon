import sys

N, M = map(int, sys.stdin.readline().split())
arr = sorted(map(int, sys.stdin.readline().split()))

selected = []
used = [False] * N

def backtrack():
    if len(selected) == M:
        print(' '.join(map(str, selected)))
        return
    
    for i in range(N):
        if not used[i]:
            used[i] = True
            selected.append(arr[i])
            backtrack()
            selected.pop()
            used[i] = False

backtrack()