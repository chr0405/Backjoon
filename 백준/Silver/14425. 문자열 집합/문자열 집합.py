import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S = set(input() for i in range(N))

Count = 0
for j in range(M):
    Word = input()
    if Word in S:
        Count += 1
print(Count)