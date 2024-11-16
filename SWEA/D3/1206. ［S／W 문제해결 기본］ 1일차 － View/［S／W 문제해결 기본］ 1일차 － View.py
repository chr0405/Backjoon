
for tc in range(1, 11):
    buildingCount = int(input().strip())
    buildingList = list(map(int, input().split()))
    count = 0
    i = 0

    for _ in range(buildingCount-4):
        checkArray = buildingList[i:i+5]
        if checkArray[2] == max(checkArray):
            checkArray2 = checkArray[0:2]+checkArray[3:5]
            secondMax = max(checkArray2)
            count += checkArray[2] - secondMax
        i += 1

    print(f'#{tc} {count}')