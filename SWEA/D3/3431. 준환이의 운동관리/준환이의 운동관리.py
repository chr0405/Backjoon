T = int(input().strip())

for i in range(1, T+1):
    L, U, X = map(int, input().split())
    answer = 0
    
    if X < L:
        answer = L - X
    elif X > U:
        answer = -1
    else: answer = 0
    
    print(f'#{i} {answer}')