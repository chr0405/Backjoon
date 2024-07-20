import sys

input = sys.stdin.read
data = input().split()
N = int(data[0])

stack = []
output = []

index = 1

for _ in range(N):
    command = int(data[index])
    if command == 1:
        stack.append(int(data[index + 1]))
        index += 2
    elif command == 2:
        if stack:
            output.append(stack.pop())
        else:
            output.append(-1)
        index += 1
    elif command == 3:
        output.append(len(stack))
        index += 1
    elif command == 4:
        if stack:
            output.append(0)
        else:
            output.append(1)
        index += 1
    elif command == 5:
        if stack:
            output.append(stack[-1])
        else:
            output.append(-1)
        index += 1

for result in output:
    print(result)