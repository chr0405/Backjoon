T = int(input().strip())

for TC in range(1, T+1):
    N = int(input().strip())
    answerArray = []
    
    answerArray.append(f'#{TC}')
    
    for i in range(N):
            answerArray.append(f'1/{N}')
    
    print(' '.join(answerArray))