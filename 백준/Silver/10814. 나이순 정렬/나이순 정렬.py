import sys
input = sys.stdin.readline

N = int(input().strip())
members = []

for _ in range(N):
    old, name = input().split()
    members.append((int(old), name))

members.sort(key=lambda x: x[0])

for member in members:
    print(member[0], member[1])