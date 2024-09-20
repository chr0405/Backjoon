import sys
input = sys.stdin.readline

N = int(input())
ropes = [int(input()) for _ in range(N)]

ropes.sort(reverse=True)

mw = 0

for i in range(N):
    cw = ropes[i] * (i + 1)
    mw = max(mw, cw)

print(mw)