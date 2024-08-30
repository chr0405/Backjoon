import sys

N = int(sys.stdin.readline().strip())
numbers = []

for _ in range(N):
    old, name = sys.stdin.readline().split()
    numbers.append([int(old), name])

numbers.sort(key=lambda x : x[0])

for i in range(N):
    print(numbers[i][0], numbers[i][1], sep=" ")