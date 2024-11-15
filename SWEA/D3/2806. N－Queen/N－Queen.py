T = int(input().strip())

def DFS(i, checkCol, rDiag, lDiag):
    global answer

    if i == N:
        answer += 1
        return

    for j in range(N):
        if checkCol[j] and rDiag[i+j] and lDiag[(j-i) + (N-1)]:
            checkCol[j] = False
            rDiag[i+j] = False
            lDiag[(j-i) + (N-1)] = False

            DFS(i+1, checkCol, rDiag, lDiag)

            checkCol[j] = True
            rDiag[i + j] = True
            lDiag[(j - i) + (N - 1)] = True

for tc in range(1, T+1):
    N = int(input().strip())
    checkCol = [True] * N
    rDiag = [True] * ((N*2)-1)
    lDiag = [True] * ((N*2)-1)
    answer = 0

    DFS(0, checkCol, rDiag, lDiag)

    print(f'#{tc} {answer}')