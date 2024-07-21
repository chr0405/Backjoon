import sys
from collections import deque

input = sys.stdin.read
data = input().split()
N = int(data[0])

deque_ = deque()
output = []

index = 1

for _ in range(N):
    command = int(data[index])
    if command == 1:
        deque_.appendleft(int(data[index + 1]))
        index += 2
    elif command == 2:
        deque_.append(int(data[index + 1]))
        index += 2
    elif command == 3:
        if deque_:
            output.append(deque_.popleft())
        else:
            output.append(-1)
        index += 1
    elif command == 4:
        if deque_:
            output.append(deque_.pop())
        else:
            output.append(-1)
        index += 1
    elif command == 5:
        output.append(len(deque_))
        index += 1
    elif command == 6:
        if deque_:
            output.append(0)
        else:
            output.append(1)
        index += 1
    elif command == 7:
        if deque_:
            output.append(deque_[0])
        else:
            output.append(-1)
        index += 1
    elif command == 8:
        if deque_:
            output.append(deque_[-1])
        else:
            output.append(-1)
        index += 1

for result in output:
    print(result)