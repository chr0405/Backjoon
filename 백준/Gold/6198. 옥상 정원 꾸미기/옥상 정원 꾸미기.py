import sys

N = int(sys.stdin.readline())
stack = []
count = 0

for tower in range(N):
    
    h = int(sys.stdin.readline())
    
    while stack:
        if stack[-1] > h:
            count += len(stack)
            break
        else:
            stack.pop()
    stack.append(h)

print(count)