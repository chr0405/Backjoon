import sys

N, M = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))
array.sort()
selected = []

def backTracking(start) :
    if len(selected) == M :
        print(" ".join(map(str, selected)))
        return
    
    for i in range(start, N):
            selected.append(array[i])
            backTracking(i + 1)
            selected.pop()

backTracking(0)