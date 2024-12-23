from collections import deque

n = int(input())
queue = deque(range(1, n + 1))

result = []

while len(queue) > 1:
    result.append(queue.popleft())
    queue.append(queue.popleft())

result.append(queue[0])

print(*result)
