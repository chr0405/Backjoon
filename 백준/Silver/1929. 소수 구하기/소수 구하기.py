import sys
input = sys.stdin.readline
import math

def primeFunction(prime):
    if prime == 1:
        return False
    for i in range(2, int(math.sqrt(prime)) + 1):
        if prime % i == 0:
            return False
    return True

M, N = map(int, sys.stdin.readline().split())

for i in range(M, N+1):
    if primeFunction(i):
        print(i)