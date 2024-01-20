import sys
n = int(input())
list = [0] * 10001
for i in range(n):
    a = int(sys.stdin.readline())
    list[a] += 1
for i in range(10001):
    if list[i] > 0:
        for j in range(list[i]):
            print(i)