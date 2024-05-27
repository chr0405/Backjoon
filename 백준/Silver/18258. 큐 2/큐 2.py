from collections import deque
import sys

N = int(sys.stdin.readline())

dq = deque()

for i in range(N):
  
  command = sys.stdin.readline().split()

  if command[0] == 'push':
    dq.append(command[1])

  elif command[0] == 'pop':
    if dq:
      print(dq.popleft())
    else:
      print(-1)

  elif command[0] == 'size':
    print(len(dq))

  elif command[0] == 'empty':
    if not dq:
      print(1)
    else:
      print(0)

  elif command[0] == 'front':
    if dq:
      print(dq[0])
    else:
      print(-1)

  elif command[0] == 'back':
    if dq:
      print(dq[-1])
    else:
      print(-1)