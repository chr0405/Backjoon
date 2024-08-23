import sys

N, M = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))
array.sort()
selected = []


def backTracking(start):
    if len(selected) == M:
        print(" ".join(map(str, selected)))
        return
    
    last_used = None
    
    for i in range(start, N):
        if array[i] != last_used :
            selected.append(array[i])
            last_used = array[i]
            backTracking(i + 1)
            selected.pop()

backTracking(0)