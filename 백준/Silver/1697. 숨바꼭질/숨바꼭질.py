import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

arr = [-1] * 100001

def BFS():
    arr[N] = 0
    queue = deque([N])

    while True:
        startPosition = queue.popleft()
        
        for testValue in [-1, 1, startPosition]:
            if testValue == startPosition:
                testPosition = startPosition * 2
            else:
                testPosition = startPosition + testValue

            if 0 <= testPosition <= 100000 and arr[testPosition] == -1:
                arr[testPosition] = arr[startPosition] + 1
                queue.append(testPosition)

            if testPosition == K:
                return arr[K]

print(BFS())