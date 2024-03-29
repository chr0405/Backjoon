import sys
from math import gcd

trees = int(sys.stdin.readline())
firstTree = int(sys.stdin.readline())
treesLength = []

for i in range(trees-1):
    num = int(sys.stdin.readline())
    treesLength.append(num - firstTree)
    firstTree = num

greatest = treesLength[0]

for i in range(1, len(treesLength)):
    greatest = gcd(greatest, treesLength[i])

result = 0

for each in treesLength:
    result += each // greatest - 1

print(result)