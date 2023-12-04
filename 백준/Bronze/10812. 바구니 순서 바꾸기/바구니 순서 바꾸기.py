N, M = map(int, input().split())
N_list = [i for i in range(1, N + 1)]
for _ in range(M) :
    i, j, k = map(int, input().split())
    i, j, k = i - 1, j - 1, k - 1
    N_list = N_list[:i] + N_list[k:j+1] + N_list[i:k] + N_list[j+1:]
for i in (N_list) :
    print(i, end=" ")