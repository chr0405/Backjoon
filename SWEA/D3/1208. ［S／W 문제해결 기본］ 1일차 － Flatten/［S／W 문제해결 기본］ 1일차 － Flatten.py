
for tc in range(1, 11):
    answer = 0
    dumpCount = int(input().strip())
    boxList = list(map(int, input().split()))
    complete = False

    for _ in range(dumpCount):
        boxList.sort()

        if boxList[-1] - boxList[0] <= 1:
            complete = True
            break
        else:
            boxList[-1] -= 1
            boxList[0] += 1

    if complete:
        answer = 1
    else:
        boxList.sort()
        answer = boxList[-1] - boxList[0]

    print(f'#{tc} {answer}')