import sys

rangeNum = int(sys.stdin.readline())

count = 1
stack = []
resultList = []

no = False

for _ in range(rangeNum):

    num = int(sys.stdin.readline())
    
    while count <= num:
        stack.append(count)
        resultList.append('+')
        count += 1
    
    if stack[-1] == num:
        stack.pop()
        resultList.append('-')
    else: 
        no = True
        break

if no == True: print('NO')
else: print(('\n').join(resultList))