T = int(input().strip())

for TC in range(1, T+1):
    N, K = map(int, input().split())
    kList = list(map(int, input().split()))
    notSubmitList = []
    
    for n in range(1, N+1):
        if n not in kList:
            notSubmitList.append(n)
    
    notSubmitList.sort()
    answer = ' '.join(map(str, notSubmitList))

    print(f'#{TC} {answer}')