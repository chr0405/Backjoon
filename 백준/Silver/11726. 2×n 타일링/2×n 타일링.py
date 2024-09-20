import sys

n = int(sys.stdin.readline().strip())

D = [0] * (n + 1)
D[1] = 1

if n >= 2:
    D[2] = 2

if n == 1:
    print(1)
else:
    for i in range(3, n + 1):
        D[i] = (D[i-1] + D[i-2]) % 10007
    print(D[n])