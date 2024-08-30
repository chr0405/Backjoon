import sys

N = int(sys.stdin.readline().strip())
numbers = []

for _ in range(N):
    num = int(sys.stdin.readline().strip())
    numbers.append(num)

numbers.sort()

print("\n".join(map(str, numbers)))
