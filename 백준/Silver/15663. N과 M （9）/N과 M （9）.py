import sys

N, M = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))
array.sort()
selected = []

used = [False] * N

def backTracking():
    if len(selected) == M:
        print(" ".join(map(str, selected)))
        return
    
    last_used = None
    
    for i in range(N):
        if not used[i] and (array[i] != last_used):
            used[i] = True
            selected.append(array[i])
            last_used = array[i]
            backTracking()
            used[i] = False
            selected.pop()

backTracking()