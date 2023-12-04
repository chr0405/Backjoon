N, M = map(int, input().split())
Trees = list(map(int, input().split())) # 배열의 요소가 띄어쓰기 간격으로 들어올 때
Start, End = 1, max(Trees)

while Start <= End:
    Mid = (Start + End) // 2
    Cnt = 0
    for Tree in Trees :
        if Tree > Mid :
            Cnt += Tree - Mid
    if Cnt >= M : Start = Mid + 1
    else : End = Mid - 1
print(End)