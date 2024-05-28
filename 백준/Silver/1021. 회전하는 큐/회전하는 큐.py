from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split())

MList = list(map(int, sys.stdin.readline().split()))
Ndq = deque(number for number in range(1, N + 1))

count = 0

for selectNumber in MList:
  while 1:
    if Ndq[0] == selectNumber:
      Ndq.popleft()
      break
    elif Ndq.index(selectNumber) < len(Ndq)/2: # 첫 번째 원소 마지막으로 이동
      while Ndq[0] != selectNumber:
        Ndq.append(Ndq.popleft())  
        count += 1
    else:
      while Ndq[0] != selectNumber: # 마지막 원소 첫 번째로 이동
        Ndq.appendleft(Ndq.pop())  
        count += 1

print(count)