import sys
input = sys.stdin.readline

Dictionary = {}
Count = 0
n, m = map(int, input().split())

for _ in range(n):
    alphabet = input().rstrip()
    Dictionary[alphabet] = True

for _ in range(m):
    Word = input().rstrip()
    if Word in Dictionary:
        Count += 1

print(Count)