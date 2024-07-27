from collections import deque

n = int(input().strip())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

queue = deque()

for i in range(n):
    if a[i] == 0:
        queue.append(b[i])

m = int(input().strip())
commands = list(map(int, input().split()))

result = []

for command in commands:
    queue.appendleft(command)  
    result.append(queue.pop())  

print(' '.join(map(str, result)))