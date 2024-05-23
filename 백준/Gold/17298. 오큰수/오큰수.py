import sys

A = int(sys.stdin.readline())
AList = list(map(int, sys.stdin.readline().split()))
stack = []
NGEList = []

for number in reversed(AList):

    while stack:
        if stack[-1] > number:
            NGEList.append(str(stack[-1]))
            break
        else:
            stack.pop()

    if not stack:
        NGEList.append('-1')

    stack.append(number)

print(" ".join(reversed(NGEList)))