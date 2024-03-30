import sys
input=sys.stdin.readline
import math

A1, B1 = map(int, input().split())
A2, B2 = map(int, input().split())

resultA = (B1 * A2) + (B2 * A1)
resultB = B1 * B2

def GCD(A, B):
    while B:
        A, B = B, A%B
    return A

gcd = GCD(resultA, resultB)
resultA = int(resultA/gcd)
resultB = int(resultB/gcd)

print(resultA, resultB)