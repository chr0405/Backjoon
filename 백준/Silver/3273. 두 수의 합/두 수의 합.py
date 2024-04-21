import sys
input = sys.stdin.readline

n = int(input())
Arr = sorted(list(map(int, input().split())))
x = int(input())

count = 0
left, right = 0, n-1
while left < right:
    temp = Arr[left] + Arr[right]
    if temp == x:
        count += 1
        left += 1
    elif temp < x:
        left += 1
    else:
        right -= 1

print(count)