import sys

N, M = map(int, sys.stdin.readline().split())
array = []

def backTracking(start) :
    if len(array) == M :
        print(" ".join(map(str, array)))
        return
    
    for i in range(start, N + 1):
        array.append(i)
        backTracking(i)
        array.pop()

backTracking(1)