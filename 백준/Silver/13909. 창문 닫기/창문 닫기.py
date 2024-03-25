import sys
N = int(sys.stdin.readline())

result = 0
i = 1

while i * i <= N:
    i += 1
    result += 1

print(result)