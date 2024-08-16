import sys

N, M = map(int, sys.stdin.readline().split())
array = []

def backTracking(startPorint) :
    if len(array) == M :
        print(" ".join(map(str, array)))
        return
    
    for i in range(startPorint, N + 1):
        array.append(i)
        backTracking(i + 1)
        array.pop()

backTracking(1)