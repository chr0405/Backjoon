import sys

T = int(input())
i = 0
while i < T :
    i += 1
    A, B = map(int, sys.stdin.readline().split())
    print(A + B)