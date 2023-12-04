N, M = map(int, input().split()) 
N_list = [0] * (N + 1)

for m in range(0, M) :
    i, j, k = map(int, input().split())
    for change_range in range(i, j+1) :
        N_list[change_range] = k

for n in range(1, N + 1) :
    print(N_list[n], end = " ")