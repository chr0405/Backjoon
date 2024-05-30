import sys

testCase = sys.stdin.readline().rstrip()
stack=[]
count = 0

for point in range(len(testCase)):

  if testCase[point] == '(':
    stack.append(testCase[point])

  else: # ')'인 경우
    
    # 레이저인 경우
    if testCase[point-1] == '(':
      stack.pop()
      count += len(stack)

    # 쇠 막대기의 끝점인 경우      
    else:
      stack.pop()
      count += 1

print(count)