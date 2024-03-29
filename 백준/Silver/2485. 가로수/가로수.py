import sys
from math import gcd

trees = int(sys.stdin.readline())

firstTree = int(sys.stdin.readline())

treesLength = []

for i in range(trees-1):
    num = int(sys.stdin.readline())
    treesLength.append(num - firstTree)
    firstTree = num

g = treesLength[0]

for j in range(1, len(treesLength)):
    g = gcd(g, treesLength[j])

result = 0

for each in treesLength:
    result += each // g - 1

print(result)