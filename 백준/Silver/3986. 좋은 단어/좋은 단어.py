import sys

N = int(sys.stdin.readline())
count = 0

for _ in range(N):

  testCase = sys.stdin.readline().rstrip()
  stack = []
  test = True

  for char in testCase:
    
    if not stack:
      stack.append(char)
    
    else: 
      if char == 'A':
        if stack[-1] == 'A':
          stack.pop()
        else:
          stack.append(char)

      if char == 'B':
        if stack[-1] == 'B':
          stack.pop()
        else:
          stack.append(char)

  if not stack:
    count += 1

print(count)