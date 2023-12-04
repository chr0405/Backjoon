def DAQ(X, Y, N):
    Check = N_list[X][Y]
    for i in range(X, X+N):
        for j in range(Y, Y+N):
            if Check != N_list[i][j]:
                Check = -1
                break
    
    if Check == -1:
        print("(", end='')
        N = N // 2
        DAQ(X, Y, N)
        DAQ(X, Y + N, N)
        DAQ(X + N, Y, N)
        DAQ(X + N, Y + N, N)
        print(")", end='')
    
    elif Check == 1 : print(1, end='')
    else : print(0, end='')
        
N = int(input())
N_list = [list(map(int, input())) for i in range(N)]
# 2차원 배열

DAQ(0, 0, N)