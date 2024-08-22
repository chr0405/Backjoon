import sys

N, M = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))
array.sort()
selected = []
printList = []

def backTracking(start) :
    if len(selected) == M :
        if selected not in printList:
            printList.append(selected[:])
            print(" ".join(map(str, selected)))
        return
    
    for i in range(start, N):
            selected.append(array[i])
            backTracking(i)
            selected.pop()

backTracking(0)