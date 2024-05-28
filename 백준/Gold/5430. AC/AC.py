from collections import deque
import sys

T = int(sys.stdin.readline())

for _ in range(T):

  p = list(sys.stdin.readline().rstrip()) # 수행할 함수
  n = int(sys.stdin.readline())
  dq = deque(sys.stdin.readline()[1:-2].split(","))

  errorTest = True
  RCommand = 0

  for command in p:
    if command == 'R':
      RCommand += 1
    elif command == 'D':
      if len(dq) < 1 or dq == deque(['']):
          errorTest = False
          print("error")
          break
      else:
        if RCommand % 2 == 0:
          dq.popleft()
        else:
          dq.pop()

  if errorTest:
    if RCommand % 2 == 0:
      print("[" + ",".join(dq) + "]")
    else:
      dq.reverse()
      print("[" + ",".join(dq) + "]")