import sys

stack = []

for _ in range(int(sys.stdin.readline())): # K
    command = int(sys.stdin.readline())
    if command == 0 :
        stack.pop()
    else : stack.append(command)

print(sum(stack))