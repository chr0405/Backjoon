import sys
input = sys.stdin.readline

testCase = int(input().strip())
pArray = [[0, 0] for _ in range(41)]

pArray[0][0] = 1
pArray[0][1] = 0
pArray[1][0] = 0
pArray[1][1] = 1

for _ in range(testCase):
    N = int(input().strip())
    
    if N == 0:
        print(pArray[0][0], pArray[0][1])
    elif N == 1:
        print(pArray[1][0], pArray[1][1])
    else:
        for i in range(2, N + 1):
            pArray[i][0] = pArray[i - 1][0] + pArray[i - 2][0]
            pArray[i][1] = pArray[i - 1][1] + pArray[i - 2][1]
        print(pArray[N][0], pArray[N][1])
    