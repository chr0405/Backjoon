def checkDef(checkList):
    return 1 if checkList == checkList[::-1] else 0

for tc in range(1, 11):
    wordLen = int(input().strip())
    wordBoard = [list(input().strip()) for _ in range(8)]
    wordBoardReverse = list(zip(*wordBoard))
    count = 0
    
    for i in range(8):
        for j in range(8 - wordLen + 1):
            count += checkDef(wordBoard[i][j:j + wordLen])
            count += checkDef(wordBoardReverse[i][j:j + wordLen])
    
    print(f'#{tc} {count}')
