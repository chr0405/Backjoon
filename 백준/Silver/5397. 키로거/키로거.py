import sys

testCaseNub = int(sys.stdin.readline())

for _ in range(testCaseNub):
    testCase = list(sys.stdin.readline().rstrip())
    leftTemp = []
    rightTemp = []
    for char in testCase:
        if char == '<':
            if leftTemp:
                rightTemp.append(leftTemp.pop())
        elif char == '>':
            if rightTemp:
                leftTemp.append(rightTemp.pop())
        elif char == '-':
            if leftTemp:
                leftTemp.pop()
        else : leftTemp.append(char)
    leftTemp.extend(reversed(rightTemp))
    print(''.join(leftTemp))
