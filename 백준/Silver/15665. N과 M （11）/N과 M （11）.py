import sys

N, M = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))
array.sort()
selected = []


def backTracking():
    if len(selected) == M:
        print(" ".join(map(str, selected)))
        return
    
    last_used = None
    
    for i in range(N):
        if array[i] != last_used :
            selected.append(array[i])
            last_used = array[i]
            backTracking()
            selected.pop()

backTracking()