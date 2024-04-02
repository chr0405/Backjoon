import math
import sys
sys.setrecursionlimit(200000)
input = sys.stdin.readline

# def primeFunction(prime):
#     if prime < 2:
#         return False
#     for i in range(2, int(math.sqrt(prime)) + 1):
#         if prime % i == 0:
#             return False
#     return True

# while True:
#     n = int(input())
    
#     if n == 0:
#         break
    
#     count = 0
#     for i in range(n+1, (2*n)+1):
#         if primeFunction(i):
#             count += 1
#     print(count)

nRange = 123456*2+1
nList = [1] * nRange
for i in range(1, nRange):
    if i == 1:
        continue
    for j in range(2, int(math.sqrt(i))+1):
        if i % j == 0:
            nList[i] = 0
            break

while True:
    n = int(input())
    
    if n == 0:
        break
    
    prime = 0
    for i in range(n+1, 2*n+1):
            prime += nList[i]
    print(prime)