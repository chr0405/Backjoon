from collections import deque
import sys

N = int(sys.stdin.readline())
dp = deque(range(1, N + 1))

while len(dp) != 1 :
  dp.popleft()
  temp = dp.popleft()
  dp.append(temp)

print(dp.pop())