import sys

N = int(sys.stdin.readline())
NList = list(map(int, sys.stdin.readline().split()))
stack = []
resultList = []

for num in range(N):
    while stack:
        if stack[-1][1] >= NList[num]:
            resultList.append(str(stack[-1][0] + 1))
            break
        else : stack.pop()
    if not stack:
        resultList.append("0")
    stack.append([num, NList[num]])

print(' '.join(resultList))