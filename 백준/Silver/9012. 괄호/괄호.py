import sys

N = int(sys.stdin.readline())

for _ in range(N):

  testCase = sys.stdin.readline().rstrip()
  stack = []
  test = True

  for char in testCase:
    if char == '(':
      stack.append(char)
    else :
      if not stack:
        print('NO')
        test = False
        break
      else:
        stack.pop()

  if test and stack:
    print('NO')
  elif test and not stack:
    print('YES')