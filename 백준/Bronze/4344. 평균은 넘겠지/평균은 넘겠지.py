N = int(input())

for _ in range(N):
    N_list = list(map(int, input().split()))
    avg = sum(N_list[1:]) / N_list[0] 
    cnt = 0
    for score in N_list[1:] :
        if score > avg:
            cnt += 1 
    rate = cnt / N_list[0] *100
    print(f'{rate:.3f}%')