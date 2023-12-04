N = int(input()) # 지방의 수
N_list = list(map(int, input().split()))
# 각 지방의 예산요청
M = int(input()) # 총 예산
# Start, End = min(N_list), max(N_list)
Start, End = 0, max(N_list)

while Start <= End :
    Mid = (Start+End) // 2
    Cnt = 0
    for i in N_list :
        if i >= Mid :
            Cnt = Cnt + Mid
        else : Cnt = Cnt + i
    # if Cnt >= M : End = Mid - 1
    if Cnt > M : End = Mid - 1
    else : Start = Mid + 1

# for i in N_list:
#     if i >= Mid : i = Mid

# print(max(N_list))
print(End)