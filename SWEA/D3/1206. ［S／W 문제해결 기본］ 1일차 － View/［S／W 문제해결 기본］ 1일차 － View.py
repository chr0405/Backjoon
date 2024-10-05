
def CountFunc(N, nList):
    count = 0

    for i in range(2, N - 2):
        if nList[i - 1] < nList[i] and nList[i - 2] < nList[i]:
            if nList[i + 1] < nList[i] and nList[i + 2] < nList[i]:
                maxHeight = max(nList[i - 2], nList[i - 1], nList[i + 1], nList[i + 2])
                count += nList[i] - maxHeight
    
    return count

for i in range(1, 11):
    N = int(input().strip())
    nList = list(map(int, input().split()))

    print(f'#{i} {CountFunc(N, nList)}')