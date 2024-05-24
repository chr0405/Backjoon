import sys

N = int(sys.stdin.readline())

stack = []
totalCount = 0

for _ in range(N):
    
    person = int(sys.stdin.readline())

    # stack 끝값 < person
    while stack and stack[-1][0] < person:
        totalCount += stack.pop()[1]

    # stack 비어있음
    if not stack:
        stack.append((person, 1))
        continue

    # stack 끝값 == person
    if stack and stack[-1][0] == person:
        count = stack.pop()[1]
        totalCount += count

        if stack:
            totalCount += 1
        stack.append((person, count + 1))

    # stack 끝값 > person
    else:
        stack.append((person, 1))
        totalCount += 1
    
print(totalCount)