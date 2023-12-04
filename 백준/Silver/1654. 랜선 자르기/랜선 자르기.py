K, N = map(int, input().split())
K_list = list(int(input()) for _ in range(K))
Start = 1
End = max(K_list)

while(Start <= End) :
    Mid = (Start + End) // 2
    Cnt = 0
    for i in K_list :
        Cnt += i // Mid
    
    if Cnt >= N: Start = Mid + 1 # 왜 >=이지?
    # N개보다 많이 만드는 것도 N개를 만드는 것에 포함된다
    # 이때 만들 수 있는 최대 랜선의 길이를 구한다
    else : End = Mid - 1

print(End)