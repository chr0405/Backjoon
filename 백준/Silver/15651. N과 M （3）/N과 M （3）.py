import sys

N, M = map(int, sys.stdin.readline().split())
array = []

def backTracking() :
    if len(array) == M :
        print(" ".join(map(str, array)))
        return
    
    for i in range(1, N + 1):
        array.append(i)
        backTracking()
        array.pop()

backTracking()