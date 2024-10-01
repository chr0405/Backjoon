import sys
input = sys.stdin.readline

T = int(input().strip())
P = list([1] * (100 + 1))

for i in range(4, 100 + 1):
    P[i] = P[i - 2] + P[i - 3]

for _ in range(T):
    N = int(input().strip())
    print(P[N])