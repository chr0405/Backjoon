N = int(input())

for _ in range(N):
    testCase1, testCase2 = map(str, input().split())
    testCase1 = sorted(testCase1)
    testCase2 = sorted(testCase2)
    if testCase1 == testCase2:
        print('Possible')
    else: print('Impossible')