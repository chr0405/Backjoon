import sys
input = sys.stdin.readline

N = int(input())
nList = [int(input()) for _ in range(N)]

nList.sort()

xSUMy = []
for i in range(N):
    for j in range(i, N):
        xSUMy.append(nList[i] + nList[j])

xSUMy.sort()

def binary_search(target):
    left, right = 0, len(xSUMy) - 1
    while left <= right:
        mid = (left + right) // 2
        if xSUMy[mid] == target:
            return True
        elif xSUMy[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

answer = 0
for k in range(N):
    for z in range(k):
        target = nList[k] - nList[z]
        if binary_search(target):
            answer = max(answer, nList[k])

print(answer)