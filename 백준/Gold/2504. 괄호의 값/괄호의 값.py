import sys

testCase = list(sys.stdin.readline())

stack = []
temp = 1
result = 0

test = True

for point in range(len(testCase)):

  if testCase[point]=='(':
    temp *= 2
    stack.append(testCase[point])
    
  elif testCase[point]=='[':
    temp *= 3
    stack.append(testCase[point])
    
  elif testCase[point]==')':

    if not stack or stack[-1]!='(':
      test = False
      break

    if testCase[point-1]=='(':
      result += temp
    temp //= 2
    stack.pop()
    
  elif testCase[point]==']':

    if not stack or stack[-1]!='[':
      test = False
      break

    if testCase[point-1]=='[':
      result += temp
    temp //= 3
    stack.pop()

if stack or not test:
  print(0)
else:
  print(result)