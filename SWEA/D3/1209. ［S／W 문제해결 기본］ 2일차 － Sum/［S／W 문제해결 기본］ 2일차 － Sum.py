for _ in range(10):

    tc = int(input().strip())
    totalNum = [list(map(int, input().split())) for _ in range(100)]
    totalNum_reverse = list(zip(*totalNum))
    slashCount = 0
    backSlashCount = 0
    rowColMax = 0

    for i in range(100):
        slashCount += totalNum[i][i]
        backSlashCount += totalNum[i][99-i]
        rowColMax = max(rowColMax, sum(totalNum[i]), sum(totalNum_reverse[i]))
    
    answer = max(slashCount, backSlashCount, rowColMax)

    print(f'#{tc} {answer}')