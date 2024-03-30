import sys
input=sys.stdin.readline
import math

testCase = int(input())

def primeCheckFunc(n):
    for i in range(2 ,int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

for i in range(testCase):
    n=int(input())
    while 1 :
        if n == 0 or n == 1 :
            print(2)
            break
        if primeCheckFunc(n) :
            print(n)
            break
        else :
            n += 1