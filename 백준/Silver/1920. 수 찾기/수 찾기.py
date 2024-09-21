import sys
input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().split()))
A.sort()

M = int(input())
mList = list(map(int, input().split()))

def binary_search(target):
    left, right = 0, len(A) - 1

    while left <= right:
        mid = (left + right) // 2
        if A[mid] == target:
            return 1
        elif A[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return 0

for num in mList:
    print(binary_search(num))